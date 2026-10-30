---
template: gui.html
---

# The application

Use the EasyDiffraction application to build a crystallographic model, compare calculated and measured diffraction data, refine parameters, and prepare a report. The desktop and browser applications share the same visual workspace and project model.

[Open the web app](https://enhantica.github.io/edi/webapp/){ .md-button .md-button--primary }
[Explore the application layout](workspace.md){ .md-button }

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Completed Rietveld refinement — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Completed Rietveld refinement — Main"><title>Completed Rietveld refinement — Main</title><defs><clipPath id="gui-clip-13-analysis-basic-overview-application-introduction"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-overview-application-introduction)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-overview-application-introduction-1" data-gui-parts="[[0,0,1480,77]]" d="M-2.000 -2.000 L1482.000 -2.000 L1482.000 79.000 L-2.000 79.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-application-introduction-2" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-application-introduction-3" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-application-introduction-4" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /></svg></a>
<figcaption>Completed Rietveld refinement — Main.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="13-analysis-basic-overview-application-introduction-1" aria-pressed="true">1. Workflow navigation</button> Move between Home, Project, Structure, Experiment, Analysis and Report.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-application-introduction-2" aria-pressed="false">2. Main workspace</button> Inspect the analysis view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-application-introduction-3" aria-pressed="false">3. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-application-introduction-4" aria-pressed="false">4. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
</figure>


## Start here

Use the [browser application](browser.md) or [set up the desktop application](desktop.md). Read [Application layout](workspace.md) to learn the controls and workflow, then follow [Example refinement](first-refinement.md).

## A workflow you can follow

The pages across the top follow **Project → Structure → Experiment → Analysis → Report**. You can return to an earlier page whenever your model needs attention.

| Page | What you do there |
| --- | --- |
| [Project](projects.md) | Open an example or a saved project, and decide where to keep your work. |
| [Structure](structures.md) | Load or create crystal structures, then edit symmetry, cell and atom sites. |
| [Experiment](experiments.md) | Load measured data and describe the instrument, profile, background and linked structures. |
| [Analysis](refine.md) | Choose free parameters, select the fitting mode and inspect the result. |
| [Report](reports.md) | Review and save a document containing your model and results. |

## Start with an example or your own data

An included example provides structures, experiments and starting conditions together. It is a useful first step if you want to understand the controls before preparing input files.

To use your own measurement, [create a new project](new-project.md), add a structure, create an experiment and load its data. You can also open a complete existing project.

## Desktop and browser

The scientific workflow is the same. File handling depends on where the application runs:

- [Desktop](desktop.md) works directly with project folders and zip archives on your computer.
- [Browser](browser.md) supports local file access in Chrome and Edge. Other browser workflows use browser storage and downloadable project copies.

## Use the same project elsewhere

The project also opens in [Python](../python/index.md) and through the [command line](../cli/index.md). Shared explanations belong in [User guide](../user-guide/index.md); these pages focus on the application's controls.
