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
    return LABELS.get(target, (target, ''))


def figure(scene: dict, *, annotations: bool = True) -> str:
    meta = scene['layout']
    image = '../../assets/gui/y2o3/' + scene['image']
    description = html.escape(scene['description'], quote=True)
    identity = scene['id']
    targets = meta['highlights'] if annotations else []
    rects, buttons = [], []
    for number, target in enumerate(targets, 1):
        x, y, width, height = meta['items'][target]['visible_bounds']
        title, text = label(target, scene['page'])
        key = f'{identity}-{number}'
        rects.append(
            f'<rect data-gui-region="{key}" x="{x:.2f}" y="{y:.2f}" width="{width:.2f}" height="{height:.2f}" />'
        )
        buttons.append(
            f'<li><button type="button" data-gui-target="{key}" aria-pressed="false">'
            f'{number}. {html.escape(title)}</button> {html.escape(text)}</li>'
        )
    controls = '<ol class="gui-regions">' + ''.join(buttons) + '</ol>' if targets else ''
    return (
        '<figure class="gui-figure" data-gui-figure>\n'
        f'<svg class="gui-capture" viewBox="0 0 1480 800" role="img" aria-label="{description}">'
        f'<title>{description}</title><image href="{image}" width="1480" height="800" />'
        + ''.join(rects)
        + '</svg>\n'
        f'<figcaption>{description}. <a href="{image}">Open full-size screenshot</a></figcaption>\n'
        + controls
        + '\n</figure>\n'
    )


def page(title: str, body: str) -> str:
    return f'---\ntemplate: gui.html\n---\n\n# {title}\n\n{body}\n'


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

The screenshots below follow an actual application run at **1480 by 800 pixels**. Select a numbered explanation to highlight that part of the interface. The [page and sidebar reference](screen-reference.md) shows every enabled sidebar tab.

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
    body += '\n## All page and sidebar views\n\nContinue to the [screen reference](screen-reference.md) for every enabled tab, or [find your way around the workspace](workspace.md).\n'
    (DOCS / 'application/y2o3-walkthrough.md').write_text(
        page('Y₂O₃ on SPODI: a complete GUI walkthrough', body)
    )
    workspace = """The interface follows the same analysis workflow as the [User guide](../user-guide/analysis-workflow/index.md). The top bar selects a page, the central workspace shows its main view, and the sidebar contains the related controls.

## Main regions

Select an explanation below the screenshot to highlight the corresponding region. The example shows **Analysis after fitting**, with the results popup closed.

"""
    workspace += figure(by_id['13-analysis-basic'])
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

See the [screen reference](screen-reference.md) for each enabled tab, or follow the [Y₂O₃ walkthrough](y2o3-walkthrough.md) to build the analysis step by step.

## Selection and messages

Selecting a structure or experiment changes the model being inspected. The status bar reports the project state, messages and fitting progress. Read messages after importing data or when an operation is refused.
"""
    (DOCS / 'application/workspace.md').write_text(page('Find your way around', workspace))
    gallery = 'These views come from the same Y₂O₃/SPODI walkthrough. Every enabled sidebar tab is shown. All **Analysis** and **Report** views were captured after the fit completed and its results popup was closed.\n'
    for name in ['project', 'structure', 'experiment', 'analysis', 'report']:
        gallery += f'\n## {name.title()}\n'
        for scene in scenes:
            if scene['page'] == name and scene['sidebar']:
                gallery += f'\n### {scene["sidebar"]}\n\n' + figure(scene, annotations=False)
    gallery += '\n## Capture provenance\n\n'
    gallery += f'App source: [`{manifest["source_revision"][:8]}`](https://github.com/enhantica/edi/commit/{manifest["source_revision"]}). '
    gallery += 'Image dimensions, native page/sidebar/fit state and annotation geometry are recorded in the [capture manifest](../assets/gui/y2o3/manifest.json) and matching JSON sidecars. The [JavaScript walkthrough](../assets/gui/y2o3/walkthrough.js) drives the run.\n'
    (DOCS / 'application/screen-reference.md').write_text(
        page('Page and sidebar reference', gallery)
    )
    (DOCS / 'application/first-refinement.md').write_text("""# Your first refinement

Follow the [illustrated Y₂O₃/SPODI walkthrough](y2o3-walkthrough.md) to create a project, import its structure and experiment, run a refinement and review the report.

For an overview of the controls, see [the workspace](workspace.md). The [page and sidebar reference](screen-reference.md) shows each enabled sidebar tab.
""")
    print(json.dumps({'imported': len(scenes), 'source': manifest['source_revision']}))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bundle', type=Path)
    render(parser.parse_args().bundle.resolve())


if __name__ == '__main__':
    main()
