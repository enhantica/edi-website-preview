#!/usr/bin/env python3
"""Render shared interface previews and release download controls."""

from __future__ import annotations

import hashlib
import html
import json
import re
import struct
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'surfaces/docs'


def preview(filename: str, description: str, crop_top: int = 0) -> str:
    source = DOCS / 'assets' / filename
    data = source.read_bytes()
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError(f'Interface preview must be PNG: {filename}')
    width, height = struct.unpack('!II', data[16:24])
    if not 0 <= crop_top < height:
        raise ValueError(f'Invalid preview crop: {filename}')
    shown_height = height - crop_top
    image = html.escape('../assets/' + filename + '?v=' + hashlib.sha256(data).hexdigest()[:12])
    title = html.escape(description, quote=True)
    clip = 'interface-' + source.stem
    frame = f'y="{crop_top}" width="{width}" height="{shown_height}" rx="12"'
    return (
        '<figure class="ed-interface-preview" data-interface-hero>\n'
        f'<a class="gui-image-link" href="{image}" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: {title}">'
        f'<svg class="gui-capture" viewBox="0 {crop_top} {width} {shown_height}" width="{width}" height="{shown_height}" role="img" aria-label="{title}">'
        f'<title>{title}</title><defs><clipPath id="{clip}"><rect {frame} /></clipPath></defs>'
        f'<image href="{image}" width="{width}" height="{height}" clip-path="url(#{clip})" />'
        f'<rect class="gui-image-frame" {frame} />'
        '</svg></a>\n</figure>'
    )


def replace_marker(source: Path, kind: str, key: str, content: str) -> None:
    start, end = f'<!-- {kind}:{key} -->', f'<!-- /{kind} -->'
    text, count = re.subn(
        re.escape(start) + '.*?' + re.escape(end),
        lambda _: start + '\n' + content + '\n' + end,
        source.read_text(),
        flags=re.DOTALL,
    )
    if count != 1:
        raise ValueError(f'Expected one {kind} marker in {source}')
    source.write_text(text)


def render() -> None:
    capture = DOCS / 'assets/interfaces/capture.json'
    if capture.exists():
        metadata = json.loads(capture.read_text())
        example = metadata['example']
        fixture = json.loads((DOCS / 'assets/gui/y2o3/manifest.json').read_text())['example']
        if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', example) or example != fixture:
            raise ValueError('Interface screenshots must use the selected GUI example')
        replace_marker(
            DOCS / 'python/examples.md',
            'example',
            'python',
            "```python\nimport edi\n\nproject = edi.Project.load('" + example + "')\n```",
        )
        command = 'fit ' + example + ' --dry'
        replace_marker(
            DOCS / 'cli/examples.md',
            'example',
            'cli',
            '=== "Standalone"\n\n    ```console\n    edi ' + command + '\n    ```\n\n'
            '=== "Python package"\n\n    ```console\n    python -m edi ' + command + '\n    ```',
        )
    for name, image, title, crop in [
        ('application', 'edi-analysis-hero.png', 'EasyDiffraction graphical application', 62),
        ('python', 'interfaces/python-notebook.png', 'EasyDiffraction in a Jupyter notebook', 0),
        ('cli', 'interfaces/command-line.png', 'EasyDiffraction command-line session', 0),
    ]:
        source = DOCS / name / 'index.md'
        if f'<!-- interface-preview:{name} -->' in source.read_text():
            replace_marker(source, 'interface-preview', name, preview(image, title, crop))
    releases = json.loads((ROOT / 'distributions.json').read_text())
    for family, filename in [
        ('desktop', 'application/desktop.md'),
        ('command-line', 'cli/standalone.md'),
    ]:
        source = DOCS / filename
        if not source.exists():
            continue
        buttons = []
        for entry in releases[family]:
            label = html.escape(entry['platform'], quote=True)
            url = entry['url']
            if url is None:
                buttons.append(
                    f'<button class="md-button" type="button" disabled aria-label="{label} download not available yet">{label}</button>'
                )
            else:
                parsed = urlsplit(url)
                if parsed.scheme != 'https' or not parsed.netloc:
                    raise ValueError(f'Invalid {family} download URL: {url}')
                buttons.append(
                    f'<a class="md-button" href="{html.escape(url, quote=True)}" aria-label="Download for {label}">{label}</a>'
                )
        replace_marker(
            source,
            'distribution',
            family,
            '<div class="ed-downloads">' + '\n'.join(buttons) + '</div>',
        )


if __name__ == '__main__':
    render()
