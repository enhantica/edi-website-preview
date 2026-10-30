(() => {
  if (window.ediGuiCaptureInstalled) return;
  window.ediGuiCaptureInstalled = true;
  let dialog, opener;
  const geometry = svg => {
    const scale = svg.getBoundingClientRect().width / svg.viewBox.baseVal.width;
    if (!scale) return;
    const padding = 1.5 / scale;
    svg.querySelectorAll('[data-gui-region]').forEach(region => {
      const parts = JSON.parse(region.dataset.guiParts);
      const [x, y, width, height] = parts[0];
      const left = x - padding, top = y - padding;
      const right = x + width + padding, bottom = y + height + padding;
      const points = [[left, top]];
      if (parts.length === 2) {
        const [tx, ty, tw] = parts[1];
        points.push([tx - padding, top], [tx - padding, ty - padding],
          [tx + tw + padding, ty - padding], [tx + tw + padding, top]);
      }
      points.push([right, top], [right, bottom], [left, bottom]);
      region.setAttribute('d', 'M' + points.map(point => point.join(' ')).join(' L') + ' Z');
    });
  };
  const observer = new ResizeObserver(entries => entries.forEach(entry => geometry(entry.target)));
  const close = () => dialog?.close();
  const show = link => {
    if (!dialog) {
      dialog = document.createElement('dialog');
      dialog.className = 'gui-lightbox';
      dialog.setAttribute('aria-labelledby', 'gui-lightbox-title');
      dialog.innerHTML = '<header class="gui-lightbox-header"><h2 id="gui-lightbox-title"></h2>' +
        '<button class="gui-lightbox-close" type="button" aria-label="Close enlarged screenshot" autofocus>' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button></header>' +
        '<div class="gui-lightbox-stage"></div>';
      document.body.append(dialog);
      dialog.querySelector('button').addEventListener('click', close);
      dialog.addEventListener('keydown', event => {
        if (event.key === 'Tab') {
          event.preventDefault();
          dialog.querySelector('button').focus();
        }
      });
      dialog.addEventListener('click', event => {
        if (event.target === dialog || event.target.classList.contains('gui-lightbox-stage')) close();
      });
      dialog.addEventListener('close', () => {
        document.documentElement.classList.remove('gui-lightbox-open');
        const svg = dialog.querySelector('.gui-capture');
        if (svg) observer.unobserve(svg);
        dialog.querySelector('.gui-lightbox-stage').replaceChildren();
        if (opener?.isConnected) opener.focus({preventScroll: true});
      });
    }
    opener = link;
    const svg = link.querySelector('.gui-capture').cloneNode(true);
    const clip = svg.querySelector('clipPath');
    const id = clip.id + '-lightbox';
    clip.id = id;
    svg.querySelector('image').setAttribute('clip-path', `url(#${id})`);
    dialog.querySelector('h2').textContent = svg.querySelector('title').textContent;
    dialog.querySelector('.gui-lightbox-stage').replaceChildren(svg);
    dialog.showModal();
    document.documentElement.classList.add('gui-lightbox-open');
    observer.observe(svg);
    geometry(svg);
  };
  document.addEventListener('click', event => {
    const link = event.target.closest('[data-gui-open]');
    if (link) {
      if (event.button || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      show(link);
      return;
    }
    const button = event.target.closest('[data-gui-target]');
    if (!button) return;
    const figure = button.closest('[data-gui-figure]');
    const active = button.getAttribute('aria-pressed') !== 'true';
    figure.querySelectorAll('[data-gui-target]').forEach(item => {
      item.setAttribute('aria-pressed', String(active && item === button));
    });
    figure.querySelectorAll('[data-gui-region]').forEach(region => {
      region.classList.toggle('is-active', active && region.dataset.guiRegion === button.dataset.guiTarget);
    });
  });
  const initialize = () => {
    close();
    observer.disconnect();
    document.querySelectorAll('svg.gui-capture').forEach(svg => {
      observer.observe(svg);
      geometry(svg);
    });
  };
  if (typeof document$ !== 'undefined') document$.subscribe(initialize);
  else initialize();
})();
