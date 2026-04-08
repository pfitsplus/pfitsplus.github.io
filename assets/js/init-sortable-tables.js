document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("table.js-sort-table").forEach(function (table) {
    new Tablesort(table);
  });
});
