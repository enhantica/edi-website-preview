---
template: gui.html
---

# Find your way around

The interface follows the same analysis workflow as the [User guide](../user-guide/analysis-workflow/index.md). The top bar selects a page, the central workspace shows its main view, and the sidebar contains the related controls.

## Main regions

Select an explanation below the screenshot to highlight the corresponding region. The example shows **Analysis after fitting**, with the results popup closed.

<figure class="gui-figure" data-gui-figure>
<svg class="gui-capture" viewBox="0 0 1480 800" role="img" aria-label="Completed Rietveld refinement — Main"><title>Completed Rietveld refinement — Main</title><image href="../assets/gui/y2o3/13-analysis-basic.png" width="1480" height="800" /><rect class="is-active" data-gui-region="13-analysis-basic-1" x="0.00" y="0.00" width="1480.00" height="77.00" /><rect class="" data-gui-region="13-analysis-basic-2" x="0.00" y="77.00" width="770.00" height="681.00" /><rect class="" data-gui-region="13-analysis-basic-3" x="770.00" y="77.00" width="710.00" height="681.00" /><rect class="" data-gui-region="13-analysis-basic-4" x="0.00" y="758.00" width="1480.00" height="42.00" /></svg>
<figcaption>Completed Rietveld refinement — Main. <a href="../assets/gui/y2o3/13-analysis-basic.png">Open full-size screenshot</a></figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="13-analysis-basic-1" aria-pressed="true">1. Workflow navigation</button> Move between Home, Project, Structure, Experiment, Analysis and Report.</li><li><button type="button" data-gui-target="13-analysis-basic-2" aria-pressed="false">2. Main workspace</button> Inspect the analysis view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="13-analysis-basic-3" aria-pressed="false">3. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="13-analysis-basic-4" aria-pressed="false">4. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
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

See the [screen reference](screen-reference.md) for each enabled tab, or follow the [Y₂O₃ walkthrough](y2o3-walkthrough.md) to build the analysis step by step.

## Selection and messages

Selecting a structure or experiment changes the model being inspected. The status bar reports the project state, messages and fitting progress. Read messages after importing data or when an operation is refused.
