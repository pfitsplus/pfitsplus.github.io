#!/usr/bin/env python3
"""ads_to_posts.py – Fetch publications from the PFITS+ ADS public library and
generate draft news posts in the Jekyll _posts/ directory.

Usage:
    python scripts/ads_to_posts.py [--dry-run] [--posts-dir _posts]

Required environment variable:
    ADS_TOKEN  Your NASA ADS API token.
               Obtain one at https://ui.adsabs.harvard.edu/user/settings/token

The script:
1. Reads all bibcodes from the configured ADS public library.
2. Scans existing posts for ADS links to identify already-posted papers.
3. For each new paper, writes a draft Markdown file into _posts/ that matches
   the site's publication-post conventions (title, date, categories, tags,
   ADS link, journal citation line, and author list with profile links).
"""

import argparse
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import requests


# ── Configuration ─────────────────────────────────────────────────────────────

ADS_API_BASE = "https://api.adsabs.harvard.edu/v1"

# Public library ID – taken from the Publications nav link in _data/navigation.yml
ADS_LIBRARY_ID = "_-AhcKuYSKyaIu_U5ebVsA"

# Metadata fields to retrieve from ADS for each paper
ADS_FIELDS = ",".join([
    "bibcode", "title", "author", "year", "pubdate",
    "pub", "volume", "page", "keyword", "doctype",
    "identifier", "doi",
])

# ── Journal name maps ──────────────────────────────────────────────────────────

# Bibcode journal code → full journal name (italicised in post body)
JOURNAL_FULL_NAMES = {
    "A&A":   "Astronomy & Astrophysics",
    "A&AS":  "Astronomy & Astrophysics Supplement Series",
    "AJ":    "The Astronomical Journal",
    "AN":    "Astronomische Nachrichten",
    "ApJ":   "The Astrophysical Journal",
    "ApJL":  "The Astrophysical Journal Letters",
    "ApJS":  "The Astrophysical Journal Supplement Series",
    "Icar":  "Icarus",
    "MNRAS": "Monthly Notices of the Royal Astronomical Society",
    "NatAs": "Nature Astronomy",
    "PASP":  "Publications of the Astronomical Society of the Pacific",
    "PASA":  "Publications of the Astronomical Society of Australia",
    "PhRvL": "Physical Review Letters",
    "PhRvD": "Physical Review D",
    "PhRvE": "Physical Review E",
    "RNAAS": "Research Notes of the AAS",
}

# Bibcode journal code → filename-safe abbreviation (lowercase)
# Defaults to the lowercased bibcode code; override only when needed
JOURNAL_ABBREVS = {
    "A&A":  "aa",
    "A&AS": "aas",
}

# ── Team member registry ───────────────────────────────────────────────────────

# last name (lowercase) → (display name as used in posts, permalink slug)
# Keep in sync with _team/ collection; update when team membership changes.
TEAM_MEMBERS = {
    "balaji":      ("Sricharan Balaji",      "balaji-sricharan"),
    "baronett":    ("Stanley A. Baronett",   "baronett-stanley"),
    "brouillette": ("Olivia Brouillette",    "brouillette-olivia"),
    "canas":       ("Manuel Canas",          "canas-manuel"),
    "carrera":     ("Daniel Carrera",        "carrera-daniel"),
    "chang":       ("Eonho Chang",           "chang-eonho"),
    "childs":      ("Anna Childs",           "childs-anna"),
    "davenport":   ("Abigail Davenport",     "davenport-abigail"),
    "de cun":      ("Victoria de Cun",       "decun-victoria"),
    "dyda":        ("Sergei Dyda",           "dyda-sergei"),
    "godines":     ("Daniel Godines",        "godines-daniel"),
    "hall":        ("Weston Hall",           "hall-weston"),
    "hutnik":      ("Leopold Hutnik",        "hutnik-leopold"),
    "krapp":       ("Leo Krapp",             "krapp-leo"),
    "lehmann":     ("Marius Lehmann",        "lehmann-marius"),
    "li":          ("Rixin Li",              "rixin-li"),
    "lim":         ("Jeonghoon Lim",         "lim-jeonghoon"),
    "lyra":        ("Wladimir Lyra",         "lyra-wladimir"),
    "mohov":       ("Aleksey Mohov",         "mohov-aleksey"),
    "olds":        ("Camden Olds",           "olds-camden"),
    "rea":         ("David Rea",             "rea-david"),
    "sengupta":    ("Debanjan Sengupta",     "sengupta-debanjan"),
    "serviss":     ("Eleanor Serviss",       "serviss-eleanor"),
    "simon":       ("Jacob B. Simon",        "simon-jacob"),
    "tanvir":      ("Tabassum Tanvir",       "tanvir-tabassum"),
    "umurhan":     ("Orkan M. Umurhan",      "umurhan-orkan"),
    "yang":        ("Chao-Chin Yang",        "yang-chao-chin"),
    "youdin":      ("Andrew N. Youdin",      "youdin-andrew"),
}


