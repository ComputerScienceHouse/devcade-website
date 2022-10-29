function toggleDropdown(e) {
  e.classList.toggle("hidden");
}

function dropdown_init() {
  dropdowns = document.querySelectorAll(".dropdown-toggle");
  drops = document.querySelectorAll(".dropped");
  for (let i = 0; i < dropdowns.length; i++) {
    dropdowns[i].onclick = function () {
      toggleDropdown(drops[i]);
    };
  }
}

dropdown_init();
