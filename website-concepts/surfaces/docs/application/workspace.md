---
template: gui.html
---

# Application layout

The interface follows the same analysis workflow as the [User guide](../user-guide/analysis-workflow/index.md). The top bar selects a page, the central workspace shows its main view, and the sidebar contains the related controls.

## Main regions

The arrows show how to follow the workflow and read the controls. Select an explanation below to highlight a region. The example shows **Analysis after fitting**, with the results popup closed.

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Completed Rietveld refinement — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Completed Rietveld refinement — Main"><title>Completed Rietveld refinement — Main</title><defs><clipPath id="gui-clip-13-analysis-basic-layout"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-layout)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-layout-1" data-gui-parts="[[0,0,1480,77]]" d="M-2.000 -2.000 L1482.000 -2.000 L1482.000 79.000 L-2.000 79.000 Z" /><path class="is-active" data-gui-region="13-analysis-basic-layout-2" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="is-active" data-gui-region="13-analysis-basic-layout-3" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="is-active" data-gui-region="13-analysis-basic-layout-4" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /><path class="gui-direction is-active" data-gui-direction d="M573.72 26.18 L882.10 26.18 L882.10 13.86 L906.74 38.50 L882.10 63.14 L882.10 50.82 L573.72 50.82 Z" aria-hidden="true" /><path class="gui-direction is-active" data-gui-direction d="M1270.55 158.72 L1306.05 158.72 L1306.05 640.78 L1323.80 640.78 L1288.30 676.28 L1252.80 640.78 L1270.55 640.78 Z" aria-hidden="true" /></svg></a>
<figcaption>Completed Rietveld refinement — Main.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-overview aria-pressed="true">Layout overview</button> Follow the workflow from left to right, then the sidebar from top to bottom.</li><li><button type="button" data-gui-target="13-analysis-basic-layout-1" aria-pressed="false">1. Workflow navigation</button> Move between Home, Project, Structure, Experiment, Analysis and Report.</li><li><button type="button" data-gui-target="13-analysis-basic-layout-2" aria-pressed="false">2. Main workspace</button> Inspect the analysis view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="13-analysis-basic-layout-3" aria-pressed="false">3. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="13-analysis-basic-layout-4" aria-pressed="false">4. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
</figure>

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

## Page and sidebar views

These views come from the same Y₂O₃/SPODI walkthrough. Every enabled sidebar tab is shown. Select **Workflow page** to see how its toolbar tab connects to the whole page. All **Analysis** and **Report** views were captured after the fit completed and its results popup was closed.

### Project