# ── ADS API helpers ────────────────────────────────────────────────────────────

# Retry configuration for handling ADS API rate limiting (HTTP 429)
ADS_MAX_RETRIES = 5
ADS_BACKOFF_BASE = 2  # seconds; delay for attempt n = ADS_BACKOFF_BASE ** n


def _ads_request(
    session: requests.Session, method: str, url: str, **kwargs
) -> requests.Response:
    """Make an HTTP request to the ADS API, retrying on 429 with exponential backoff.

    On a 429 response the ``Retry-After`` header is honoured when present;
    otherwise the delay doubles with each attempt (2s, 4s, 8s, …).
    Raises :class:`requests.HTTPError` if retries are exhausted.
    """
    for attempt in range(ADS_MAX_RETRIES + 1):
        resp = session.request(method, url, **kwargs)
        if resp.status_code != 429:
            resp.raise_for_status()
            return resp

        if attempt == ADS_MAX_RETRIES:
            print(
                f"ERROR: ADS rate limit (429) not resolved after "
                f"{ADS_MAX_RETRIES} retries – giving up.",
                file=sys.stderr,
            )
            resp.raise_for_status()

        # Determine how long to wait before the next attempt
        retry_after = resp.headers.get("Retry-After")
        if retry_after is not None:
            try:
                delay = float(retry_after)
            except ValueError:
                delay = ADS_BACKOFF_BASE ** (attempt + 1)
        else:
            delay = ADS_BACKOFF_BASE ** (attempt + 1)

        print(
            f"  ADS rate limit hit (429). Retrying in {delay:.0f}s "
            f"(attempt {attempt + 1}/{ADS_MAX_RETRIES}) …",
            file=sys.stderr,
        )
        time.sleep(delay)


def ads_session(token: str) -> requests.Session:
    """Return a requests Session pre-configured with the ADS Bearer token."""
    s = requests.Session()
    s.headers["Authorization"] = f"Bearer {token}"
    return s


def fetch_library_bibcodes(session: requests.Session) -> list:
    """Return all bibcodes in the configured ADS public library (paginated)."""
    bibcodes: list = []
    rows = 100
    start = 0
    while True:
        resp = _ads_request(
            session, "GET",
            f"{ADS_API_BASE}/biblib/libraries/{ADS_LIBRARY_ID}",
            params={"rows": rows, "start": start},
        )
        data = resp.json()
        docs = data.get("documents", [])
        bibcodes.extend(docs)
        if len(docs) < rows:
            break
        start += rows
    return bibcodes


def fetch_paper_metadata(session: requests.Session, bibcodes: list) -> list:
    """Fetch full metadata for *bibcodes* using the ADS big-query endpoint."""
    if not bibcodes:
        return []
    papers: list = []
    chunk_size = 200
    for i in range(0, len(bibcodes), chunk_size):
        chunk = bibcodes[i : i + chunk_size]
        body = "bibcode\n" + "\n".join(chunk)
        resp = _ads_request(
            session, "POST",
            f"{ADS_API_BASE}/search/bigquery",
            params={"q": "*:*", "fl": ADS_FIELDS, "rows": chunk_size},
            data=body.encode(),
            headers={"Content-Type": "big-query/csv"},
        )
        papers.extend(resp.json().get("response", {}).get("docs", []))
    return papers


# ── Existing-post helpers ──────────────────────────────────────────────────────

_BIBCODE_RE = re.compile(
    r"https?://ui\.adsabs\.harvard\.edu/abs/([^/]+)/abstract"
)


def posted_bibcodes(posts_dir: Path) -> set:
    """Return the set of ADS bibcodes already referenced by posts in *posts_dir*."""
    codes: set = set()
    for md in posts_dir.glob("*.md"):
        text = md.read_text(encoding="utf-8")
        for m in _BIBCODE_RE.finditer(text):
            codes.add(m.group(1))
    return codes


# ── Formatting helpers ─────────────────────────────────────────────────────────

def journal_code_from_bibcode(bibcode: str) -> str:
    """Extract the journal abbreviation embedded in a bibcode.

    Bibcode structure: YYYYJJJJJVVVPPPATTTTT
    Chars 4-8 (0-indexed) hold the journal code, right-padded with dots.
    """
    return bibcode[4:9].rstrip(".")


