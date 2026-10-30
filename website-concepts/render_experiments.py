#!/usr/bin/env python3
"""Render experiment tags and a searchable catalogue from native app metadata."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
from itertools import starmap
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'surfaces/docs'
ASSETS = DOCS / 'assets/reference'


def badge(family: str, token: str, *, prefix: str = '../') -> str:
    definitions = json.loads((ASSETS / 'experiment-tags.json').read_text())
    item = definitions['tags'][family][token]
    return (
        f'<a class="ed-tag ed-tag--{item["tone"]}" href="{prefix}user-guide/experiment-types/#{item["anchor"]}" '
        f'title="{html.escape(item["meaning"], quote=True)}">{html.escape(item["label"])}</a>'
    )


def replace(path: Path, key: str, content: str) -> None:
    start, end = '<!-- ' + key + ' -->', '<!-- /' + key + ' -->'
    text = path.read_text()
    if start not in text:
        text += '\n\n' + start + '\n' + end + '\n'
    text, count = re.subn(
        re.escape(start) + '.*?' + re.escape(end),
        lambda _: start + '\n' + content + '\n' + end,
        text,
        flags=re.DOTALL,
    )
    if count != 1:
        raise ValueError(f'Duplicate marker {key}: {path}')
    path.write_text(text)


def render() -> None:
    if not (ASSETS / 'experiment-tags.json').exists():
        return
    registry = json.loads((ASSETS / 'experiment-tags.json').read_text())
    metadata = json.loads((ASSETS / 'examples.json').read_text())['examples']
    css = [
        '/* Generated from the app experiment tag registry. */',
        '.ed-tag {display:inline-flex;align-items:center;white-space:nowrap;border-radius:3px;padding:.08em .38em;margin:.12em .16em .12em 0;font-size:.82em;line-height:1.5;text-decoration:none!important}',
        '.ed-tag:hover,.ed-tag:focus-visible {text-decoration:underline!important;outline-offset:2px}',
        '.ed-example-filters {display:flex;flex-wrap:wrap;gap:.5rem;margin-block:.7rem}',
        '.ed-example-filters input,.ed-example-filters select {font:inherit;max-width:100%;padding:.4em .6em;border:1px solid var(--md-default-fg-color--lightest);border-radius:5px;background:var(--md-default-bg-color);color:var(--md-default-fg-color)}',
        '.ed-example-name {display:block}',
        '.ed-example-tags {display:block;margin-top:.25em}',
        '[data-example-row][hidden] {display:none}',
    ]
    for tone, colors in registry['tones'].items():
        for scheme, key in [('default', 'light'), ('slate', 'dark')]:
            color = colors[key]
            if not re.fullmatch(r'#[0-9a-fA-F]{6}', color):
                raise ValueError('Invalid tag colour')
            css.append(
                f'[data-md-color-scheme="{scheme}"] .ed-tag--{tone} {{color:{color};background:{color}21}}'
            )
    (DOCS / 'assets/experiment-tags.css').write_text('\n'.join(css) + '\n')
    prose = {
        'purpose': (
            'Purpose',
            'Simulation calculates a pattern. Fitting compares a model with measured observations.',
        ),
        'fittingMode': (
            'Fitting mode',
            'Choose how experiments contribute to a fit. This is separate from their measurement type.',
        ),
        'sampleForm': (
            'Sample form',
            'Powder profiles contain overlapping reflections; single-crystal data identify individual reflections.',
        ),
        'probe': (
            'Probe',
            'Neutrons and X-rays interact with the sample differently. Select the probe used for the measurement.',
        ),
        'beamMode': (
            'Beam mode',
            'Constant-wavelength powder data use scattering angle; time-of-flight data use arrival time and an instrument calibration.',
        ),
        'scatteringType': (
            'Scattering type',
            'Bragg diffraction describes the crystalline contribution from lattice reflections.',
        ),
    }
    meanings = {
        'single-fit': 'Refine one experiment.',
        'joint-fit': 'Refine several experiments together with shared model quantities.',
        'sequential-fit': 'Fit a scan in order, using the preceding result as the next starting point.',
        'independent-fit': 'Fit each dataset from the same starting model.',
        'powder-diffraction': 'Diffraction from many crystallite orientations, usually measured as an intensity profile.',
        'single-crystal-diffraction': 'Diffraction from an oriented crystal, measured as individual reflection intensities.',
        'neutron-diffraction': 'Diffraction using neutrons; nuclear scattering and, where modelled, magnetic scattering contribute.',
        'x-ray-diffraction': 'Diffraction using X-rays; the scattering model depends on the electron distribution.',
        'constant-wavelength': 'A specified incident wavelength; powder patterns are commonly expressed against 2θ.',
        'time-of-flight': 'Neutron wavelengths are separated by arrival time. Calibration relates flight time to diffraction geometry.',
    }
    lines = [
        '# Experiment types and labels',
        '',
        'Use these labels to recognise the same measurement in the app, example catalogue and guides. Colour helps scanning; the text identifies the meaning.',
        '',
        'An experiment has several independent attributes. For example, the first refinement is '
        + ' '.join(
            starmap(
                badge,
                [
                    ('sampleForm', 'powder'),
                    ('probe', 'neutron'),
                    ('beamMode', 'constant wavelength'),
                ],
            )
        )
        + '.',
        '',
        'Choose the measurement type before loading data. The app enables combinations it currently supports; a listed attribute does not imply every combination is available. [See the experiment controls](../application/experiments.md).',
        '',
    ]
    seen = set()
    for family, values in registry['tags'].items():
        title, explanation = prose[family]
        lines += ['## ' + title, '', explanation, '']
        for token, item in values.items():
            if item['anchor'] in seen:
                continue
            seen.add(item['anchor'])
            lines += [
                '### ' + item['meaning'] + ' {#' + item['anchor'] + '}',
                '',
                badge(family, token) + ' ' + meanings.get(item['anchor'], explanation),
                '',
            ]
    lines += [
        '## Next steps',
        '',
        '[Choose an example](examples.md) · [Fitting modes](fitting-modes.md) · [Instrument and profiles](../physics/profiles.md)',
        '',
    ]
    (DOCS / 'user-guide/experiment-types.md').write_text('\n'.join(lines))
    # One compact, progressively disclosed catalogue; all entries remain readable without JS.
    controls = [
        '<div class="ed-example-filters"><input type="search" data-example-search aria-label="Search examples" placeholder="Search sample, instrument or label">'
    ]
    for family, title in [
        ('purpose', 'Purpose'),
        ('fittingMode', 'Fitting mode'),
        ('sampleForm', 'Sample form'),
        ('probe', 'Probe'),
        ('beamMode', 'Beam mode'),
    ]:
        values = sorted({
            v for entry in metadata.values() for v in entry['values'].get(family, [])
        })
        if len(values) < 2:
            continue
        options = ['<option value="">All ' + title.lower() + 's</option>']
        for token in values:
            label = registry['tags'].get(family, {}).get(token, {}).get('meaning', token)
            options.append(
                f'<option value="{html.escape(token, quote=True)}">{html.escape(label)}</option>'
            )
        controls.append(
            f'<select data-example-filter="{family}" aria-label="{title}">'
            + ''.join(options)
            + '</select>'
        )
    controls.append('</div><p data-example-count aria-live="polite"></p>')
    rows = [
        '<table><thead><tr><th>Example</th><th>Purpose and experiment</th></tr></thead><tbody>'
    ]
    for identity, entry in metadata.items():
        attrs = ' '.join(
            f'data-{key.lower()}="{html.escape(json.dumps(values), quote=True)}"'
            for key, values in entry['values'].items()
        )
        title = ' / '.join(entry['samples']) + ' · ' + entry['origin']
        labels = []
        for family, values in registry['tags'].items():
            for token in entry['values'].get(family, []):
                if token in values:
                    labels.append(badge(family, token))
        search = html.escape(
            (
                identity + ' ' + title + ' ' + entry['detail'] + ' ' + json.dumps(entry['values'])
            ).lower(),
            quote=True,
        )
        rows.append(
            f'<tr data-example-row data-search="{search}" {attrs}><td><a class="ed-example-name" href="https://github.com/enhantica/edi/tree/ai-assistant-on-dev/docs/user/cli/{identity}">{html.escape(title)}</a>{html.escape(entry["detail"])}</td><td>'
            + ' '.join(labels)
            + '</td></tr>'
        )
    rows.append('</tbody></table>')
    content = (
        '<details><summary>Find more examples by measurement type</summary>\n<div data-example-catalogue>\n'
        + '\n'.join(controls + rows)
        + '\n</div>\n</details>'
    )
    replace(DOCS / 'user-guide/examples.md', 'example-catalogue', content)
    replace(
        DOCS / 'user-guide/glossary.md',
        'experiment-labels',
        'For linked definitions of `pd`, `sc`, `neut`, `xray`, `cwl` and `tof`, see [Experiment types and labels](experiment-types.md).',
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--import-native', type=Path)
    args = parser.parse_args()
    if args.import_native:
        ASSETS.mkdir(parents=True, exist_ok=True)
        source = args.import_native.resolve()
        provenance = {
            'edi_commit': subprocess.check_output(
                ['git', 'rev-parse', 'HEAD'], cwd=source, text=True
            ).strip(),
            'files': {},
        }
        for name, filename in [('tags', 'tags.json'), ('examples', 'metadata.json')]:
            path = source / 'app/examples' / filename
            data = path.read_bytes()
            provenance['files'][filename] = hashlib.sha256(data).hexdigest()
            shutil.copyfile(
                path, ASSETS / ('experiment-tags.json' if name == 'tags' else 'examples.json')
            )
        (ASSETS / 'experiment-provenance.json').write_text(json.dumps(provenance, indent=2) + '\n')
    render()


if __name__ == '__main__':
    main()
