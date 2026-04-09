document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("table.js-sort-table").forEach(function (table) {
    new Tablesort(table);
  });
});

(function () {
  function addSortIcons(table) {
    const headers = table.querySelectorAll("thead th");

    headers.forEach((th) => {
      if (th.dataset.sortable === "false") return;

      if (!th.querySelector(".sort-icon")) {
        th.insertAdjacentHTML(
          "beforeend",
          ' <span class="sort-icon"><i class="fas fa-sort" aria-hidden="true"></i></span>'
        );
      }

      if (!th.hasAttribute("aria-sort")) {
        th.setAttribute("aria-sort", "none");
      }
    });
  }

  function resetIcons(table) {
    table.querySelectorAll("thead th .sort-icon i").forEach((icon) => {
      icon.classList.remove("fa-sort-up", "fa-sort-down");
      icon.classList.add("fa-sort");
    });

    table.querySelectorAll("thead th").forEach((th) => {
      if (th.dataset.sortable === "false") return;
      th.setAttribute("aria-sort", "none");
      th.dataset.sortDir = "";
    });
  }

  function setIcon(th, dir) {
    const icon = th.querySelector(".sort-icon i");
    if (!icon) return;

    icon.classList.remove("fa-sort", "fa-sort-up", "fa-sort-down");

    if (dir === "asc") {
      icon.classList.add("fa-sort-up");
      th.setAttribute("aria-sort", "ascending");
    } else if (dir === "desc") {
      icon.classList.add("fa-sort-down");
      th.setAttribute("aria-sort", "descending");
    } else {
      icon.classList.add("fa-sort");
      th.setAttribute("aria-sort", "none");
    }
  }

  document.querySelectorAll("table").forEach((table) => {
    addSortIcons(table);

    const headers = table.querySelectorAll("thead th");

    headers.forEach((th) => {
      if (th.dataset.sortable === "false") return;

      th.addEventListener("click", function () {
        const nextDir = th.dataset.sortDir === "asc" ? "desc" : "asc";

        resetIcons(table);

        th.dataset.sortDir = nextDir;
        setIcon(th, nextDir);
      });
    });

    // If your sortable library emits this event, prefer it over click-only syncing.
    table.addEventListener("Sortable.sorted", function () {
      // Optional: if your library adds classes/attributes to the active <th>,
      // read them here and call setIcon(...) accordingly.
    });
  });
})();
