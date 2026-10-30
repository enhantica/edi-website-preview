#!/usr/bin/env python3
"""Render the shared workflow using the same bundled icons as navigation."""

from __future__ import annotations

import html
import re
from importlib.metadata import distribution
from pathlib import Path

import yaml
from defusedxml import ElementTree
from render_experiments import replace

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'surfaces/docs'


def render() -> None:
    config = yaml.load((ROOT / 'surfaces/mkdocs.yml').read_text(), Loader=yaml.BaseLoader)
    stages = config['extra']['workflow_icons']
    package = distribution('zensical')
    diagram = [
        '<div class="ed-workflow-diagram">',
        '<svg viewBox="0 0 760 92" role="img" aria-labelledby="workflow-title" xmlns="http://www.w3.org/2000/svg">',
        '<title id="workflow-title">Project, Structure, Experiment, Analysis, Report. Revisit earlier stages when assessing the fit.</title>',
        '<defs><marker id="workflow-arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 6 3 0 6" fill="#0084c7"/></marker></defs>',
    ]
    for index, (title, name) in enumerate(stages.items()):
        relative = 'zensical/templates/.icons/material/' + name + '.svg'
        source = Path(package.locate_file(relative))
        root = ElementTree.fromstring(source.read_bytes())
        paths = ''.join(
            '<path d="' + html.escape(path.attrib['d'], quote=True) + '"/>'
            for path in root
            if path.tag.endswith('path')
        )
        if not paths:
            raise ValueError('Workflow icon has no vector paths: ' + name)
        x = 4 + index * 152
        diagram += [
            f'<a href="{title.lower()}/" aria-label="{title}">',
            f'<rect x="{x}" y="12" width="136" height="68" rx="5" fill="#0084c7" fill-opacity=".07" stroke="#0084c7"/>',
            f'<svg x="{x + 58}" y="21" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{paths}</svg>',
            f'<text x="{x + 68}" y="65" fill="currentColor" text-anchor="middle" font-size="16">{title}</text></a>',
        ]
        if index < len(stages) - 1:
            diagram.append(
                f'<path d="M{x + 137} 46h13" stroke="#0084c7" marker-end="url(#workflow-arrow)"/>'
            )
    diagram += ['</svg>', '</div>']
    path = DOCS / 'user-guide/analysis-workflow/index.md'
    text = path.read_text()
    if '<!-- workflow-diagram -->' not in text:
        text = re.sub(
            r'<svg viewBox="0 0 760 .*?</svg>',
            '<!-- workflow-diagram -->\n<!-- /workflow-diagram -->',
            text,
            count=1,
            flags=re.DOTALL,
        )
        path.write_text(text)
    replace(path, 'workflow-diagram', '\n'.join(diagram))
    # Stage links use the same identifiers in the diagram, overview table and guides.
    for path in (DOCS / 'user-guide').rglob('*.md'):
        text = path.read_text()
        for title, name in stages.items():
            text = re.sub(
                r'\['
                + title
                + r'\]\(([^)]+/'
                + title.lower()
                + r'\.md|'
                + title.lower()
                + r'\.md)\)',
                r'[:material-' + name + ': ' + title + r'](\1)',
                text,
            )
        path.write_text(text)


if __name__ == '__main__':
    render()
