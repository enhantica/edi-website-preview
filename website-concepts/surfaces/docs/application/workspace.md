---
template: gui.html
---

# Application layout

The interface follows the same analysis workflow as the [User guide](../user-guide/analysis-workflow/index.md). The top bar selects a page, the central workspace shows its main view, and the sidebar contains the related controls.

## Main regions

The arrows show how to follow the workflow and read the controls. Select an explanation below to highlight a region. The example shows **Analysis after fitting**, with the results popup closed.

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Completed Rietveld refinement — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Completed Rietveld refinement — Main"><title>Completed Rietveld refinement — Main</title><defs><clipPath id="gui-clip-13-analysis-basic-layout"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-layout)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-layout-1" data-gui-parts="[[0,0,1480,77]]" d="M-2.000 -2.000 L1482.000 -2.000 L1482.000 79.000 L-2.000 79.000 Z" /><path class="is-active" data-gui-region="13-analysis-basic-layout-2" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="is-active" data-gui-region="13-analysis-basic-layout-3" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="is-active" data-gui-region="13-analysis-basic-layout-4" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /><path class="gui-direction is-active" data-gui-direction d="M573.72 26.18 L882.10 26.18 L882.10 13.86 L906.74 38.50 L882.10 63.14 L882.10 50.82 L573.72 50.82 Z" aria-hidden="true" /><path class="gui-direction is-active" data-gui-direction d="M1270.55 158.72 L1306.05 158.72 L1306.05 640.78 L1323.80 640.78 L1288.30 676.28 L1252.80 640.78 L1270.55 640.78 Z" aria-hidden="true" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-overview aria-pressed="true">Layout overview</button> Follow the workflow from left to right, then the sidebar from top to bottom.</li><li><button type="button" data-gui-target="13-analysis-basic-layout-1" aria-pressed="false">1. Workflow navigation</button> Move between Home, Project, Structure, Experiment, Analysis and Report.</li><li><button type="button" data-gui-target="13-analysis-basic-layout-2" aria-pressed="false">2. Main workspace</button> Inspect the analysis view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="13-analysis-basic-layout-3" aria-pressed="false">3. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="13-analysis-basic-layout-4" aria-pressed="false">4. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
</figure>

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

## Page and sidebar views

Choose **Overview** for the whole page. :material-dock-left: marks a main-view tab; :material-dock-right: marks a sidebar tab. Only enabled tabs are shown. Analysis and Report show the completed refinement.

### :material-home: Home

Start an analysis, learn the interface through built-in tutorials, read about EasyDiffraction, open the documentation or get in touch.

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/01-home.png?v=0206c48d32c4" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Home overview"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Home overview"><title>Home overview</title><defs><clipPath id="gui-clip-01-home-workflow"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/01-home.png?v=0206c48d32c4" width="1480" height="800" clip-path="url(#gui-clip-01-home-workflow)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="01-home-workflow-1" data-gui-parts="[[0,77,1480,681],[542,0,53.46875,77]]" d="M-2.000 75.000 L540.000 75.000 L540.000 -2.000 L597.469 -2.000 L597.469 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>

</figure>

### :material-archive: Project

Create or open a project and keep its details together.

