#!/usr/bin/env python3
"""Import a validated native walkthrough and generate its illustrated documentation."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from itertools import starmap
from pathlib import Path

from checks.gui_capture import validate_bundle

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'surfaces/docs'
LABELS = {
    'appBar': (
        'Workflow navigation',
        'Move between Home, Project, Structure, Experiment, Analysis and Report.',
    ),
    'statusBar': (
        'Status bar',
        'Read project counts, messages, calculation and fitting state here.',
    ),
    'home.start': ('Start', 'Begin a new analysis on the Project page.'),
    'project.create': ('Create a new project', 'Open the project-details form.'),
    'group.getStarted': ('Get started', 'Create a project or open an existing one.'),
    'createProject.name': ('Name', 'Use a short project identifier.'),
    'createProject.title': ('Title', 'Give the analysis a descriptive title.'),
    'createProject.description': ('Description', 'Record the sample, measurement and purpose.'),
    'createProject.location': ('Location', 'Choose where the project will be saved.'),
    'structures.load': ('Load structure', 'Import the structure file for this example.'),
    'structures.list': (
        'Structures',
        'Select the structure whose cell and atom sites you want to inspect.',
    ),
    'experiments.load': (
        'Load experiment',
        'Import the experiment file, including measured intensities and instrument settings.',
    ),
}

LABELS.update({
    'group.examples': (
        'Built-in examples',
        'Search or filter the example catalogue and select a case.',
    ),
    'project.openChoice': ('Project source', 'Choose a folder or a zip archive.'),
    'project.saveChoice': ('Save options', 'Choose the output format and whether to save a copy.'),
    'structures.create': ('Create structure', 'Add a starting structure to edit.'),
    'structures.duplicate': ('Duplicate structure', 'Copy the selected structure.'),
    'spaceGroup.itNumber': ('Space-group number', 'Select the symmetry of your model.'),
    'spaceGroup.nameHM': ('Space-group symbol', 'Check the Hermann-Mauguin symbol and setting.'),
    'cell.length_a': ('Cell length a', 'Inspect the cell length and its uncertainty.'),
    'cell.length_b': ('Cell length b', 'Values controlled by symmetry are linked.'),
    'cell.length_c': ('Cell length c', 'Use the cell convention of the selected space group.'),
    'atomSites.list': (
        'Atom sites',
        'Inspect atom types, fractional coordinates and occupancies.',
    ),
    'experiments.list': ('Experiments', 'Select the measurement to inspect.'),
    'experiments.loadData.0': (
        'Measured-data file',
        'Load the observed intensities for this experiment.',
    ),
    'experiments.create': (
        'Create experiment',
        'Add an experiment and choose its measurement type.',
    ),
    'background.type': ('Background model', 'Choose the background representation.'),
    'background.rows': (
        'Background values',
        'Inspect or edit the values in the selected representation.',
    ),
    'excludedRegions.list': (
        'Excluded intervals',
        'Set the boundaries of regions omitted from fitting.',
    ),
    'linkedStructure.list': (
        'Linked structures',
        'Inspect phase links, scales and derived fractions.',
    ),
    'fittingMode.type': ('Fitting mode', 'The available choices depend on the project.'),
    'report.writesHtml': ('HTML report', 'Select an HTML document.'),
    'report.writesPdf': ('PDF report', 'Select a PDF document.'),
    'report.writesCif': ('CIF report', 'Select a crystallographic report.'),
    'report.save': ('Save report', 'Write the selected report formats.'),
    'group.su_format': (
        'Standard uncertainties',
        'Choose how values and their standard uncertainties are written.',
    ),
    'group.appearance': (
        'Appearance',
        'Choose atom sizes, display scale and displacement ellipsoids.',
    ),
    'group.scattering_length': (
        'Scattering lengths',
        'Set custom neutron scattering lengths for atom types in this structure.',
    ),
    'group.scattering_source': (
        'Scattering source',
        'Choose the neutron scattering-length reference used by the experiment.',
    ),
    'group.instrument': (
        'Instrument',
        'Inspect the measurement conditions and calibration parameters.',
    ),
    'group.peak': ('Peak profile', 'Choose the peak shape and edit its profile parameters.'),
    'group.data': ('Measured data', 'Inspect the measured range, intensities and uncertainties.'),
    'group.absorption': (
        'Absorption',
        'Choose the sample absorption model and its physical parameters.',
    ),
    'group.preferred_orientation': (
        'Preferred orientations',
        'Set preferred directions and March parameters for linked structures.',
    ),
    'group.alias': ('Aliases', 'Give parameters short names for use in constraint expressions.'),
    'group.constraint': (
        'Constraints',
        'Define relations between aliased parameters and enable the relations to apply.',
    ),
    'group.minimizer': ('Minimizer', 'Choose the descent strategy and convergence settings.'),
    'group.shownParameters': (
        'Parameters shown',
        'Choose which additional parameter groups appear alongside free parameters.',
    ),
    'group.patternUpdates': (
        'Pattern updates during a scan',
        'Choose how often the display updates while a scan is fitted.',
    ),
    'peak.cutoff_fwhm': (
        'Peak cutoff',
        'Set the peak calculation window in multiples of the full width at half maximum.',
    ),
    'fitStart.list': (
        'Fit start values',
        'Inspect the free parameters before the last fit; use Undo to restore that state.',
    ),
})


def label(target: str, page: str, native_label: str = '') -> tuple[str, str]:
    if target in LABELS:
        return LABELS[target]
    if target.endswith('.mainContent'):
        return (
            'Main workspace',
            f'Inspect the {page} view here. Its content changes with the active page and selection.',
        )
    if target.endswith('.manualSidebar'):
        return (
            'Sidebar',
            'Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.',
        )
    if target.endswith('.page'):
        return (
            'Workflow page',
            'The selected toolbar tab opens this workspace and its sidebar together.',
        )
    if target.startswith('group.'):
        title = native_label or re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', target[6:]).replace('_', ' ')
        return title[:1].upper() + title[1:], ''
    return native_label or target, ''


def region_parts(meta: dict, target: str) -> list[list[float]]:
    """Join a sidebar's active tab to its body using this capture's Qt bounds."""
    if target.startswith('mainView.'):
        _, name, key = target.split('.')
        tab = meta['items'][f'mainArea.{name}.tab.{key}']
        x, y, width, height = meta['items'][f'workflow.{name}.mainContent']['visible_bounds']
        tx, ty, tw, th = tab['visible_bounds']
        bottom = ty + th
        if not tab['enabled'] or not (
            x <= tx < tx + tw <= x + width and y <= ty < bottom < y + height
        ):
            raise ValueError('A main-view tab must be enabled and inside its workspace')
        return [[x, bottom, width, y + height - bottom], [tx, ty, tw, th]]
    if target.endswith('.page'):
        name = target.split('.')[1]
        main = meta['items'][f'workflow.{name}.mainContent']['visible_bounds']
        tab = meta['items'][f'appBar.tab.{name}']['visible_bounds']
        if name == 'home':
            return [main, tab]
        sidebar = meta['items'][f'workflow.{name}.manualSidebar']['visible_bounds']
        x, y, width, height = main
        sx, sy, sw, sh = sidebar
        if abs(x + width - sx) > 0.1 or abs(y - sy) > 0.1 or abs(height - sh) > 0.1:
            raise ValueError('Workflow regions must form one adjoining page')
        return [[x, y, width + sw, height], tab]
    bounds = meta['items'][target]['visible_bounds']
    if not target.endswith('.manualSidebar'):
        return [bounds]
    selected = [tab for tab in meta['state']['sidebar_tabs'] if tab['checked']]
    if len(selected) != 1:
        raise ValueError('A sidebar outline requires one selected native tab')
    tab = meta['items'].get(selected[0]['id'], {})
    if tab.get('ambiguous') or 'visible_bounds' not in tab:
        raise ValueError('The selected native tab has no unique visible geometry')
    tx, ty, tw, th = tab['visible_bounds']
    x, y, width, height = bounds
    bottom = ty + th
    if not (x <= tx < tx + tw <= x + width and y <= ty < bottom < y + height):
        raise ValueError('The selected tab must sit inside its sidebar')
    return [[x, bottom, width, y + height - bottom], [tx, ty, tw, th]]


def region_path(parts: list[list[float]], padding: float = 2) -> str:
    """Trace a square outline; the browser adjusts padding to display pixels."""
    x, y, width, height = parts[0]
    left, top, right, bottom = x - padding, y - padding, x + width + padding, y + height + padding
    points = [(left, top)]
    if len(parts) == 2:
        tx, ty, tw, _ = parts[1]
        points += [
            (tx - padding, top),
            (tx - padding, ty - padding),
            (tx + tw + padding, ty - padding),
            (tx + tw + padding, top),
        ]
    points += [(right, top), (right, bottom), (left, bottom)]
    return 'M' + ' L'.join(f'{px:.3f} {py:.3f}' for px, py in points) + ' Z'


def gui_icon(item: dict) -> str:
    name = item.get('icon', '')
    if not name:
        return ''
    glyphs = json.loads((DOCS / 'assets/gui-icons/glyphs.json').read_text())
    code = ord(name) if len(name) == 1 and 0xE000 <= ord(name) <= 0xF8FF else glyphs.get(name)
    if code is None:
        raise ValueError(f'GUI icon is absent from the bundled Font Awesome 5 face: {name}')
    return f'<span class="gui-fa" aria-hidden="true">&#{code};</span>'


def pane(title: str, content: str) -> str:
    title = title.replace('"', "'")
    return (
        '\n=== "'
        + title
        + '"\n\n'
        + '\n'.join('    ' + line if line else '' for line in content.splitlines())
        + '\n'
    )


def viewer(panes: list[tuple[str, str]]) -> str:
    content = ''.join(starmap(pane, panes)) if len(panes) > 1 else panes[0][1]
    return '<div class="gui-viewer" markdown="1">\n\n' + content + '\n</div>\n'


def figure(
    scene: dict,
    *,
    view: str = 'overview',
    instance: str = '',
    description: str = '',
    explanation: str = '',
    selection: str = '',
    interactive: bool = True,
) -> str:
    meta = scene['layout']
    image = '../assets/gui/y2o3/' + scene['image'] + '?v=' + meta['image_sha256'][:12]
    description = html.escape(description or scene['description'], quote=True)
    identity = f'{scene["id"]}-{view}' + (f'-{instance}' if instance else '')
    if selection:
        identity += '-' + selection.replace('.', '-')
    targets = (
        [f'workflow.{scene["page"]}.manualSidebar']
        if view == 'sidebar'
        else ([f'workflow.{scene["page"]}.page'] if view == 'workflow' else meta['highlights'])
    )
    if view == 'main':
        targets = [f'mainView.{scene["page"]}.{selection.rsplit(".", 1)[1]}']
    navigation = ''
    if view == 'overview':
        targets = [target for target in targets if target != 'appBar']
        empty = (
            scene['page'] == 'home'
            or (scene['page'] == 'structure' and not meta['state']['structures'])
            or (scene['page'] == 'experiment' and not meta['state']['experiments'])
        )
        if empty:
            targets = [target for target in targets if not target.endswith('.mainContent')]
        tab = f'appBar.tab.{scene["page"]}'
        parts = region_parts(meta, tab)
        data = html.escape(json.dumps(parts, separators=(',', ':')), quote=True)
        navigation = (
            f'<path data-gui-navigation data-gui-parts="{data}" d="{region_path(parts)}" />'
        )
    if interactive and view in {'overview', 'layout'}:
        panes = []
        if view == 'layout':
            panes.append((
                'Overview',
                figure(
                    scene,
                    view=view,
                    instance=instance,
                    interactive=False,
                    explanation='The page bar, main view, sidebar and status bar stay in the same places as you work.',
                ),
            ))
        for target in targets:
            item = meta['items'].get(target, {})
            title, text = label(target, scene['page'], item.get('label', ''))
            panes.append((
                gui_icon(item) + html.escape(title),
                figure(
                    scene,
                    view=view,
                    instance=instance,
                    selection=target,
                    interactive=False,
                    description=title,
                    explanation=text or scene['description'].rstrip('.') + '.',
                ),
            ))
        return viewer(panes)
    if selection and view != 'main':
        targets = [selection]
    paths = []
    for number, target in enumerate(targets, 1):
        inset = view in {'layout', 'flow'}
        parts = [meta['items'][target]['visible_bounds']] if inset else region_parts(meta, target)
        key = f'{identity}-{number}'
        data = html.escape(json.dumps(parts, separators=(',', ':')), quote=True)
        paths.append(
            f'<path class="{"is-active" if number == 1 or view in {"layout", "flow"} else ""}" data-gui-region="{key}" '
            + ('data-gui-inset="2" ' if inset else '')
            + f'data-gui-parts="{data}" d="{region_path(parts, -2 if inset else 2)}" />'
        )
    arrows = ''
    if view == 'flow':
        half = meta['items']['appBar']['visible_bounds'][3] * 0.18
        for axis, name in [
            ('x', 'appBar.workflow'),
            ('y', f'workflow.{scene["page"]}.manualSidebar'),
        ]:
            x, y, width, height = meta['items'][name]['visible_bounds']
            if axis == 'x':
                start, end, centre = (
                    x + width * 0.08,
                    x + width * 0.92,
                    y + height * 0.5,
                )
                points = [
                    (start, centre - half),
                    (end - half * 2, centre - half),
                    (end - half * 2, centre - half * 2),
                    (end, centre),
                    (end - half * 2, centre + half * 2),
                    (end - half * 2, centre + half),
                    (start, centre + half),
                ]
            else:
                start, end, centre = (
                    y + height * 0.12,
                    y + height * 0.88,
                    x + width * 0.5,
                )
                points = [
                    (centre - half, start),
                    (centre + half, start),
                    (centre + half, end - half * 2),
                    (centre + half * 2, end - half * 2),
                    (centre, end),
                    (centre - half * 2, end - half * 2),
                    (centre - half, end - half * 2),
                ]
            data = 'M' + ' L'.join(f'{px:.2f} {py:.2f}' for px, py in points) + ' Z'
            arrows += f'<path class="gui-direction is-active" data-gui-direction data-gui-axis="{axis}" d="{data}" aria-hidden="true" />'
    clip = f'gui-clip-{identity}'
    return (
        '<figure class="gui-figure" data-gui-figure>\n'
        + (
            f'<p class="gui-view-description">{html.escape(explanation)}</p>\n'
            if explanation
            else ''
        )
        + f'<a class="gui-image-link" href="{image}" data-gui-open aria-haspopup="dialog" '
        f'aria-label="Enlarge screenshot: {description}">'
        f'<svg class="gui-capture" data-gui-view="{view}" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="{description}">'
        f'<title>{description}</title><defs><clipPath id="{clip}"><rect width="1480" height="800" rx="12" /></clipPath></defs>'
        f'<image href="{image}" width="1480" height="800" clip-path="url(#{clip})" />'
        '<rect class="gui-image-frame" width="1480" height="800" rx="12" />'
        + ''.join(paths)
        + navigation
        + arrows
        + '</svg></a>\n'
        + '\n</figure>\n'
    )


def page(title: str, body: str) -> str:
    return f'---\ntemplate: gui.html\n---\n\n# {title}\n\n{body.rstrip()}\n'


def native_options(text: str, by_id: dict[str, dict]) -> str:
    """Keep authored choice lists bound to the captured native selector model."""
    models = {
        (entry['category'], entry['id']): entry['explanation_url']
        for entry in json.loads((DOCS / 'physics/catalogue.json').read_text())['models']
    }

    def replace(match: re.Match[str]) -> str:
        scene, target, category = match.group(1, 2, 3)
        options = by_id[scene]['layout']['items'][target].get('options', [])
        if not options or len({item['token'] for item in options}) != len(options):
            raise ValueError(f'{scene}: {target} needs unique native options')
        rows = []
        for item in options:
            name = html.escape(item['label']).replace('|', '&#124;')
            if category:
                route = models[category, item['token']]
                name = f'[{name}](../physics/{route})'
            rows.append(f'- {name}')
        return match[0].split('\n', 1)[0] + '\n' + '\n'.join(rows) + '\n<!-- /gui-options -->'

    return re.sub(
        r'<!-- gui-options:([\w-]+):([\w.]+):([\w]*) -->\n.*?<!-- /gui-options -->',
        replace,
        text,
        flags=re.DOTALL,
    )


def illustrate_guides(by_id: dict[str, dict]) -> None:
    """Place source-matched scenes after their corresponding how-to instructions."""
    if 'guide-project-open' not in by_id:
        return
    registry = json.loads((ROOT / 'gui-guide-scenes.json').read_text())
    for filename, sections in registry.items():
        source = DOCS / filename
        text = native_options(source.read_text(), by_id)
        text = re.sub(r'<!-- gui-guide:.*?<!-- /gui-guide -->\n?', '', text, flags=re.DOTALL)
        text = re.sub(r'<figure class="gui-figure".*?</figure>\n?', '', text, flags=re.DOTALL)
        headings = list(re.finditer(r'^## (.+)$', text, re.MULTILINE))
        present = {match[1] for match in headings}
        missing = set(sections) - present
        if missing:
            raise ValueError(f'{filename}: missing authored headings {sorted(missing)}')
        for number in reversed(range(len(headings))):
            match = headings[number]
            if match[1] not in sections:
                continue
            scenes = sections[match[1]]
            if isinstance(scenes, str):
                scenes = [scenes]
            slug = re.sub(r'[^a-z0-9]+', '-', match[1].lower()).strip('-')
            figures = []
            for index, identity in enumerate(scenes):
                if identity not in by_id:
                    raise ValueError(f'{filename}: required capture {identity} is missing')
                figures.append(figure(by_id[identity], instance=f'{source.stem}-{slug}-{index}'))
            end = headings[number + 1].start() if number + 1 < len(headings) else len(text)
            content = (
                f'\n<!-- gui-guide:{slug} -->\n' + '\n'.join(figures) + '<!-- /gui-guide -->\n\n'
            )
            text = text[:end].rstrip() + '\n' + content + text[end:]
        if not text.startswith('---\n'):
            text = '---\ntemplate: gui.html\n---\n\n' + text
        source.write_text(text.rstrip() + '\n')


def render(bundle: Path) -> None:
    manifest, scenes = validate_bundle(bundle)
    by_id = {scene['id']: scene for scene in scenes}
    fixture = manifest.get('fixture', {'samples': ['Y₂O₃'], 'origin': 'SPODI @ FRM II'})
    structure_file = Path(manifest['inputs']['structure']['file']).name
    experiment_file = Path(manifest['inputs']['experiment']['file']).name
    destination = DOCS / 'assets/gui/y2o3'
    destination.mkdir(parents=True, exist_ok=True)
    artifacts = {'manifest.json', 'walkthrough.js'}
    artifacts.update(item['file'] for item in manifest['inputs'].values())
    artifacts.update(item['file'] for item in manifest.get('dependencies', []))
    for scene in scenes:
        artifacts.update((scene['image'], scene['metadata']))
    for artifact in sorted(artifacts):
        target = destination / artifact
        target.parent.mkdir(parents=True, exist_ok=True)
        if (bundle / artifact).resolve() != target.resolve():
            shutil.copy2(bundle / artifact, target)
    intro = f"""Build a project from its separate inputs, refine the model and review the report. This example is **{manifest['example']}**: {' + '.join(fixture['samples'])}, {fixture['origin']}.

