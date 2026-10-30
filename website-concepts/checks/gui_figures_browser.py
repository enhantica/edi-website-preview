#!/usr/bin/env python3
"""Check GUI figure sizing, unclipped compound outlines and the image dialog."""

from __future__ import annotations

import argparse
import functools
import http.server
import json
import threading
from pathlib import Path

from network_browser import ROOT, Browser, QuietHandler, require

FIGURES = r"""
const article = document.querySelector('article');
const width = article.getBoundingClientRect().width;
const figures = [...article.querySelectorAll('.gui-figure')].map(figure => {
  const svg = figure.querySelector('svg.gui-capture');
  const bounds = svg.getBoundingClientRect();
  const scale = bounds.width / 1480;
  const regions = [...svg.querySelectorAll('[data-gui-region]')].map(region => {
    const parts = JSON.parse(region.dataset.guiParts), box = region.getBBox();
    const left = Math.min(...parts.map(p => p[0]));
    const top = Math.min(...parts.map(p => p[1]));
    return {parts: parts.length, paddingX: (left-box.x)*scale,
      paddingY: (top-box.y)*scale, square: getComputedStyle(region).strokeLinejoin === 'miter'};
  });
  return {width: bounds.width, height: bounds.height, column: width,
    overflow: getComputedStyle(svg).overflow, radius: getComputedStyle(svg).borderRadius,
    imageClip: svg.querySelector('image').hasAttribute('clip-path'),
    regions, active: svg.querySelectorAll('[data-gui-region].is-active').length};
});
return {figures, overflow: document.documentElement.scrollWidth > innerWidth,
  oldCaption: article.textContent.includes('Open full-size screenshot')};
"""


def press(browser: Browser, selector: str, key: str) -> None:
    if browser.kind == 'safari':
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys

        browser.driver.find_element(By.CSS_SELECTOR, selector).send_keys(getattr(Keys, key))
    else:
        browser.page.locator(selector).first.press(
            {'ENTER': 'Enter', 'ESCAPE': 'Escape', 'TAB': 'Tab'}[key]
        )


def exercise(browser: Browser, base: str, output: Path) -> list[dict]:
    results = []
    for width in (1440, 390):
        browser.viewport(width, 1000)
        for route, count in [
            ('application/workspace/', 16),
            ('application/first-refinement/', 10),
            ('application/examples/', 1),
        ]:
            browser.goto(base + route)
            result = browser.execute(FIGURES)
            require(not result['overflow'] and not result['oldCaption'], result)
            require(len(result['figures']) == count, result)
            for figure in result['figures']:
                require(abs(figure['width'] - figure['column']) < 1, figure)
                require(abs(figure['width'] / figure['height'] - 1480 / 800) < 0.01, figure)
                require(figure['overflow'] == 'visible' and figure['radius'] == '0px', figure)
                require(figure['imageClip'] and figure['active'] in {1, 4}, figure)
                for region in figure['regions']:
                    require(abs(region['paddingX'] - 1.5) < 0.05, region)
                    require(abs(region['paddingY'] - 1.5) < 0.05, region)
                    require(region['square'], region)
            if route.endswith('workspace/'):
                require(all(f['regions'][0]['parts'] == 2 for f in result['figures'][1:]), result)
            opener = 'article [data-gui-open]'
            browser.execute('document.querySelector(arg).focus();', opener)
            press(browser, opener, 'ENTER')
            browser.until("document.querySelector('.gui-lightbox')?.open")
            modal = browser.execute("""
const dialog = document.querySelector('.gui-lightbox'), svg=dialog.querySelector('.gui-capture');
const rect=svg.getBoundingClientRect(), stage=dialog.querySelector('.gui-lightbox-stage').getBoundingClientRect();
return {dialogWidth: dialog.getBoundingClientRect().width, viewport: innerWidth,
  fits: rect.width <= stage.width && rect.height <= stage.height,
  shape: svg.querySelector('[data-gui-region]').getAttribute('d'),
  sourceShape: document.querySelector('article [data-gui-region]').getAttribute('d'),
  focus: document.activeElement.matches('.gui-lightbox-close'),
  scroll: getComputedStyle(document.documentElement).overflow,
  clip: svg.querySelector('image').getAttribute('clip-path')};
""")
            require(abs(modal['dialogWidth'] - modal['viewport']) < 1, modal)
            require(modal['fits'] and modal['focus'] and modal['scroll'] == 'hidden', modal)
            require('-lightbox' in modal['clip'], modal)
            press(browser, '.gui-lightbox-close', 'TAB')
            require(
                browser.execute(
                    "return document.querySelector('.gui-lightbox').contains(document.activeElement);"
                )
            )
            browser.shot(output / f'{browser.kind}-{width}-dialog.png')
            press(browser, '.gui-lightbox-close', 'ESCAPE')
            browser.until("!document.querySelector('.gui-lightbox').open")
            require(
                browser.execute(
                    "return document.activeElement.matches('article [data-gui-open]');"
                )
            )
            require(
                browser.execute(
                    "return !document.documentElement.classList.contains('gui-lightbox-open');"
                )
            )
            results.append({'width': width, 'route': route, 'figures': count, 'dialog': 'PASS'})
        if width == 1440:
            registry = json.loads((ROOT / 'gui-guide-scenes.json').read_text())
            for filename, sections in registry.items():
                browser.goto(base + filename.replace('.md', '/'))
                expected = sum(
                    len(value) if isinstance(value, list) else 1 for value in sections.values()
                )
                result = browser.execute(FIGURES)
                require(len(result['figures']) == expected, (filename, result))
                require(
                    browser.execute(
                        "const ids=[...document.querySelectorAll('[id]')].map(e=>e.id);return ids.length === new Set(ids).size;"
                    ),
                    filename,
                )
                require(
                    all(abs(f['width'] - f['column']) < 1 for f in result['figures']), filename
                )
        browser.goto(base + 'application/y2o3-walkthrough/')
        require(
            browser.execute(
                "return location.pathname.endsWith('/application/first-refinement/') && document.querySelector('h1').id === 'example-refinement';"
            )
        )
        browser.goto(base + 'application/screen-reference/')
        require(
            browser.execute(
                "return location.pathname.endsWith('/application/workspace/') && document.querySelector('h1').id === 'application-layout';"
            )
        )
        links = browser.execute("""
return [...document.querySelectorAll('.md-sidebar--primary a')].map(a=>a.textContent.trim());
""")
        require(links.index('Application layout') < links.index('Example refinement'), links)
        require(
            'Page and sidebar reference' not in links and 'Y₂O₃ walkthrough' not in links, links
        )
    require(not browser.errors, browser.errors)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--browser', choices=['chromium', 'safari'], default='chromium')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    server = http.server.ThreadingHTTPServer(
        ('127.0.0.1', 0), functools.partial(QuietHandler, directory=str(ROOT / '_build'))
    )
    threading.Thread(target=server.serve_forever, daemon=True).start()
    browser = Browser(args.browser)
    try:
        checks = exercise(browser, f'http://127.0.0.1:{server.server_port}/', args.output)
        report = {
            'status': 'PASS',
            'browser': browser.kind,
            'version': browser.version,
            'checks': checks,
        }
        (args.output / f'gui-{args.browser}.json').write_text(json.dumps(report, indent=2) + '\n')
        print(json.dumps(report), flush=True)
    finally:
        browser.close()
        server.shutdown()


if __name__ == '__main__':
    main()