=== "Overview"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/05-project-basic.png?v=faf8e7a87764" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Project overview"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Project overview"><title>Project overview</title><defs><clipPath id="gui-clip-05-project-basic-workflow"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/05-project-basic.png?v=faf8e7a87764" width="1480" height="800" clip-path="url(#gui-clip-05-project-basic-workflow)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="05-project-basic-workflow-1" data-gui-parts="[[0,77,1480,681],[595.46875,0,59.734375,77]]" d="M-2.000 75.000 L593.469 75.000 L593.469 -2.000 L657.203 -2.000 L657.203 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-left: <span class='gui-sr-only'>Main view: </span>Project"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/05-project-basic.png?v=faf8e7a87764" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Project — Main view: Project"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Project — Main view: Project"><title>Project — Main view: Project</title><defs><clipPath id="gui-clip-05-project-basic-main-description"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/05-project-basic.png?v=faf8e7a87764" width="1480" height="800" clip-path="url(#gui-clip-05-project-basic-main-description)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="05-project-basic-main-description-1" data-gui-parts="[[0,119,770,639],[0,77,55.734375,42]]" d="M-2.000 117.000 L-2.000 117.000 L-2.000 75.000 L57.734 75.000 L57.734 117.000 L772.000 117.000 L772.000 760.000 L-2.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Main"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/05-project-basic.png?v=faf8e7a87764" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Project — Sidebar: Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Project — Sidebar: Main"><title>Project — Sidebar: Main</title><defs><clipPath id="gui-clip-05-project-basic-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/05-project-basic.png?v=faf8e7a87764" width="1480" height="800" clip-path="url(#gui-clip-05-project-basic-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="05-project-basic-sidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Extra"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/05-project-extras.png?v=6c05237cf72f" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Project — Sidebar: Extra"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Project — Sidebar: Extra"><title>Project — Sidebar: Extra</title><defs><clipPath id="gui-clip-05-project-extras-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/05-project-extras.png?v=6c05237cf72f" width="1480" height="800" clip-path="url(#gui-clip-05-project-extras-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="05-project-extras-sidebar-1" data-gui-parts="[[770,119,710,639],[813.40625,77,45.359375,42]]" d="M768.000 117.000 L811.406 117.000 L811.406 75.000 L860.766 75.000 L860.766 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Text"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/05-project-text.png?v=c84b4e47c467" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Project — Sidebar: Text"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Project — Sidebar: Text"><title>Project — Sidebar: Text</title><defs><clipPath id="gui-clip-05-project-text-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/05-project-text.png?v=c84b4e47c467" width="1480" height="800" clip-path="url(#gui-clip-05-project-text-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="05-project-text-sidebar-1" data-gui-parts="[[770,119,710,639],[858.53125,77,39.171875,42]]" d="M768.000 117.000 L856.531 117.000 L856.531 75.000 L899.703 75.000 L899.703 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

### :material-puzzle: Structure

Inspect the crystal structure and edit its symmetry, cell and atom sites.

=== "Overview"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/08-structure-basic.png?v=3ba62a04504a" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Structure overview"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Structure overview"><title>Structure overview</title><defs><clipPath id="gui-clip-08-structure-basic-workflow"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/08-structure-basic.png?v=3ba62a04504a" width="1480" height="800" clip-path="url(#gui-clip-08-structure-basic-workflow)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="08-structure-basic-workflow-1" data-gui-parts="[[0,77,1480,681],[655.203125,0,72.25,77]]" d="M-2.000 75.000 L653.203 75.000 L653.203 -2.000 L729.453 -2.000 L729.453 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-left: <span class='gui-sr-only'>Main view: </span>Structure"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/08-structure-basic.png?v=3ba62a04504a" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Structure — Main view: Structure"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Structure — Main view: Structure"><title>Structure — Main view: Structure</title><defs><clipPath id="gui-clip-08-structure-basic-main-view"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/08-structure-basic.png?v=3ba62a04504a" width="1480" height="800" clip-path="url(#gui-clip-08-structure-basic-main-view)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="08-structure-basic-main-view-1" data-gui-parts="[[0,119,770,639],[0,77,69.1875,42]]" d="M-2.000 117.000 L-2.000 117.000 L-2.000 75.000 L71.188 75.000 L71.188 117.000 L772.000 117.000 L772.000 760.000 L-2.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Main"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/08-structure-basic.png?v=3ba62a04504a" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Structure — Sidebar: Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Structure — Sidebar: Main"><title>Structure — Sidebar: Main</title><defs><clipPath id="gui-clip-08-structure-basic-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/08-structure-basic.png?v=3ba62a04504a" width="1480" height="800" clip-path="url(#gui-clip-08-structure-basic-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="08-structure-basic-sidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Extra"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/08-structure-extras.png?v=71aebe4a84dd" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Structure — Sidebar: Extra"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Structure — Sidebar: Extra"><title>Structure — Sidebar: Extra</title><defs><clipPath id="gui-clip-08-structure-extras-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/08-structure-extras.png?v=71aebe4a84dd" width="1480" height="800" clip-path="url(#gui-clip-08-structure-extras-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="08-structure-extras-sidebar-1" data-gui-parts="[[770,119,710,639],[813.40625,77,45.359375,42]]" d="M768.000 117.000 L811.406 117.000 L811.406 75.000 L860.766 75.000 L860.766 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Text"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/08-structure-text.png?v=40fe1ac312d6" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Structure — Sidebar: Text"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Structure — Sidebar: Text"><title>Structure — Sidebar: Text</title><defs><clipPath id="gui-clip-08-structure-text-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/08-structure-text.png?v=40fe1ac312d6" width="1480" height="800" clip-path="url(#gui-clip-08-structure-text-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="08-structure-text-sidebar-1" data-gui-parts="[[770,119,710,639],[858.53125,77,39.171875,42]]" d="M768.000 117.000 L856.531 117.000 L856.531 75.000 L899.703 75.000 L899.703 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

### :material-microscope: Experiment

Compare the measured pattern with the calculation and configure the measurement model.

=== "Overview"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/11-experiment-basic.png?v=7f83aefad735" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Experiment overview"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Experiment overview"><title>Experiment overview</title><defs><clipPath id="gui-clip-11-experiment-basic-workflow"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/11-experiment-basic.png?v=7f83aefad735" width="1480" height="800" clip-path="url(#gui-clip-11-experiment-basic-workflow)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="11-experiment-basic-workflow-1" data-gui-parts="[[0,77,1480,681],[727.453125,0,84.90625,77]]" d="M-2.000 75.000 L725.453 75.000 L725.453 -2.000 L814.359 -2.000 L814.359 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-left: <span class='gui-sr-only'>Main view: </span>Pattern"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/11-experiment-basic.png?v=7f83aefad735" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Experiment — Main view: Pattern"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Experiment — Main view: Pattern"><title>Experiment — Main view: Pattern</title><defs><clipPath id="gui-clip-11-experiment-basic-main-chart"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/11-experiment-basic.png?v=7f83aefad735" width="1480" height="800" clip-path="url(#gui-clip-11-experiment-basic-main-chart)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="11-experiment-basic-main-chart-1" data-gui-parts="[[0,119,770,639],[0,77,57.765625,42]]" d="M-2.000 117.000 L-2.000 117.000 L-2.000 75.000 L59.766 75.000 L59.766 117.000 L772.000 117.000 L772.000 760.000 L-2.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Main"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/11-experiment-basic.png?v=7f83aefad735" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Experiment — Sidebar: Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Experiment — Sidebar: Main"><title>Experiment — Sidebar: Main</title><defs><clipPath id="gui-clip-11-experiment-basic-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/11-experiment-basic.png?v=7f83aefad735" width="1480" height="800" clip-path="url(#gui-clip-11-experiment-basic-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="11-experiment-basic-sidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Extra"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/11-experiment-extras.png?v=2d6620cbc61a" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Experiment — Sidebar: Extra"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Experiment — Sidebar: Extra"><title>Experiment — Sidebar: Extra</title><defs><clipPath id="gui-clip-11-experiment-extras-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/11-experiment-extras.png?v=2d6620cbc61a" width="1480" height="800" clip-path="url(#gui-clip-11-experiment-extras-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="11-experiment-extras-sidebar-1" data-gui-parts="[[770,119,710,639],[813.40625,77,45.359375,42]]" d="M768.000 117.000 L811.406 117.000 L811.406 75.000 L860.766 75.000 L860.766 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Text"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/11-experiment-text.png?v=6cdf84888c54" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Experiment — Sidebar: Text"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Experiment — Sidebar: Text"><title>Experiment — Sidebar: Text</title><defs><clipPath id="gui-clip-11-experiment-text-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/11-experiment-text.png?v=6cdf84888c54" width="1480" height="800" clip-path="url(#gui-clip-11-experiment-text-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="11-experiment-text-sidebar-1" data-gui-parts="[[770,119,710,639],[858.53125,77,39.171875,42]]" d="M768.000 117.000 L856.531 117.000 L856.531 75.000 L899.703 75.000 L899.703 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

### :material-calculator: Analysis

Choose parameters to refine, run the fit and inspect the pattern and parameter correlations.

=== "Overview"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Analysis overview"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Analysis overview"><title>Analysis overview</title><defs><clipPath id="gui-clip-13-analysis-basic-workflow"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-workflow)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-workflow-1" data-gui-parts="[[0,77,1480,681],[812.359375,0,67.84375,77]]" d="M-2.000 75.000 L810.359 75.000 L810.359 -2.000 L882.203 -2.000 L882.203 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-left: <span class='gui-sr-only'>Main view: </span>Pattern"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Analysis — Main view: Pattern"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Analysis — Main view: Pattern"><title>Analysis — Main view: Pattern</title><defs><clipPath id="gui-clip-13-analysis-basic-main-fitting"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-main-fitting)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-main-fitting-1" data-gui-parts="[[0,119,770,639],[0,77,57.765625,42]]" d="M-2.000 117.000 L-2.000 117.000 L-2.000 75.000 L59.766 75.000 L59.766 117.000 L772.000 117.000 L772.000 760.000 L-2.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-left: <span class='gui-sr-only'>Main view: </span>Correlations"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/guide-analysis-correlations.png?v=b4b4015fae4d" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Analysis — Main view: Correlations"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Analysis — Main view: Correlations"><title>Analysis — Main view: Correlations</title><defs><clipPath id="gui-clip-guide-analysis-correlations-main-correlations"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-analysis-correlations.png?v=b4b4015fae4d" width="1480" height="800" clip-path="url(#gui-clip-guide-analysis-correlations-main-correlations)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-analysis-correlations-main-correlations-1" data-gui-parts="[[0,119,770,639],[57.09375,77,86.484375,42]]" d="M-2.000 117.000 L55.094 117.000 L55.094 75.000 L145.578 75.000 L145.578 117.000 L772.000 117.000 L772.000 760.000 L-2.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Main"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Analysis — Sidebar: Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Analysis — Sidebar: Main"><title>Analysis — Sidebar: Main</title><defs><clipPath id="gui-clip-13-analysis-basic-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-sidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Extra"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-extras.png?v=0b6d798e7cb1" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Analysis — Sidebar: Extra"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Analysis — Sidebar: Extra"><title>Analysis — Sidebar: Extra</title><defs><clipPath id="gui-clip-13-analysis-extras-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-extras.png?v=0b6d798e7cb1" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-extras-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-extras-sidebar-1" data-gui-parts="[[770,119,710,639],[813.40625,77,45.359375,42]]" d="M768.000 117.000 L811.406 117.000 L811.406 75.000 L860.766 75.000 L860.766 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Text"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-text.png?v=05a78e18aec2" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Analysis — Sidebar: Text"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Analysis — Sidebar: Text"><title>Analysis — Sidebar: Text</title><defs><clipPath id="gui-clip-13-analysis-text-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-text.png?v=05a78e18aec2" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-text-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-text-sidebar-1" data-gui-parts="[[770,119,710,639],[858.53125,77,39.171875,42]]" d="M768.000 117.000 L856.531 117.000 L856.531 75.000 L899.703 75.000 L899.703 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Settings"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-settings.png?v=a6abd57c8bda" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Analysis — Sidebar: Settings"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Analysis — Sidebar: Settings"><title>Analysis — Sidebar: Settings</title><defs><clipPath id="gui-clip-13-analysis-settings-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-settings.png?v=a6abd57c8bda" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-settings-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-settings-sidebar-1" data-gui-parts="[[770,119,710,639],[897.21875,77,62.96875,42]]" d="M768.000 117.000 L895.219 117.000 L895.219 75.000 L962.188 75.000 L962.188 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

### :material-clipboard-text: Report

Review the results and choose what to include in an exported report.

=== "Overview"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/14-report-basic.png?v=1a34e2660cbe" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Report overview"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Report overview"><title>Report overview</title><defs><clipPath id="gui-clip-14-report-basic-workflow"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/14-report-basic.png?v=1a34e2660cbe" width="1480" height="800" clip-path="url(#gui-clip-14-report-basic-workflow)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="14-report-basic-workflow-1" data-gui-parts="[[0,77,1480,681],[880.203125,0,58.25,77]]" d="M-2.000 75.000 L878.203 75.000 L878.203 -2.000 L940.453 -2.000 L940.453 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-left: <span class='gui-sr-only'>Main view: </span>Report"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/14-report-basic.png?v=1a34e2660cbe" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Report — Main view: Report"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Report — Main view: Report"><title>Report — Main view: Report</title><defs><clipPath id="gui-clip-14-report-basic-main-report"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/14-report-basic.png?v=1a34e2660cbe" width="1480" height="800" clip-path="url(#gui-clip-14-report-basic-main-report)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="14-report-basic-main-report-1" data-gui-parts="[[0,119,770,639],[0,77,54.125,42]]" d="M-2.000 117.000 L-2.000 117.000 L-2.000 75.000 L56.125 75.000 L56.125 117.000 L772.000 117.000 L772.000 760.000 L-2.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Main"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/14-report-basic.png?v=1a34e2660cbe" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Report — Sidebar: Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Report — Sidebar: Main"><title>Report — Sidebar: Main</title><defs><clipPath id="gui-clip-14-report-basic-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/14-report-basic.png?v=1a34e2660cbe" width="1480" height="800" clip-path="url(#gui-clip-14-report-basic-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="14-report-basic-sidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>

=== ":material-dock-right: <span class='gui-sr-only'>Sidebar: </span>Text"

    <figure class="gui-figure" data-gui-figure>
    <a class="gui-image-link" href="../assets/gui/y2o3/14-report-text.png?v=676889b4f03a" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Report — Sidebar: Text"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Report — Sidebar: Text"><title>Report — Sidebar: Text</title><defs><clipPath id="gui-clip-14-report-text-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/14-report-text.png?v=676889b4f03a" width="1480" height="800" clip-path="url(#gui-clip-14-report-text-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="14-report-text-sidebar-1" data-gui-parts="[[770,119,710,639],[858.53125,77,39.171875,42]]" d="M768.000 117.000 L856.531 117.000 L856.531 75.000 L899.703 75.000 L899.703 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>

    </figure>
