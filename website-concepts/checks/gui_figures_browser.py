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
  return {width: bounds.width, height: bounds.height, column: width, view:svg.dataset.guiView,
    caption: !!figure.querySelector('figcaption'),
    overflow: getComputedStyle(svg).overflow, radius: getComputedStyle(svg).borderRadius,
    imageClip: svg.querySelector('image').hasAttribute('clip-path'),
    regions, active: svg.querySelectorAll('[data-gui-region].is-active').length};
});
return {figures, overflow: document.documentElement.scrollWidth > innerWidth,
  oldCaption: article.textContent.includes('Open full-size screenshot'),
  oldControls:article.querySelectorAll('[data-gui-target], [data-gui-overview]').length};
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


def check_viewers(browser: Browser, width: int, output: Path) -> None:
    require(browser.execute("return document.querySelectorAll('.tabbed-set').length === 6;"))
    groups = browser.execute(
        "return [...document.querySelectorAll('.tabbed-set')].map(group=>group.querySelectorAll('.tabbed-labels label').length);"
    )
    require(groups == [5, 5, 5, 5, 7, 4], groups)
    inventory = browser.execute(r"""
return [...document.querySelectorAll('.tabbed-set')].map(group =>
  [...group.querySelectorAll('.tabbed-labels label')].map(label => ({
    title: label.textContent.trim().replace(/\s+/g, ' '),
    icons: label.querySelectorAll('svg').length
  })));
""")
    require(
        [item['title'] for item in inventory[4]]
        == [
            'Overview',
            'Main view: Pattern',
            'Main view: Correlations',
            'Sidebar: Main',
            'Sidebar: Extra',
            'Sidebar: Text',
            'Sidebar: Settings',
        ],
        inventory,
    )
    require(
        all(
            item['icons'] == (0 if item['title'] == 'Overview' else 1)
            for group in inventory[1:]
            for item in group
        ),
        inventory,
    )
    require(browser.execute("return document.querySelector('h3#home') !== null;"))
    for group, modes in enumerate(groups):
        image_positions, descriptions = [], []
        for mode in range(modes):
            browser.execute(
                "document.querySelectorAll('.tabbed-set')[arg[0]].querySelectorAll('.tabbed-labels label')[arg[1]].click();",
                [group, mode],
            )
            browser.wait(0.05)
            visible = browser.execute(
                "return [...document.querySelectorAll('.tabbed-set')[arg].querySelectorAll('svg.gui-capture')].filter(svg=>svg.getBoundingClientRect().width>0).length;",
                group,
            )
            require(visible == 1, (group, mode, visible))
            selected = browser.execute(
                """
const group=document.querySelectorAll('.tabbed-set')[arg[0]];
const label=group.querySelectorAll('.tabbed-labels label')[arg[1]];
const svg=[...group.querySelectorAll('svg.gui-capture')].find(svg=>svg.getBoundingClientRect().width>0);
return {label:label.textContent.trim(), title:svg.querySelector('title').textContent,
  text:svg.closest('figure').querySelector('.gui-view-description').textContent,
  offset:svg.getBoundingClientRect().top-group.getBoundingClientRect().top,
  image:svg.querySelector('image').getAttribute('href')};
""",
                [group, mode],
            )
            image_positions.append(selected['offset'])
            descriptions.append(selected['text'])
            require(bool(selected['text']), selected)
            if mode == 0 and group:
                require(selected['title'].endswith(' overview'), selected)
            elif mode:
                require(selected['title'].endswith(selected['label']), selected)
            if group == 4 and mode == 2:
                require('guide-analysis-correlations.png' in selected['image'], selected)
                browser.shot(output / f'{browser.kind}-{width}-correlations.png')
        require(max(image_positions) - min(image_positions) < 1, (group, image_positions))
        require(len(set(descriptions)) == modes, (group, descriptions))
        browser.execute(
            "document.querySelectorAll('.tabbed-set')[arg].querySelector('.tabbed-labels label').click();",
            group,
        )


def exercise(browser: Browser, base: str, output: Path) -> list[dict]:
    results = []
    for width in (1440, 390):
        browser.viewport(width, 1000)
        for route, count in [
            ('application/workspace/', 32),
            ('application/first-refinement/', 21),
            ('application/examples/', 1),
        ]:
            browser.goto(base + route)
            result = browser.execute(FIGURES)
            require(not result['overflow'] and not result['oldCaption'], result)
            require(not result['oldControls'], result)
            require(len(result['figures']) == count, result)
            for figure in result['figures']:
                if not figure['width']:
                    continue
                require(not figure['caption'], figure)
                require(abs(figure['width'] - figure['column']) < 1, figure)
                require(abs(figure['width'] / figure['height'] - 1480 / 800) < 0.01, figure)
                require(figure['overflow'] == 'visible' and figure['radius'] == '0px', figure)
                require(figure['imageClip'] and figure['active'] in {1, 4}, figure)
                for region in figure['regions']:
                    require(abs(region['paddingX'] - 1.5) < 0.05, region)
                    require(abs(region['paddingY'] - 1.5) < 0.05, region)
                    require(region['square'], region)
            if route.endswith('workspace/'):
                require(
                    all(
                        f['regions'][0]['parts'] == 2
                        for f in result['figures']
                        if f['view'] in {'workflow', 'main', 'sidebar'}
                    ),
                    result,
                )
            if route.endswith('workspace/'):
                check_viewers(browser, width, output)
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
            browser.until(
                "!document.querySelector('.gui-lightbox').open && !document.documentElement.classList.contains('gui-lightbox-open') && document.activeElement.matches('article [data-gui-open]')"
            )
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
                require(len(result['figures']) >= expected, (filename, result))
                require(not result['oldControls'], (filename, result))
                require(
                    browser.execute(
                        "const ids=[...document.querySelectorAll('[id]')].map(e=>e.id);return ids.length === new Set(ids).size;"
                    ),
                    filename,
                )
                require(
                    all(
                        abs(f['width'] - f['column']) < 1 for f in result['figures'] if f['width']
                    ),
                    filename,
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