Select a numbered explanation to highlight that part of the interface. The [application layout](workspace.md) introduces the workspace and every enabled sidebar tab.

## Download the inputs

- [Crystal structure: {structure_file}](../assets/gui/y2o3/{manifest['inputs']['structure']['file']})
- [Experiment and measured intensities: {experiment_file}](../assets/gui/y2o3/{manifest['inputs']['experiment']['file']})

The experiment input contains the measured pattern, instrument, profile, background and starting free parameters. Import these files separately; start with an empty project.
"""
    sections = [
        ('Home', 'Open EasyDiffraction and press **Start**.', '01-home'),
        ('Create a project', 'Choose **Create a new project**.', '02-project-start'),
        (
            'Enter the project details',
            'Enter a name, title, authors and description for the analysis. Choose a location on your computer, then confirm.',
            '03-project-details',
        ),
        (
            'Inspect the project',
            'The Project page keeps the analysis details together. The enabled sidebar tabs offer additional views of this state.',
            '04-project-created',
        ),
        (
            'Load the structure',
            f'Open **Structure**, expand **Structures**, choose **Load** and select **{structure_file}**.',
            '06-structure-import',
        ),
        (
            'Inspect the crystal structure',
            'Inspect the cell, symmetry and atom sites. See [crystallography](../physics/crystallography.md) and [atomic displacement parameters](../physics/displacement.md) for their physical meaning.',
            '07-structure-loaded',
        ),
        (
            'Load the experiment',
            f'Open **Experiment**, expand **Experiments**, choose **Load** and select **{experiment_file}**.',
            '09-experiment-import',
        ),
        (
            'Inspect the initial pattern',
            'Compare the measured and calculated intensities before fitting. Review the [peak profile](../physics/profiles/cw.md), [background](../physics/background.md), reflection marks and residual.',
            '10-experiment-loaded',
        ),
        (
            'Refine the model',
            'Open **Analysis**, inspect the free parameters and press **Fit**. Wait for fitting to finish, review the result and close the results popup. This screenshot shows the completed fit with that popup closed. See [Rietveld refinement](../physics/rietveld.md), [uncertainties](../physics/minimization.md) and [reliability factors](../physics/reliability.md).',
            '13-analysis-basic',
        ),
        (
            'Review the report',
            'Open **Report** to review the structure, measurement and fitted results. Use the sidebar to choose the report contents and export format.',
            '14-report-basic',
        ),
    ]
    body = intro
    for title, explanation, identity in sections:
        body += f'\n## {title}\n\n{explanation}\n\n' + figure(by_id[identity])
    body += '\n## Explore the workspace\n\nSee [Application layout](workspace.md) for an annotated overview of every workflow page and its enabled sidebar tabs.\n'
    (DOCS / 'application/first-refinement.md').write_text(page('Example refinement', body))
    workspace = """The interface follows the same analysis workflow as the [User guide](../user-guide/analysis-workflow/index.md). The top bar selects a page, the central workspace shows its main view, and the sidebar contains the related controls.