def filename_journal_abbrev(code: str) -> str:
    """Return the lowercase, filename-safe journal abbreviation."""
    return JOURNAL_ABBREVS.get(code, code.lower())


def publication_date(paper: dict) -> datetime:
    """Parse the ADS pubdate field (YYYY-MM-00 / YYYY-00-00) into a datetime."""
    raw = paper.get("pubdate", "") or paper.get("year", "2000") + "-01"
    parts = raw.split("-")
    year = int(parts[0]) if parts else 2000
    month = int(parts[1]) if len(parts) > 1 and parts[1] != "00" else 1
    day = 1  # ADS days are almost always "00"
    return datetime(year, month, day, 8, 0, 0)


def lookup_team_member(ads_name: str) -> tuple[str, str] | None:
    """Return (display_name, slug) for an ADS author name, or None if not found.

    ADS names are in "Last, First M." format.
    """
    last = ads_name.split(",")[0].strip().lower()
    return TEAM_MEMBERS.get(last)


def format_author(ads_name: str) -> str:
    """Format one ADS author as a Markdown link if they are a team member."""
    member = lookup_team_member(ads_name)
    if member:
        display, slug = member
        return f"[{display}](/team/{slug}/)"
    # Fall back to the raw ADS name unchanged
    return ads_name


def format_citation_line(paper: dict) -> str:
    """Return the 'Published in …' line for the post body."""
    bibcode = paper.get("bibcode", "")
    jcode = journal_code_from_bibcode(bibcode)
    doctype = paper.get("doctype", "article")
    pub = paper.get("pub", "")

    volume = str(paper.get("volume") or "")
    pages = paper.get("page") or []
    page_str = str(pages[0]) if pages and pages[0] is not None else ""

    if doctype == "eprint" or jcode == "arXiv":
        # Preprint – try to name the target journal from the ADS 'pub' field
        if pub and "arxiv" not in pub.lower():
            return f"Submitted to *{pub}*."
        return "Submitted for publication."

    full_name = JOURNAL_FULL_NAMES.get(jcode) or pub or jcode
    parts = [f"*{full_name}*"]
    if volume:
        parts.append(volume)
    if page_str:
        parts.append(page_str)
    return "Published in " + ", ".join(parts) + "."


def select_tags(paper: dict) -> list:
    """Return a deduplicated, sorted list of tags for the post front matter.

    Includes:
    - A subset of ADS keywords (astrophysics-relevant, lowercased).
    - Team-member names in "Lastname, Firstname" format (for authors in the team).
    """
    tags: list[str] = []

    # Subject keywords from ADS (skip very generic or administrative ones)
    skip_prefixes = ("arxiv:", "doi:", "isbn:", "issn:")
    # Broad/administrative standalone keywords to always exclude
    skip_exact = {
        "earth and planetary astrophysics",
        "solar and stellar astrophysics",
    }
    seen: set[str] = set()
    raw_keywords = paper.get("keyword") or []
    for kw in raw_keywords:
        kw_clean = str(kw).strip().lower()
        if not kw_clean:
            continue
        if kw_clean.isdigit():
            continue
        if any(kw_clean.startswith(p) for p in skip_prefixes):
            continue
        # Skip hyphenated subcategory tags (e.g. "astrophysics - solar and stellar astrophysics")
        if " - " in kw_clean:
            continue
        if kw_clean in skip_exact:
            continue
        if kw_clean not in seen:
            seen.add(kw_clean)
            tags.append(kw_clean)

    # Team member tags – use the ADS "Lastname, First M." form directly,
    # which matches the site's "Lastname, Firstname" tag convention.
    for ads_name in paper.get("author") or []:
        member = lookup_team_member(ads_name)
        if member:
            tag = ads_name.strip()
            if tag not in seen:
                seen.add(tag)
                tags.append(tag)

    return tags


