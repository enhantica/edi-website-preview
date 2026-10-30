#!/usr/bin/env python3
"""Import a validated native walkthrough and generate its illustrated documentation."""

from __future__ import annotations

import argparse
import html
import json
import shutil
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
    'group.getStarted': ('Project actions', 'Create a project or open an existing one.'),
    'createProject.name': ('Name', 'Use a short project identifier.'),
    'createProject.title': ('Title', 'Give the analysis a descriptive title.'),
    'createProject.description': ('Description', 'Record the sample, measurement and purpose.'),
    'createProject.location': ('Location', 'Choose where the project will be saved.'),
    'structures.load': ('Load structure', 'Import the separate y2o3.edi structure file.'),
    'structures.list': (
        'Structures',
        'Select the structure whose cell and atom sites you want to inspect.',
    ),
    'experiments.load': (
        'Load experiment',
        'Import spodi.edi, including its measured intensities and instrument settings.',
    ),
}


def label(target: str, page: str) -> tuple[str, str]:
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
    return LABELS.get(target, (target, ''))


def region_parts(meta: dict, target: str) -> list[list[float]]:
    """Join a sidebar's active tab to its body using this capture's Qt bounds."""
    if target.endswith('.page'):
        name = target.split('.')[1]
        main = meta['items'][f'workflow.{name}.mainContent']['visible_bounds']
        sidebar = meta['items'][f'workflow.{name}.manualSidebar']['visible_bounds']
        tab = meta['items'][f'appBar.tab.{name}']['visible_bounds']
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