## Main regions

Choose a tab to inspect each region. These four areas stay in the same places on every workflow page.

"""
    workspace += figure(by_id['11-experiment-basic'], view='layout')
    workspace += '\n## Following the workflow\n\nMove through the pages from left to right. Within each page, work down the sidebar from top to bottom.\n\n'
    workspace += figure(
        by_id['11-experiment-basic'],
        view='flow',
        interactive=False,
        description='Follow the pages from left to right and the sidebar controls from top to bottom',
    )
    workspace += """
## Workflow pages

| Page | What you do here |
| --- | --- |
| Home | Start an analysis, learn the interface and find help. |
| Project | Create or open a project and record its details. |
| Structure | Load and inspect the crystal structure, cell and atom sites. |
| Experiment | Load measured intensities and configure the instrument, profile and background. |
| Analysis | Choose free parameters, run fitting and inspect the fitted pattern and results. |
| Report | Review and export a report of the analysis. |

## Sidebar tabs

**Main** contains the primary controls for the active page. **Extra**, **Text** and **Settings** provide additional controls or representations where available. A disabled tab has no available view in the current state.

The page views below introduce each enabled tab. Then follow [Example refinement](first-refinement.md) to build the analysis step by step.

## Selection and messages

Selecting a structure or experiment changes the model being inspected. The status bar reports the project state, messages and fitting progress. Read messages after importing data or when an operation is refused.
"""
    gallery = '\n## Page and sidebar views\n\nChoose **Overview** for the whole page. :lucide-monitor: marks a main-view tab; :material-dock-right: marks a sidebar tab. Only enabled tabs are shown. Analysis and Report show the completed refinement.\n'
    gallery += '\n### :material-home: Home\n\nStart an analysis, learn the interface through built-in tutorials, read about EasyDiffraction, open the documentation or get in touch.\n\n'
    gallery += figure(by_id['01-home'], view='workflow', description='Home overview')
    introductions = {
        'project': 'Create or open a project and keep its details together.',
        'structure': 'Inspect the crystal structure and edit its symmetry, cell and atom sites.',
        'experiment': 'Compare the measured pattern with the calculation and configure the measurement model.',
        'analysis': 'Choose parameters to refine, run the fit and inspect the pattern and parameter correlations.',
        'report': 'Review the results and choose what to include in an exported report.',
    }

    main_descriptions = {
        'project': {
            'Project': 'Read the project details, location, structures and experiments in one view.'
        },
        'structure': {
            'Structure': 'Inspect the selected crystal structure and its unit cell in the interactive view.'
        },
        'experiment': {
            'Pattern': 'Compare measured and calculated intensities, reflection marks and the residual pattern.'
        },
        'analysis': {
            'Pattern': 'Inspect the fitted pattern, residual and agreement factors for the selected experiment.',
            'Correlations': 'Inspect correlations between refined parameters to identify strongly coupled values.',
        },
        'report': {
            'Report': 'Read the report preview for the current model and results before exporting it.'
        },
    }
    sidebar_descriptions = {
        (
            'project',
            'Main',
        ): 'Create or open a project, browse built-in examples and return to recent work.',
        (
            'structure',
            'Main',
        ): 'Select a structure and edit its symmetry, cell, atom sites and displacement parameters.',
        (
            'experiment',
            'Main',
        ): 'Choose an experiment and edit its instrument, profile, background and linked structures.',
        (
            'analysis',
            'Main',
        ): 'Choose free parameters, inspect their values and bounds, and adjust the selected value.',
        (
            'report',
            'Main',
        ): 'Choose output formats, save locations and the sections included in the report.',
        (
            'project',
            'Extra',
        ): 'Choose how standard uncertainties are displayed in the project data.',
        ('structure', 'Extra'): 'Adjust the structure appearance and scattering-length settings.',
        (
            'experiment',
            'Extra',
        ): 'Configure intensity corrections, scattering sources and background estimation.',
        (
            'analysis',
            'Extra',
        ): 'Configure fitting modes, minimizers, parameter aliases and constraints.',
    }
    common_descriptions = {
        'Text': "Inspect or edit this page's project data in its text representation.",
        'Settings': 'Choose which parameters are shown and how the displayed pattern updates during a scan.',
    }
    for name in ['project', 'structure', 'experiment', 'analysis', 'report']:
        icon = {
            'project': 'archive',
            'structure': 'puzzle',
            'experiment': 'microscope',
            'analysis': 'calculator',
            'report': 'clipboard-text',
        }[name]
        gallery += f'\n### :material-{icon}: {name.title()}\n'
        modes = [scene for scene in scenes if scene['page'] == name and scene['sidebar']]
        base = modes[0]
        panes = [
            (
                'Overview',
                figure(
                    base,
                    view='workflow',
                    description=f'{name.title()} overview',
                    explanation=introductions[name],
                ),
            )
        ]
        tabs = sorted(
            (
                (key, item)
                for key, item in base['layout']['items'].items()
                if key.startswith(f'mainArea.{name}.tab.') and item['enabled']
            ),
            key=lambda pair: pair[1]['visible_bounds'][0],
        )
        for index, (key, item) in enumerate(tabs):
            selected = base
            if index:
                captures = [
                    by_id[action['scene']]
                    for action in manifest['actions']
                    if action['action'] == key and action['scene'] in by_id
                ]
                if not captures:
                    raise ValueError(f'Enabled main-view tab has no capture: {key}')
                selected = captures[-1]
            title = html.escape(item['label'])
            panes.append((
                f":lucide-monitor: <span class='gui-sr-only'>Main view: </span>{title}",
                figure(
                    selected,
                    view='main',
                    selection=key,
                    instance=key.rsplit('.', 1)[1],
                    description=f'{name.title()} — Main view: {item["label"]}',
                    explanation=main_descriptions[name].get(item['label'], introductions[name]),
                ),
            ))
        for scene in modes:
            panes.append((
                f":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>{scene['sidebar']}",
                figure(
                    scene,
                    view='sidebar',
                    description=f'{name.title()} — Sidebar: {scene["sidebar"]}',
                    explanation=sidebar_descriptions.get(
                        (name, scene['sidebar']),
                        common_descriptions.get(scene['sidebar'], introductions[name]),
                    ),
                ),
            ))
        gallery += viewer(panes)
    (DOCS / 'application/workspace.md').write_text(page('Application layout', workspace + gallery))
    if '15-project-examples' in by_id:
        examples = 'The web and desktop applications both include built-in example projects. Go to **Project**, select **Main** and expand **Examples**. Use the search and filters to find a case.\n\n'
        examples += figure(by_id['15-project-examples'])
        examples += '\nChoose a **Fitting** example to analyse measured data, or a **Simulation** example to inspect a calculated pattern. Examples open as working copies; use **Save project as…** to keep your changes.\n\nFor a guided analysis, follow [Example refinement](first-refinement.md). The shared [example catalogue](../user-guide/examples.md) describes the scientific cases.\n'
        (DOCS / 'application/examples.md').write_text(page('Example projects', examples))
    introduction = DOCS / 'application/index.md'
    text = introduction.read_text()
    text = re.sub(
        r'<figure class="gui-figure".*?</figure>',
        figure(by_id['13-analysis-basic'], instance='application-introduction').rstrip(),
        text,
        count=1,
        flags=re.DOTALL,
    )
    introduction.write_text(text)
    illustrate_guides(by_id)
    print(json.dumps({'imported': len(scenes), 'source': manifest['source_revision']}))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bundle', type=Path)
    render(parser.parse_args().bundle.resolve())


if __name__ == '__main__':
    main()
