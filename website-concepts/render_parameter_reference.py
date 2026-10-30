#!/usr/bin/env python3
"""Build linked GUI/Edi/Python/CIF tables from the native dictionary and verified bindings."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
from operator import itemgetter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'surfaces/docs'
ASSETS = DOCS / 'assets/reference'
STRUCTURE = {
    'space_group',
    'cell',
    'atom_site',
    'atom_site_aniso',
    'scattering_length',
    'geom',
    'structure_view',
    'space_group_symop',
    'expanded_atom_site',
    'geom_bond',
    'atom_sites_cartn_transform',
}
EXPERIMENT = {
    'experiment_type',
    'scattering_source',
    'data_source',
    'data_range',
    'data',
    'instrument',
    'peak',
    'background',
    'background_estimate',
    'absorption',
    'extinction',
    'reflns',
    'linked_structure',
    'preferred_orientation',
    'excluded_region',
    'refln',
    'data_calc',
    'pd_calc',
    'pd_calc_overall',
}


# Category-specific guides use the native category symbol; broad workflow groups
# retain the existing Material workflow icons (ADR-0002).
CATEGORY_PAGES = {
    'application/symmetry.md': 'cell',
    'application/atoms.md': 'atom_site',
    'application/displacement.md': 'atom_site_aniso',
    'application/instrument.md': 'instrument',
    'application/peak-profiles.md': 'peak',
    'application/background.md': 'background',
    'application/linked-structures.md': 'linked_structure',
    'application/minimizer.md': 'minimizer',
    'application/fitting-modes.md': 'fitting_mode',
}


def anchor(uid: str) -> str:
    if not re.fullmatch(r'[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)?', uid):
        raise ValueError('Invalid dictionary identity: ' + uid)
    return uid.replace('_', '-').replace('.', '-')


def plain(text: str) -> str:
    # Dictionary provenance belongs in the retained metadata, rather than user descriptions.
    text = re.sub(r'\s*\(ADR-\d+[^)]*\)', '', text)
    return html.escape(text).replace('|', '&#124;').replace('\n', ' ')


def code(value: str) -> str:
    return '<code>' + html.escape(value).replace('|', '&#124;') + '</code>'


def icon(name: str, glyphs: dict, *, category: str = '') -> str:
    if not name:
        return ''
    value = glyphs.get(name)
    if value is None:
        raise ValueError('Native icon has no exported Font Awesome glyph: ' + name)
    marker = f' data-reference-category="{anchor(category)}"' if category else ''
    return f'<span class="ed-reference-icon"{marker} aria-hidden="true">&#{value};</span> '


def parameter_icon(name: str, rules: list) -> str:
    return next((value for prefix, value in rules if name.startswith(prefix)), '')


def render() -> None:
    if not (ASSETS / 'dictionary.json').exists():
        return
    dictionary = json.loads((ASSETS / 'dictionary.json').read_text())
    paths = json.loads((ASSETS / 'python-paths.json').read_text())['paths']
    rules = json.loads((ASSETS / 'gui-parameter-icons.json').read_text())
    glyphs = json.loads((DOCS / 'assets/gui-icons/glyphs.json').read_text())
    catalogue = json.loads((DOCS / 'physics/catalogue.json').read_text())
    scientific = {entry['id']: entry for entry in catalogue['parameters']}
    categories = sorted(dictionary['categories'], key=itemgetter('order'))
    items = dictionary['items']
    uids = [item['uid'] for item in items]
    if len(set(uids)) != len(uids) or set(scientific) - set(uids):
        raise ValueError('Native dictionary must cover every existing scientific parameter')
    anchors = [anchor(uid) for uid in uids] + [anchor(c['id']) for c in categories]
    if len(set(anchors)) != len(anchors):
        raise ValueError('Reference anchor collision')
    lookup = {category['id']: category for category in categories}

    def gui(item: dict) -> str:
        category = item['category']
        label = plain(item['label'])
        if not item['parameter']:
            return label
        block_icon = (
            'layer-group'
            if category in STRUCTURE
            else 'microscope'
            if category in EXPERIMENT
            else ''
        )
        return (
            icon(block_icon, glyphs)
            + icon(lookup[category]['icon'], glyphs)
            + icon(parameter_icon(item['name'], rules), glyphs)
            + label
        )

    def cif(item: dict) -> str:
        variants = [v for v in item['variants'] if v['cif_names']]
        if variants:
            return '<br>'.join(code(v['token']) + ': ' + code(v['cif_names'][0]) for v in variants)
        return code(item['cif_names'][0]) if item['cif_names'] else '—'

    details = [
        '---',
        'template: physics.html',
        '---',
        '',
        '# Parameter and category reference',
        '',
        'Look up a GUI label, Edi key or CIF name. Each entry describes the current field; applicability depends on the experiment and selected model. [Compare the naming systems](../user-guide/parameter-reference.md).',
        '',
    ]
    tables = [
        '# Parameter names across interfaces',
        '',
        'Choose the names you are working with. Each category and field links to its description and scientific meaning.',
        '',
        'The **GUI** view shows control labels and the icon pattern used by Analysis parameters. The selected block, atom-site identifier and colours provide additional context in the app. **Edi** gives the keys shown in the Text tab and saved projects. **Python** gives access paths checked against the example projects; use `.value` or `.free` on a parameter. **CIF** gives the primary exchange name, including type-dependent forms.',
        '',
        'A dash means no mapping was declared, or no direct Python field was found in the checked examples. It does not imply that an Edi key is an IUCr CIF item. A listed field is not necessarily applicable, editable or independently refinable in every model.',
        '',
        '```python',
        'parameter = project.structures[0].cell.length_a',
        'print(parameter.value, parameter.free)',
        '```',
        '',
    ]
    for heading, group in [
        ('Structure parameters', STRUCTURE),
        ('Experiment parameters', EXPERIMENT),
        ('Project and analysis settings', set(lookup) - STRUCTURE - EXPERIMENT),
    ]:
        tables += ['## ' + heading, '']
        selected = [c for c in categories if c['id'] in group]
        for projection in ['GUI', 'Edi', 'Python', 'CIF']:
            tables += ['=== "' + projection + '"', '']
            for category in selected:
                entries = [item for item in items if item['category'] == category['id']]
                if not entries:
                    continue
                url = '../physics/parameters.md#' + anchor(category['id'])
                tables += [
                    '    **['
                    + icon(category['icon'], glyphs, category=category['id'])
                    + category['title']
                    + ']('
                    + url
                    + ')**',
                    '',
                    '    | Parameter or field | ' + projection + ' name | Units |',
                    '    | --- | --- | --- |',
                ]
                for item in entries:
                    url = '../physics/parameters.md#' + anchor(item['uid'])
                    name = '[' + plain(item['label']) + '](' + url + ')'
                    value = (
                        gui(item)
                        if projection == 'GUI'
                        else code(item['edi_tag'])
                        if projection == 'Edi'
                        else '<br>'.join(code(p) for p in paths.get(item['uid'], [])) or '—'
                        if projection == 'Python'
                        else cif(item)
                    )
                    tables.append(
                        '    | '
                        + name
                        + ' | '
                        + value
                        + ' | '
                        + (plain(item['units']) or '—')
                        + ' |'
                    )
                tables.append('')
    for category in categories:
        entries = [item for item in items if item['category'] == category['id']]
        if not entries:
            continue
        details += [
            '## '
            + icon(category['icon'], glyphs, category=category['id'])
            + category['title']
            + ' {#'
            + anchor(category['id'])
            + '}',
            '',
            code(category['edi_name']) + ' — ' + plain(category['description']),
            '',
        ]
        for item in entries:
            identity = anchor(item['uid'])
            details += [
                '### ' + code(item['edi_tag']) + ' {#' + identity + '}',
                '',
                plain(item['description']),
                '',
                '**GUI:** '
                + gui(item)
                + '. **Units:** '
                + (plain(item['units']) or 'not applicable')
                + '.',
                '',
            ]
            if item['uid'] in scientific:
                entry = scientific[item['uid']]
                details += [
                    '**Calculation role:** '
                    + entry['role']
                    + '. [Scientific explanation]('
                    + entry['explanation_url'].replace('/#', '.md#')
                    + ').',
                    '',
                ]
            if paths.get(item['uid']):
                details += [
                    '**Python:** ' + ', '.join(code(p) for p in paths[item['uid']]) + '.',
                    '',
                ]
            if item['cif_names']:
                details += [
                    '**CIF names:** ' + ', '.join(code(v) for v in item['cif_names']) + '.',
                    '',
                ]
            if item['edi_aliases']:
                details += [
                    '**Earlier Edi spellings accepted on import:** '
                    + ', '.join(code(v) for v in item['edi_aliases'])
                    + '.',
                    '',
                ]
            if item['options']:
                details += ['| Stored value | GUI option | Meaning |', '| --- | --- | --- |']
                for option in item['options']:
                    details += [
                        '| '
                        + code(option['token'])
                        + ' | '
                        + plain(option['label'])
                        + ' | '
                        + plain(option['description'])
                        + ' |'
                    ]
                details += ['']
            if item['variants']:
                details += ['| Form | GUI label | Units | CIF name |', '| --- | --- | --- | --- |']
                for variant in item['variants']:
                    details += [
                        '| '
                        + code(variant['token'])
                        + ' | '
                        + plain(variant['label'] or item['label'])
                        + ' | '
                        + plain(variant['units'] or item['units'])
                        + ' | '
                        + (code(variant['cif_names'][0]) if variant['cif_names'] else '—')
                        + ' |'
                    ]
                details += ['']
    (DOCS / 'physics/parameters.md').write_text('\n'.join(details))
    (DOCS / 'user-guide/parameter-reference.md').write_text('\n'.join(tables))
    for filename, uid in CATEGORY_PAGES.items():
        category = lookup[uid]
        glyph = glyphs[category['icon']]
        path = DOCS / filename
        text = path.read_text()
        # This metadata is generated from the same exported dictionary as headings.
        text = re.sub(r'^category_glyph:.*\n', '', text, flags=re.MULTILINE)
        if not text.startswith('---\n'):
            raise ValueError('Category guide must retain its template front matter: ' + filename)
        text = text.replace('---\n', '---\ncategory_glyph: ' + json.dumps(chr(glyph)) + '\n', 1)
        text = re.sub(
            r'^(# )<span[^>]*data-reference-category="[^"\n]+"[^>]*>.*?</span>\s*',
            r'\1',
            text,
            count=1,
            flags=re.MULTILINE,
        )
        text = re.sub(r'^(# ):material-[a-z-]+:\s*', r'\1', text, count=1, flags=re.MULTILINE)
        text, count = re.subn(
            r'^# ',
            '# ' + icon(category['icon'], glyphs, category=uid),
            text,
            count=1,
            flags=re.MULTILINE,
        )
        if count != 1:
            raise ValueError('Category guide must have a title: ' + filename)
        path.write_text(text)
    # A portable exact lookup also consumed by native help verification and future integrations.
    (ASSETS / 'parameter-links.json').write_text(
        json.dumps(
            {uid: 'physics/parameters/#' + anchor(uid) for uid in [*lookup, *uids]}, indent=2
        )
        + '\n'
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--import-native', type=Path)
    parser.add_argument('--dictionary', type=Path)
    parser.add_argument('--python-paths', type=Path)
    parser.add_argument('--sdk-library', type=Path)
    args = parser.parse_args()
    if args.import_native:
        if not args.dictionary or not args.python_paths or not args.sdk_library:
            parser.error('Import requires --dictionary, --python-paths and --sdk-library')
        source = args.import_native.resolve()
        ASSETS.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(args.dictionary, ASSETS / 'dictionary.json')
        shutil.copyfile(args.python_paths, ASSETS / 'python-paths.json')
        # Reuse the exact prefix rules of the native Analysis name renderer.
        qml = source / 'app/qml/Globals/ParameterNames.qml'
        rules = re.search(r'const icons = (\[.*?\]);', qml.read_text()).group(1)
        (ASSETS / 'gui-parameter-icons.json').write_text(
            json.dumps(json.loads(rules), indent=2) + '\n'
        )
        provenance = {
            'edi_commit': subprocess.check_output(
                ['git', 'rev-parse', 'HEAD'], cwd=source, text=True
            ).strip(),
            'source_sha256': {
                str(path.relative_to(source)): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in [
                    qml,
                    source / 'tools/docs/reference-metadata.cpp',
                    source / 'tools/docs/python-reference.py',
                    source / 'data/category-census.json',
                ]
            },
            'sdk_library_sha256': hashlib.sha256(args.sdk_library.read_bytes()).hexdigest(),
        }
        (ASSETS / 'parameter-provenance.json').write_text(json.dumps(provenance, indent=2) + '\n')
    render()


if __name__ == '__main__':
    main()
