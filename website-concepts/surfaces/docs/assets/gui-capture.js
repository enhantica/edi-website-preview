(() => {
  if (window.ediGuiCaptureInstalled) return;
  window.ediGuiCaptureInstalled = true;
  document.addEventListener("click", event => {
    const button = event.target.closest("[data-gui-target]");
    if (!button) return;
    const figure = button.closest("[data-gui-figure]");
    const active = button.getAttribute("aria-pressed") !== "true";
    figure.querySelectorAll("[data-gui-target]").forEach(item => {
      item.setAttribute("aria-pressed", String(active && item === button));
    });
    figure.querySelectorAll("[data-gui-region]").forEach(region => {
      region.classList.toggle("is-active", active && region.dataset.guiRegion === button.dataset.guiTarget);
    });
  });
})();
