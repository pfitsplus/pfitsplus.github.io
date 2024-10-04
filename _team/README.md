# Team Members
This folder contains [Markdown](https://www.markdownguide.org/) files for the individual members populating the [**Team**](https://pfitsplus.github.io/team/) page.
To create your own, we recommend copying an existing member profile from your institution (if available) and as close to the structure you want (e.g., a simple paragraph or multiple, extensive sections).
Rename the copy as your `institution-##-lastname-firstname.md`.
The `institution` filename prefix should match an existing header ID at the top of each HTML block listed in [./_pages/team.html](https://github.com/pfitsplus/pfitsplus.github.io/blob/main/_pages/team.html) (e.g., `<h2 id="isu">`).
For a given institution, the double-digit filename prefix `##` should follow these existing conventions based on career level or seniority:
 - `0#` for long-term or permanent positions, e.g.,
   - `00` for Professor, Principal Investigator
   - `01` for Research Professor
   - `02` for Research Scientist
- `1#` for non-permanent postdoctoral positions, e.g.,
   - `10` for Postdoctoral Fellow or Scholar
- `2#` for graduate-level positions, e.g.,
  - `20` for Graduate Fellow, Assistant, or Student

As this `##` ultimately controls the top-to-bottom order displayed under each institution on the [**Team**](https://pfitsplus.github.io/team/) page, the de facto numbering scheme is flexible and can be arbitrarily tailored as desired.
Furthermore, different pages with the same first two prefixes (i.e. `institution-##-`) will be ordered and displayed alphabetically by last name.


## Front Matter
Each file must contain a [YAML](https://yaml.org/) [**front matter**](https://jekyllrb.com/docs/front-matter/) block at the top, sandwiched between triple-dashed lines (`---`), for [Jekyll](https://jekyllrb.com/) to process.
Below is a generic example, followed by a key legend subsection:
```yaml
---
permalink: /team/lastname-firstname/
title: "Lastname, Firstname"
excerpt: "[institution]"
position: "[position]"
header:
  teaser: /assets/images/team/lastname-firstname.jpg
sidebar:
  - title: "Position"
    image: /assets/images/team/lastname-firstname.jpg
    text: "[position]<br>
    <a href='mailto:user@domain.org'>
      <i class='fas fa-fw fa-envelope'></i>Email</a><br>
    <a href='https://github.com/username' target='_blank'
      <i class='fab fa-fw fa-github'></i>GitHub</a><br>
    <a href='https://scholar.google.com/citations?user=ID' target='_blank'>
      <i class='fas fa-fw fa-user-graduate'></i>Google Scholar</a><br>
    <a href='/tags/#lastname-firstname'>
      <i class='fas fa-fw fa-newspaper'></i>News</a><br>
    <a href='https://orcid.org/0000-0000-0000-0000' target='_blank'>
      <i class='fab fa-fw fa-orcid'></i>ORCiD</a>"
  - title: "Research Interests"
    text: "<ul>
    <li> Topic 1
    <li> Topic 2"
---
```
### Key Legend
- `permalink:` After `/team/` the `lastname-firstname` segment should match the end of your Markdown filename without the `.md` extension.
- `title:` Your name—last name *first*, immediately followed by a comma (`,`), and wrapped in **double quotes** (`"`)—to be displayed in the team directory and on the top header of your profile page, e.g., `"Hubble, Edwin P."`; you can include a middle initial.
- `excerpt:` Your institution (wrapped in double quotes) as one of the existing `<h2>` headers at the top of each HTML block listed in [./_pages/team.html](https://github.com/pfitsplus/pfitsplus.github.io/blob/main/_pages/team.html) (e.g., `"Iowa State University"`)
- `position:` Your official title or position (wrapped in double quotes), e.g., `"Graduate Assistant"`.
- `header:`
  - `teaser:` The path to your profile image (`.jpg` or `.png`) in [`/assets/images/team/`](https://github.com/pfitsplus/pfitsplus.github.io/tree/dev/assets/images/team) to appear on the [main directory](https://pfitsplus.github.io/team/); please crop your photo to have *square* dimensions (i.e., 1:1 aspect ratio) and match its filename to that of your Markdown file (e.g., `lastname-firstname.jpg`).
- `sidebar:`
  - `title: "Position"` Leave as is.
    - `image:` The same path to your profile image to appear on your profile sidebar; see `header:`, `teaser:` above for the standard path and image format.
    - `text:` Your official title or position, as used in `position:` above, followed by any optional personal links; use the sample HTML link and icon tags in the example above, making sure to wrap your hypertext reference (`href=`) in *single* quotes (`'`); you must include a `"` (double quote) after the final item; see [example above](#Front-Matter).
    See also [this table](https://www.w3schools.com/icons/fontawesome_icons_webapp.asp) for a sample list of Font Awesome (FA) icons to use in `<i class='fas fa-fw ...'></i>`.
  - `title: "Research Interests"` (Optional) To be included on your profile sidebar.
    - `text: "<ul>` (HTML for _**u**nnumbered **l**ist_) (Optional) List each item on a separate line prepended with `<li> ` (HTML for _**l**ist **i**tem_, ensuring a single empty space before your text); best to keep to a maximum of 2-3 words and must include a double quote (`"`) after the final item; see [example above](#Front-Matter).


## Main Content (Markdown)
Jekyll will render your post from any [**Markdown**](https://www.markdownguide.org/) you supply below the [front matter](#Front-Matter) section.
Specifically, our site supports [GitHub Flavored Markdown (GFM)](https://github.github.com/gfm/) input, which includes some extensions beyond the standard Markdown specification, notably [_fenced code blocks_](https://github.github.com/gfm/#fenced-code-blocks).

- For a GFM reference and more information on Markdown formatting and features, see [Writing on GitHub](https://docs.github.com/en/github/writing-on-github).
- For additional post ideas and examples, see this extensive list of *rendered* [Sample Posts](https://mmistakes.github.io/minimal-mistakes/year-archive/) and their corresponding [raw Markdown files](https://github.com/mmistakes/minimal-mistakes/tree/gh-pages-3.1.6/_posts).
- See also [GitHub Learning Lab's](https://lab.github.com/), 10 step, 45 min course on [Communicating using Markdown](https://lab.github.com/githubtraining/communicating-using-markdown).