#### Main

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/05-project-basic.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Project details and controls — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Project details and controls — Main"><title>Project details and controls — Main</title><defs><clipPath id="gui-clip-05-project-basic-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/05-project-basic.png" width="1480" height="800" clip-path="url(#gui-clip-05-project-basic-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="05-project-basic-sidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="05-project-basic-sidebar-2" data-gui-parts="[[0,77,1480,681],[595.46875,0,59.734375,77]]" d="M-2.000 75.000 L593.469 75.000 L593.469 -2.000 L657.203 -2.000 L657.203 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>Project details and controls — Main.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="05-project-basic-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="05-project-basic-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

#### Extra

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/05-project-extras.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Project details and controls — Extra"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Project details and controls — Extra"><title>Project details and controls — Extra</title><defs><clipPath id="gui-clip-05-project-extras-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/05-project-extras.png" width="1480" height="800" clip-path="url(#gui-clip-05-project-extras-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="05-project-extras-sidebar-1" data-gui-parts="[[770,119,710,639],[813.40625,77,45.359375,42]]" d="M768.000 117.000 L811.406 117.000 L811.406 75.000 L860.766 75.000 L860.766 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="05-project-extras-sidebar-2" data-gui-parts="[[0,77,1480,681],[595.46875,0,59.734375,77]]" d="M-2.000 75.000 L593.469 75.000 L593.469 -2.000 L657.203 -2.000 L657.203 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>Project details and controls — Extra.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="05-project-extras-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="05-project-extras-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

#### Text

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/05-project-text.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Project details and controls — Text"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Project details and controls — Text"><title>Project details and controls — Text</title><defs><clipPath id="gui-clip-05-project-text-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/05-project-text.png" width="1480" height="800" clip-path="url(#gui-clip-05-project-text-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="05-project-text-sidebar-1" data-gui-parts="[[770,119,710,639],[858.53125,77,39.171875,42]]" d="M768.000 117.000 L856.531 117.000 L856.531 75.000 L899.703 75.000 L899.703 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="05-project-text-sidebar-2" data-gui-parts="[[0,77,1480,681],[595.46875,0,59.734375,77]]" d="M-2.000 75.000 L593.469 75.000 L593.469 -2.000 L657.203 -2.000 L657.203 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>Project details and controls — Text.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="05-project-text-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="05-project-text-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

### Structure

#### Main

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/08-structure-basic.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Crystal structure — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Crystal structure — Main"><title>Crystal structure — Main</title><defs><clipPath id="gui-clip-08-structure-basic-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/08-structure-basic.png" width="1480" height="800" clip-path="url(#gui-clip-08-structure-basic-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="08-structure-basic-sidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="08-structure-basic-sidebar-2" data-gui-parts="[[0,77,1480,681],[655.203125,0,72.25,77]]" d="M-2.000 75.000 L653.203 75.000 L653.203 -2.000 L729.453 -2.000 L729.453 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>Crystal structure — Main.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="08-structure-basic-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="08-structure-basic-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

#### Extra

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/08-structure-extras.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Crystal structure — Extra"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Crystal structure — Extra"><title>Crystal structure — Extra</title><defs><clipPath id="gui-clip-08-structure-extras-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/08-structure-extras.png" width="1480" height="800" clip-path="url(#gui-clip-08-structure-extras-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="08-structure-extras-sidebar-1" data-gui-parts="[[770,119,710,639],[813.40625,77,45.359375,42]]" d="M768.000 117.000 L811.406 117.000 L811.406 75.000 L860.766 75.000 L860.766 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="08-structure-extras-sidebar-2" data-gui-parts="[[0,77,1480,681],[655.203125,0,72.25,77]]" d="M-2.000 75.000 L653.203 75.000 L653.203 -2.000 L729.453 -2.000 L729.453 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>Crystal structure — Extra.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="08-structure-extras-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="08-structure-extras-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

#### Text

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/08-structure-text.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Crystal structure — Text"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Crystal structure — Text"><title>Crystal structure — Text</title><defs><clipPath id="gui-clip-08-structure-text-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/08-structure-text.png" width="1480" height="800" clip-path="url(#gui-clip-08-structure-text-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="08-structure-text-sidebar-1" data-gui-parts="[[770,119,710,639],[858.53125,77,39.171875,42]]" d="M768.000 117.000 L856.531 117.000 L856.531 75.000 L899.703 75.000 L899.703 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="08-structure-text-sidebar-2" data-gui-parts="[[0,77,1480,681],[655.203125,0,72.25,77]]" d="M-2.000 75.000 L653.203 75.000 L653.203 -2.000 L729.453 -2.000 L729.453 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>Crystal structure — Text.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="08-structure-text-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="08-structure-text-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

### Experiment

#### Main

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/11-experiment-basic.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: SPODI experiment — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="SPODI experiment — Main"><title>SPODI experiment — Main</title><defs><clipPath id="gui-clip-11-experiment-basic-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/11-experiment-basic.png" width="1480" height="800" clip-path="url(#gui-clip-11-experiment-basic-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="11-experiment-basic-sidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="11-experiment-basic-sidebar-2" data-gui-parts="[[0,77,1480,681],[727.453125,0,84.90625,77]]" d="M-2.000 75.000 L725.453 75.000 L725.453 -2.000 L814.359 -2.000 L814.359 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>SPODI experiment — Main.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="11-experiment-basic-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="11-experiment-basic-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

#### Extra

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/11-experiment-extras.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: SPODI experiment — Extra"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="SPODI experiment — Extra"><title>SPODI experiment — Extra</title><defs><clipPath id="gui-clip-11-experiment-extras-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/11-experiment-extras.png" width="1480" height="800" clip-path="url(#gui-clip-11-experiment-extras-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="11-experiment-extras-sidebar-1" data-gui-parts="[[770,119,710,639],[813.40625,77,45.359375,42]]" d="M768.000 117.000 L811.406 117.000 L811.406 75.000 L860.766 75.000 L860.766 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="11-experiment-extras-sidebar-2" data-gui-parts="[[0,77,1480,681],[727.453125,0,84.90625,77]]" d="M-2.000 75.000 L725.453 75.000 L725.453 -2.000 L814.359 -2.000 L814.359 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>SPODI experiment — Extra.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="11-experiment-extras-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="11-experiment-extras-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

#### Text

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/11-experiment-text.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: SPODI experiment — Text"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="SPODI experiment — Text"><title>SPODI experiment — Text</title><defs><clipPath id="gui-clip-11-experiment-text-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/11-experiment-text.png" width="1480" height="800" clip-path="url(#gui-clip-11-experiment-text-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="11-experiment-text-sidebar-1" data-gui-parts="[[770,119,710,639],[858.53125,77,39.171875,42]]" d="M768.000 117.000 L856.531 117.000 L856.531 75.000 L899.703 75.000 L899.703 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="11-experiment-text-sidebar-2" data-gui-parts="[[0,77,1480,681],[727.453125,0,84.90625,77]]" d="M-2.000 75.000 L725.453 75.000 L725.453 -2.000 L814.359 -2.000 L814.359 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>SPODI experiment — Text.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="11-experiment-text-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="11-experiment-text-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

### Analysis

#### Main

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Completed Rietveld refinement — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Completed Rietveld refinement — Main"><title>Completed Rietveld refinement — Main</title><defs><clipPath id="gui-clip-13-analysis-basic-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-sidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-sidebar-2" data-gui-parts="[[0,77,1480,681],[812.359375,0,67.84375,77]]" d="M-2.000 75.000 L810.359 75.000 L810.359 -2.000 L882.203 -2.000 L882.203 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>Completed Rietveld refinement — Main.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="13-analysis-basic-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="13-analysis-basic-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

#### Extra

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-extras.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Completed Rietveld refinement — Extra"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Completed Rietveld refinement — Extra"><title>Completed Rietveld refinement — Extra</title><defs><clipPath id="gui-clip-13-analysis-extras-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-extras.png" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-extras-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-extras-sidebar-1" data-gui-parts="[[770,119,710,639],[813.40625,77,45.359375,42]]" d="M768.000 117.000 L811.406 117.000 L811.406 75.000 L860.766 75.000 L860.766 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="13-analysis-extras-sidebar-2" data-gui-parts="[[0,77,1480,681],[812.359375,0,67.84375,77]]" d="M-2.000 75.000 L810.359 75.000 L810.359 -2.000 L882.203 -2.000 L882.203 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>Completed Rietveld refinement — Extra.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="13-analysis-extras-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="13-analysis-extras-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

#### Text

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-text.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Completed Rietveld refinement — Text"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Completed Rietveld refinement — Text"><title>Completed Rietveld refinement — Text</title><defs><clipPath id="gui-clip-13-analysis-text-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-text.png" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-text-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-text-sidebar-1" data-gui-parts="[[770,119,710,639],[858.53125,77,39.171875,42]]" d="M768.000 117.000 L856.531 117.000 L856.531 75.000 L899.703 75.000 L899.703 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="13-analysis-text-sidebar-2" data-gui-parts="[[0,77,1480,681],[812.359375,0,67.84375,77]]" d="M-2.000 75.000 L810.359 75.000 L810.359 -2.000 L882.203 -2.000 L882.203 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>Completed Rietveld refinement — Text.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="13-analysis-text-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="13-analysis-text-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

#### Settings

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-settings.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Completed Rietveld refinement — Settings"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Completed Rietveld refinement — Settings"><title>Completed Rietveld refinement — Settings</title><defs><clipPath id="gui-clip-13-analysis-settings-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-settings.png" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-settings-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-settings-sidebar-1" data-gui-parts="[[770,119,710,639],[897.21875,77,62.96875,42]]" d="M768.000 117.000 L895.219 117.000 L895.219 75.000 L962.188 75.000 L962.188 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="13-analysis-settings-sidebar-2" data-gui-parts="[[0,77,1480,681],[812.359375,0,67.84375,77]]" d="M-2.000 75.000 L810.359 75.000 L810.359 -2.000 L882.203 -2.000 L882.203 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>Completed Rietveld refinement — Settings.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="13-analysis-settings-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="13-analysis-settings-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

### Report

#### Main

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/14-report-basic.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Review the fitted structure and report — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Review the fitted structure and report — Main"><title>Review the fitted structure and report — Main</title><defs><clipPath id="gui-clip-14-report-basic-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/14-report-basic.png" width="1480" height="800" clip-path="url(#gui-clip-14-report-basic-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="14-report-basic-sidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="14-report-basic-sidebar-2" data-gui-parts="[[0,77,1480,681],[880.203125,0,58.25,77]]" d="M-2.000 75.000 L878.203 75.000 L878.203 -2.000 L940.453 -2.000 L940.453 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>Review the fitted structure and report — Main.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="14-report-basic-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="14-report-basic-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

#### Text

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/14-report-text.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Review the fitted structure and report — Text"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Review the fitted structure and report — Text"><title>Review the fitted structure and report — Text</title><defs><clipPath id="gui-clip-14-report-text-sidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/14-report-text.png" width="1480" height="800" clip-path="url(#gui-clip-14-report-text-sidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="14-report-text-sidebar-1" data-gui-parts="[[770,119,710,639],[858.53125,77,39.171875,42]]" d="M768.000 117.000 L856.531 117.000 L856.531 75.000 L899.703 75.000 L899.703 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="14-report-text-sidebar-2" data-gui-parts="[[0,77,1480,681],[880.203125,0,58.25,77]]" d="M-2.000 75.000 L878.203 75.000 L878.203 -2.000 L940.453 -2.000 L940.453 75.000 L1482.000 75.000 L1482.000 760.000 L-2.000 760.000 Z" /></svg></a>
<figcaption>Review the fitted structure and report — Text.</figcaption>
<div class="gui-view-options" role="group" aria-label="Highlight"><button type="button" class="gui-region-choice" data-gui-target="14-report-text-sidebar-1" aria-pressed="true">Tab and panel</button><button type="button" class="gui-region-choice" data-gui-target="14-report-text-sidebar-2" aria-pressed="false">Workflow page</button></div>
</figure>

## Capture provenance

App source: [`8996a2b6`](https://github.com/enhantica/edi/commit/8996a2b6093bd51fb153b5c815638d6f644df705). Image dimensions, native page/sidebar/fit state and annotation geometry are recorded in the [capture manifest](../assets/gui/y2o3/manifest.json) and matching JSON sidecars. The [JavaScript walkthrough](../assets/gui/y2o3/walkthrough.js) drives the run.