def generate_post_content(paper: dict) -> str:
    """Return the full Markdown content (front matter + body) for a post."""
    title = (paper.get("title") or ["Untitled"])[0]
    pub_date = publication_date(paper)
    bibcode = paper.get("bibcode", "")
    ads_url = f"https://ui.adsabs.harvard.edu/abs/{bibcode}/abstract"

    tags = select_tags(paper)
    authors_line = ", ".join(
        format_author(a) for a in (paper.get("author") or [])
    )
    citation_line = format_citation_line(paper)

    # Build YAML front matter
    # Escape any embedded double-quotes in the title so the YAML scalar stays valid
    title_escaped = title.replace('"', '\\"')
    # Quote every tag so bare numbers (e.g. "101") are not parsed as YAML integers
    tags_yaml = "\n".join(f'  - "{t}"' for t in tags)
    front_matter = (
        f'---\n'
        f'title: "{title_escaped}"\n'
        f'date: {pub_date.strftime("%Y-%m-%dT%H:%M:%S")}\n'
        f'categories:\n'
        f'  - Publications\n'
        f'tags:\n'
        f'{tags_yaml}\n'
        f'link: {ads_url}\n'
        f'---\n'
    )

    body = f"{citation_line}\n\nAuthors: {authors_line}\n"
    return front_matter + "\n" + body


def make_filename(paper: dict, posts_dir: Path) -> str:
    """Return a unique filename for the post, following pub-journal-lastname convention."""
    bibcode = paper.get("bibcode", "")
    jcode = journal_code_from_bibcode(bibcode)
    journal_slug = filename_journal_abbrev(jcode)

    authors = paper.get("author") or []
    first_author_last = (
        authors[0].split(",")[0].strip().lower() if authors else "unknown"
    )
    # Keep only alphanumeric and hyphens
    first_author_last = re.sub(r"[^a-z0-9]", "", first_author_last)

    pub_date = publication_date(paper)
    date_prefix = pub_date.strftime("%Y-%m-%d")
    base = f"{date_prefix}-pub-{journal_slug}-{first_author_last}"

    # Ensure uniqueness: append -2, -3, … if the base name is taken
    candidate = f"{base}.md"
    counter = 2
    while (posts_dir / candidate).exists():
        candidate = f"{base}-{counter}.md"
        counter += 1
    return candidate


# ── Main ──────────────────────────────────────────────────────────────────────

def parse_args(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be created without writing any files.",
    )
    p.add_argument(
        "--posts-dir",
        default="_posts",
        metavar="DIR",
        help="Path to the Jekyll _posts directory (default: _posts).",
    )
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    posts_dir = Path(args.posts_dir)

    token = os.environ.get("ADS_TOKEN", "").strip()
    if not token:
        print(
            "ERROR: ADS_TOKEN environment variable is not set.\n"
            "Set it to your NASA ADS API token: "
            "https://ui.adsabs.harvard.edu/user/settings/token",
            file=sys.stderr,
        )
        sys.exit(1)

    session = ads_session(token)

    # 1. Fetch all bibcodes from the ADS library
    print(f"Fetching bibcodes from ADS library {ADS_LIBRARY_ID} …")
    try:
        bibcodes = fetch_library_bibcodes(session)
    except requests.HTTPError as exc:
        print(f"ERROR fetching library: {exc}", file=sys.stderr)
        sys.exit(1)
    print(f"  Found {len(bibcodes)} papers in library.")

    # 2. Identify papers that already have a news post
    already_posted = posted_bibcodes(posts_dir)
    print(f"  {len(already_posted)} papers already have posts.")

    new_bibcodes = [b for b in bibcodes if b not in already_posted]
    print(f"  {len(new_bibcodes)} new papers to process.")

    if not new_bibcodes:
        print("No new posts to generate.")
        return

    # 3. Fetch full metadata for new papers
    print("Fetching paper metadata from ADS …")
    try:
        papers = fetch_paper_metadata(session, new_bibcodes)
    except requests.HTTPError as exc:
        print(f"ERROR fetching metadata: {exc}", file=sys.stderr)
        sys.exit(1)

    # Sort oldest-first so the git history is chronologically ordered
    papers.sort(key=lambda p: p.get("pubdate") or p.get("year") or "")

    # 4. Generate post files
    created = []
    for paper in papers:
        filename = make_filename(paper, posts_dir)
        content = generate_post_content(paper)
        filepath = posts_dir / filename

        if args.dry_run:
            print(f"\n── DRY RUN: would write {filepath} ──")
            print(content)
        else:
            filepath.write_text(content, encoding="utf-8")
            print(f"  Created: {filepath}")
        created.append(filename)

    if args.dry_run:
        print(f"\nDry run complete. Would have created {len(created)} post(s).")
    else:
        print(f"\nDone. Created {len(created)} new post draft(s) in {posts_dir}/.")
        print(
            "Review and edit them before committing – in particular check:\n"
            "  • ADS keyword tags (trim to 3–6 relevant terms)\n"
            "  • Author links (verify all team members are linked)\n"
            "  • Citation line (volume/page accuracy)\n"
            "  • Preprint entries (update once formally published)"
        )


if __name__ == "__main__":
    main()
