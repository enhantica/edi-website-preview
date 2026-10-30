#!/usr/bin/env python3
"""Render captured outputs and the shared initial/refined comparison without copied results."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from render_experiments import replace
from render_interfaces import preview

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'surfaces/docs'


def render() -> None:
    folder = DOCS / 'assets/learning'
    if not (folder / 'capture.json').exists():
        return
    metadata = json.loads((folder / 'capture.json').read_text())
    example = json.loads((DOCS / 'assets/gui/y2o3/manifest.json').read_text())['example']
    if metadata['example'] != example:
        raise ValueError('Learning comparison must use the selected GUI example')
    for filename, digest in metadata['assets_sha256'].items():
        if hashlib.sha256((folder / filename).read_bytes()).hexdigest() != digest:
            raise ValueError('Learning figure differs from its captured source')
    panes = ['<div class="gui-viewer" markdown="1">', '']
    for title, filename, description in [
        (
            'Starting model',
            'initial.svg',
            'Compare the starting calculation with the measured pattern. The residual shows their difference.',
        ),
        (
            'Refined model',
            'refined.svg',
            'After refinement, compare the same peaks and residual on exactly the same axes and scale.',
        ),
    ]:
        panes += [
            '=== "' + title + '"',
            '',
            '    <p class="gui-view-description">' + description + '</p>',
            '',
        ]
        panes += ['    ' + line for line in preview('learning/' + filename, title).splitlines()]
        panes += ['']
    panes += ['</div>', '']
    comparison = '\n'.join(panes)
    result = metadata['result']
    output = (
        f'Rwp: {100 * result["rwp"]:.2f}%   ·   Reduced χ²: {result["reduced_chi_square"]:.2f}'
    )
    for filename in ['application/first-refinement.md', 'python/examples.md']:
        replace(DOCS / filename, 'learning-comparison', comparison)
    path = DOCS / 'python/examples.md'
    text = path.read_text()
    start = text.index('For the supplied starting project:')
    end = text.index('\nThe notebook plots', start)
    text = (
        text[:start]
        + 'For the supplied starting project:\n\n```text\n'
        + output
        + '\n```\n'
        + text[end:]
    )
    path.write_text(text)
    path = DOCS / 'cli/examples.md'
    text = path.read_text()
    start = text.index('The supplied example converges')
    end = text.index('\n`--dry`', start)
    transcript = (folder / 'command-line.txt').read_text().strip()
    # The CLI includes the isolated source path in its first line; show the selected project name.
    lines = [line.rstrip() for line in transcript.splitlines()]
    if lines and lines[0].startswith('edi fit: project '):
        lines[0] = 'edi fit: project ' + example + ',' + lines[0].split(',', 1)[1]
    text = (
        text[:start]
        + 'The supplied example converges with the following output:\n\n```text\n'
        + '\n'.join(lines)
        + '\n```\n'
        + text[end:]
    )
    path.write_text(text)


if __name__ == '__main__':
    render()
