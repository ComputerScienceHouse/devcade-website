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

function setTimeframe(timeframe) {
  selection = document.getElementsByClassName(`${timeframe}`)[0];
  let others = selection.parentElement.children;
  for(let i = 0; i < others.length; i++){
    others[i].classList.add("hidden");
  }
  selection.classList.remove('hidden');

  try {
    selection = document.getElementById(timeframe);
    others = selection.parentElement.children;
    for(let i = 0; i < others.length; i++){
      others[i].classList.remove('opaque');
    }
    selection.classList.add('opaque');
    document.getElementById('yearBox').textContent = timeframe;
  }
  catch {}
}

dropdown_init();