def figure(scene: dict, *, view: str = 'overview') -> str:
    meta = scene['layout']
    image = '../assets/gui/y2o3/' + scene['image']
    description = html.escape(scene['description'], quote=True)
    identity = f'{scene["id"]}-{view}'
    targets = (
        [f'workflow.{scene["page"]}.manualSidebar'] if view == 'sidebar' else meta['highlights']
    )
    if view == 'sidebar':
        targets.append(f'workflow.{scene["page"]}.page')
    paths, buttons = [], []
    for number, target in enumerate(targets, 1):
        parts = region_parts(meta, target)
        title, text = label(target, scene['page'])
        key = f'{identity}-{number}'
        data = html.escape(json.dumps(parts, separators=(',', ':')), quote=True)
        paths.append(
            f'<path class="{"is-active" if number == 1 or view == "layout" else ""}" data-gui-region="{key}" '
            f'data-gui-parts="{data}" d="{region_path(parts)}" />'
        )
        buttons.append(
            f'<li><button type="button" data-gui-target="{key}" aria-pressed="{"true" if number == 1 and view != "layout" else "false"}">'
            f'{number}. {html.escape(title)}</button> {html.escape(text)}</li>'
        )
    if view == 'sidebar':
        buttons = [
            f'<button type="button" class="gui-region-choice" data-gui-target="{identity}-1" aria-pressed="true">Tab and panel</button>',
            f'<button type="button" class="gui-region-choice" data-gui-target="{identity}-2" aria-pressed="false">Workflow page</button>',
        ]
        controls = (
            '<div class="gui-view-options" role="group" aria-label="Highlight">'
            + ''.join(buttons)
            + '</div>'
        )
    else:
        overview = (
            '<li><button type="button" data-gui-overview aria-pressed="true">Layout overview</button> Follow the workflow from left to right, then the sidebar from top to bottom.</li>'
            if view == 'layout'
            else ''
        )
        controls = '<ol class="gui-regions">' + overview + ''.join(buttons) + '</ol>'
    arrows = ''
    if view == 'layout':
        for axis, name in [
            ('x', 'appBar.workflow'),
            ('y', f'workflow.{scene["page"]}.manualSidebar'),
        ]:
            x, y, width, height = meta['items'][name]['visible_bounds']
            if axis == 'x':
                start, end, centre, half = (
                    x + width * 0.08,
                    x + width * 0.92,
                    y + height * 0.5,
                    height * 0.16,
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
                start, end, centre, half = (
                    y + height * 0.12,
                    y + height * 0.88,
                    x + width * 0.73,
                    width * 0.025,
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
            arrows += f'<path class="gui-direction is-active" data-gui-direction d="{data}" aria-hidden="true" />'
    clip = f'gui-clip-{identity}'
    return (
        '<figure class="gui-figure" data-gui-figure>\n'
        f'<a class="gui-image-link" href="{image}" data-gui-open aria-haspopup="dialog" '
        f'aria-label="Enlarge screenshot: {description}">'
        f'<svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="{description}">'
        f'<title>{description}</title><defs><clipPath id="{clip}"><rect width="1480" height="800" rx="12" /></clipPath></defs>'
        f'<image href="{image}" width="1480" height="800" clip-path="url(#{clip})" />'
        '<rect class="gui-image-frame" width="1480" height="800" rx="12" />'
        + ''.join(paths)
        + arrows
        + '</svg></a>\n'
        f'<figcaption>{description}.</figcaption>\n' + controls + '\n</figure>\n'
    )


def page(title: str, body: str) -> str:
    return f'---\ntemplate: gui.html\n---\n\n# {title}\n\n{body.rstrip()}\n'


def render(bundle: Path) -> None:
    manifest, scenes = validate_bundle(bundle)
    by_id = {scene['id']: scene for scene in scenes}
    destination = DOCS / 'assets/gui/y2o3'
    destination.mkdir(parents=True, exist_ok=True)
    artifacts = {'manifest.json', 'walkthrough.js'}
    artifacts.update(item['file'] for item in manifest['inputs'].values())
    for scene in scenes:
        artifacts.update((scene['image'], scene['metadata']))
    for artifact in sorted(artifacts):
        target = destination / artifact
        target.parent.mkdir(parents=True, exist_ok=True)
        if (bundle / artifact).resolve() != target.resolve():
            shutil.copy2(bundle / artifact, target)
    intro = """Build a project from its separate inputs, refine the model and review the report. This example is **pd-neut-cwl_y2o3-spodi**, constant-wavelength neutron powder diffraction from SPODI at FRM II.

The screenshots below follow an actual application run at **1480 by 800 pixels**. Select a numbered explanation to highlight that part of the interface. The [application layout](workspace.md) introduces the workspace and every enabled sidebar tab.

## Download the inputs

- [Y₂O₃ crystal structure](../assets/gui/y2o3/inputs/y2o3.edi)
- [SPODI experiment and measured intensities](../assets/gui/y2o3/inputs/spodi.edi)

The experiment input contains the measured pattern, instrument, profile, background and starting free parameters. Import these files separately; start with an empty project.
"""
    sections = [
        ('Home', 'Open EasyDiffraction and press **Start**.', '01-home'),
        ('Create a project', 'Choose **Create a new project**.', '02-project-start'),
        (
            'Enter the project details',
            'Enter the name **pd-neut-cwl_y2o3-spodi**, a title, authors and description. Choose a location on your computer, then confirm.',
            '03-project-details',
        ),
        (
            'Inspect the project',
            'The Project page keeps the analysis details together. The enabled sidebar tabs offer additional views of this state.',
            '04-project-created',
        ),
        (
            'Load the structure',
            'Open **Structure**, expand **Structures**, choose **Load** and select **y2o3.edi**.',
            '06-structure-import',
        ),
        (
            'Inspect the crystal structure',
            'Inspect the cell, symmetry and atom sites. See [crystallography](../physics/crystallography.md) and [atomic displacement parameters](../physics/displacement.md) for their physical meaning.',
            '07-structure-loaded',
        ),
        (
            'Load the experiment',
            'Open **Experiment**, expand **Experiments**, choose **Load** and select **spodi.edi**.',
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

The arrows show how to follow the workflow and read the controls. Select an explanation below to highlight a region. The example shows **Analysis after fitting**, with the results popup closed.

"""
    workspace += figure(by_id['13-analysis-basic'], view='layout')
    workspace += """
## Workflow pages

| Page | What you do here |
| --- | --- |
| Home | Start an analysis. |
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
    gallery = '\n## Page and sidebar views\n\nThese views come from the same Y₂O₃/SPODI walkthrough. Every enabled sidebar tab is shown. Select **Workflow page** to see how its toolbar tab connects to the whole page. All **Analysis** and **Report** views were captured after the fit completed and its results popup was closed.\n'
    for name in ['project', 'structure', 'experiment', 'analysis', 'report']:
        gallery += f'\n### {name.title()}\n'
        for scene in scenes:
            if scene['page'] == name and scene['sidebar']:
                gallery += f'\n#### {scene["sidebar"]}\n\n' + figure(scene, view='sidebar')
    gallery += '\n## Capture provenance\n\n'
    gallery += f'App source: [`{manifest["source_revision"][:8]}`](https://github.com/enhantica/edi/commit/{manifest["source_revision"]}). '
    gallery += 'Image dimensions, native page/sidebar/fit state and annotation geometry are recorded in the [capture manifest](../assets/gui/y2o3/manifest.json) and matching JSON sidecars. The [JavaScript walkthrough](../assets/gui/y2o3/walkthrough.js) drives the run.\n'
    (DOCS / 'application/workspace.md').write_text(page('Application layout', workspace + gallery))
    if '15-project-examples' in by_id:
        examples = 'The web and desktop applications both include built-in example projects. Go to **Project**, select **Main** and expand **Examples**. Use the search and filters to find a case.\n\n'
        examples += figure(by_id['15-project-examples'])
        examples += '\nChoose a **Fitting** example to analyse measured data, or a **Simulation** example to inspect a calculated pattern. Examples open as working copies; use **Save project as…** to keep your changes.\n\nFor a guided analysis, follow [Example refinement](first-refinement.md). The shared [example catalogue](../user-guide/examples.md) describes the scientific cases.\n'
        (DOCS / 'application/examples.md').write_text(page('Example projects', examples))
    print(json.dumps({'imported': len(scenes), 'source': manifest['source_revision']}))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bundle', type=Path)
    render(parser.parse_args().bundle.resolve())


if __name__ == '__main__':
    main()
