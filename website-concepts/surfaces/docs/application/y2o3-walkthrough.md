---
template: gui.html
---

# Y₂O₃ on SPODI: a complete GUI walkthrough

Build a project from its separate inputs, refine the model and review the report. This example is **pd-neut-cwl_y2o3-spodi**, constant-wavelength neutron powder diffraction from SPODI at FRM II.

The screenshots below follow an actual application run at **1480 by 800 pixels**. Select a numbered explanation to highlight that part of the interface. The [page and sidebar reference](screen-reference.md) shows every enabled sidebar tab.

## Download the inputs

- [Y₂O₃ crystal structure](../assets/gui/y2o3/inputs/y2o3.edi)
- [SPODI experiment and measured intensities](../assets/gui/y2o3/inputs/spodi.edi)

The experiment input contains the measured pattern, instrument, profile, background and starting free parameters. Import these files separately; start with an empty project.

## Home

Open EasyDiffraction and press **Start**.

<figure class="gui-figure" data-gui-figure>
<svg class="gui-capture" viewBox="0 0 1480 800" role="img" aria-label="Start a new diffraction analysis"><title>Start a new diffraction analysis</title><image href="../assets/gui/y2o3/01-home.png" width="1480" height="800" /><rect class="is-active" data-gui-region="01-home-1" x="0.00" y="0.00" width="1480.00" height="77.00" /><rect class="" data-gui-region="01-home-2" x="0.00" y="77.00" width="1480.00" height="681.00" /><rect class="" data-gui-region="01-home-3" x="573.00" y="404.00" width="334.00" height="39.00" /></svg>
<figcaption>Start a new diffraction analysis. <a href="../assets/gui/y2o3/01-home.png">Open full-size screenshot</a></figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="01-home-1" aria-pressed="true">1. Workflow navigation</button> Move between Home, Project, Structure, Experiment, Analysis and Report.</li><li><button type="button" data-gui-target="01-home-2" aria-pressed="false">2. Main workspace</button> Inspect the home view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="01-home-3" aria-pressed="false">3. Start</button> Begin a new analysis on the Project page.</li></ol>
</figure>

## Create a project

Choose **Create a new project**.

<figure class="gui-figure" data-gui-figure>
<svg class="gui-capture" viewBox="0 0 1480 800" role="img" aria-label="Choose Create a new project"><title>Choose Create a new project</title><image href="../assets/gui/y2o3/02-project-start.png" width="1480" height="800" /><rect class="is-active" data-gui-region="02-project-start-1" x="784.00" y="168.00" width="334.00" height="39.00" /><rect class="" data-gui-region="02-project-start-2" x="770.00" y="119.00" width="710.00" height="155.00" /></svg>
<figcaption>Choose Create a new project. <a href="../assets/gui/y2o3/02-project-start.png">Open full-size screenshot</a></figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="02-project-start-1" aria-pressed="true">1. Create a new project</button> Open the project-details form.</li><li><button type="button" data-gui-target="02-project-start-2" aria-pressed="false">2. Project actions</button> Create a project or open an existing one.</li></ol>
</figure>

## Enter the project details

Enter the name **pd-neut-cwl_y2o3-spodi**, a title, authors and description. Choose a location on your computer, then confirm.

<figure class="gui-figure" data-gui-figure>
<svg class="gui-capture" viewBox="0 0 1480 800" role="img" aria-label="Enter the project details and choose its location"><title>Enter the project details and choose its location</title><image href="../assets/gui/y2o3/03-project-details.png" width="1480" height="800" /><rect class="is-active" data-gui-region="03-project-details-1" x="495.00" y="237.00" width="490.00" height="35.00" /><rect class="" data-gui-region="03-project-details-2" x="495.00" y="305.00" width="490.00" height="35.00" /><rect class="" data-gui-region="03-project-details-3" x="495.00" y="441.00" width="490.00" height="73.00" /><rect class="" data-gui-region="03-project-details-4" x="495.00" y="547.00" width="490.00" height="35.00" /></svg>
<figcaption>Enter the project details and choose its location. <a href="../assets/gui/y2o3/03-project-details.png">Open full-size screenshot</a></figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="03-project-details-1" aria-pressed="true">1. Name</button> Use a short project identifier.</li><li><button type="button" data-gui-target="03-project-details-2" aria-pressed="false">2. Title</button> Give the analysis a descriptive title.</li><li><button type="button" data-gui-target="03-project-details-3" aria-pressed="false">3. Description</button> Record the sample, measurement and purpose.</li><li><button type="button" data-gui-target="03-project-details-4" aria-pressed="false">4. Location</button> Choose where the project will be saved.</li></ol>
</figure>

## Inspect the project

The Project page keeps the analysis details together. The enabled sidebar tabs offer additional views of this state.

<figure class="gui-figure" data-gui-figure>
<svg class="gui-capture" viewBox="0 0 1480 800" role="img" aria-label="Create the project"><title>Create the project</title><image href="../assets/gui/y2o3/04-project-created.png" width="1480" height="800" /><rect class="is-active" data-gui-region="04-project-created-1" x="0.00" y="77.00" width="770.00" height="681.00" /><rect class="" data-gui-region="04-project-created-2" x="770.00" y="77.00" width="710.00" height="681.00" /></svg>
<figcaption>Create the project. <a href="../assets/gui/y2o3/04-project-created.png">Open full-size screenshot</a></figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="04-project-created-1" aria-pressed="true">1. Main workspace</button> Inspect the project view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="04-project-created-2" aria-pressed="false">2. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li></ol>
</figure>

## Load the structure

Open **Structure**, expand **Structures**, choose **Load** and select **y2o3.edi**.

<figure class="gui-figure" data-gui-figure>
<svg class="gui-capture" viewBox="0 0 1480 800" role="img" aria-label="Load the Y2O3 structure into the empty project"><title>Load the Y2O3 structure into the empty project</title><image href="../assets/gui/y2o3/06-structure-import.png" width="1480" height="800" /><rect class="is-active" data-gui-region="06-structure-import-1" x="784.00" y="260.00" width="334.00" height="39.00" /><rect class="" data-gui-region="06-structure-import-2" x="0.00" y="77.00" width="770.00" height="681.00" /></svg>
<figcaption>Load the Y2O3 structure into the empty project. <a href="../assets/gui/y2o3/06-structure-import.png">Open full-size screenshot</a></figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="06-structure-import-1" aria-pressed="true">1. Load structure</button> Import the separate y2o3.edi structure file.</li><li><button type="button" data-gui-target="06-structure-import-2" aria-pressed="false">2. Main workspace</button> Inspect the structure view here. Its content changes with the active page and selection.</li></ol>
</figure>

## Inspect the crystal structure

Inspect the cell, symmetry and atom sites. See [crystallography](../physics/crystallography.md) and [atomic displacement parameters](../physics/displacement.md) for their physical meaning.

<figure class="gui-figure" data-gui-figure>
<svg class="gui-capture" viewBox="0 0 1480 800" role="img" aria-label="Inspect the imported crystal structure"><title>Inspect the imported crystal structure</title><image href="../assets/gui/y2o3/07-structure-loaded.png" width="1480" height="800" /><rect class="is-active" data-gui-region="07-structure-loaded-1" x="784.00" y="168.00" width="682.00" height="78.00" /><rect class="" data-gui-region="07-structure-loaded-2" x="0.00" y="77.00" width="770.00" height="681.00" /></svg>
<figcaption>Inspect the imported crystal structure. <a href="../assets/gui/y2o3/07-structure-loaded.png">Open full-size screenshot</a></figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="07-structure-loaded-1" aria-pressed="true">1. Structures</button> Select the structure whose cell and atom sites you want to inspect.</li><li><button type="button" data-gui-target="07-structure-loaded-2" aria-pressed="false">2. Main workspace</button> Inspect the structure view here. Its content changes with the active page and selection.</li></ol>
</figure>

## Load the experiment

Open **Experiment**, expand **Experiments**, choose **Load** and select **spodi.edi**.

<figure class="gui-figure" data-gui-figure>
<svg class="gui-capture" viewBox="0 0 1480 800" role="img" aria-label="Load the SPODI experiment and measured intensities"><title>Load the SPODI experiment and measured intensities</title><image href="../assets/gui/y2o3/09-experiment-import.png" width="1480" height="800" /><rect class="is-active" data-gui-region="09-experiment-import-1" x="784.00" y="260.00" width="218.00" height="39.00" /><rect class="" data-gui-region="09-experiment-import-2" x="0.00" y="77.00" width="770.00" height="681.00" /></svg>
<figcaption>Load the SPODI experiment and measured intensities. <a href="../assets/gui/y2o3/09-experiment-import.png">Open full-size screenshot</a></figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="09-experiment-import-1" aria-pressed="true">1. Load experiment</button> Import spodi.edi, including its measured intensities and instrument settings.</li><li><button type="button" data-gui-target="09-experiment-import-2" aria-pressed="false">2. Main workspace</button> Inspect the experiment view here. Its content changes with the active page and selection.</li></ol>
</figure>

## Inspect the initial pattern

Compare the measured and calculated intensities before fitting. Review the [peak profile](../physics/profiles/cw.md), [background](../physics/background.md), reflection marks and residual.

<figure class="gui-figure" data-gui-figure>
<svg class="gui-capture" viewBox="0 0 1480 800" role="img" aria-label="Compare the measured pattern with the initial calculation"><title>Compare the measured pattern with the initial calculation</title><image href="../assets/gui/y2o3/10-experiment-loaded.png" width="1480" height="800" /><rect class="is-active" data-gui-region="10-experiment-loaded-1" x="0.00" y="77.00" width="770.00" height="681.00" /><rect class="" data-gui-region="10-experiment-loaded-2" x="770.00" y="77.00" width="710.00" height="681.00" /></svg>
<figcaption>Compare the measured pattern with the initial calculation. <a href="../assets/gui/y2o3/10-experiment-loaded.png">Open full-size screenshot</a></figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="10-experiment-loaded-1" aria-pressed="true">1. Main workspace</button> Inspect the experiment view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="10-experiment-loaded-2" aria-pressed="false">2. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li></ol>
</figure>

## Refine the model

Open **Analysis**, inspect the free parameters and press **Fit**. Wait for fitting to finish, review the result and close the results popup. This screenshot shows the completed fit with that popup closed. See [Rietveld refinement](../physics/rietveld.md), [uncertainties](../physics/minimization.md) and [reliability factors](../physics/reliability.md).

<figure class="gui-figure" data-gui-figure>
<svg class="gui-capture" viewBox="0 0 1480 800" role="img" aria-label="Completed Rietveld refinement — Main"><title>Completed Rietveld refinement — Main</title><image href="../assets/gui/y2o3/13-analysis-basic.png" width="1480" height="800" /><rect class="is-active" data-gui-region="13-analysis-basic-1" x="0.00" y="0.00" width="1480.00" height="77.00" /><rect class="" data-gui-region="13-analysis-basic-2" x="0.00" y="77.00" width="770.00" height="681.00" /><rect class="" data-gui-region="13-analysis-basic-3" x="770.00" y="77.00" width="710.00" height="681.00" /><rect class="" data-gui-region="13-analysis-basic-4" x="0.00" y="758.00" width="1480.00" height="42.00" /></svg>
<figcaption>Completed Rietveld refinement — Main. <a href="../assets/gui/y2o3/13-analysis-basic.png">Open full-size screenshot</a></figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="13-analysis-basic-1" aria-pressed="true">1. Workflow navigation</button> Move between Home, Project, Structure, Experiment, Analysis and Report.</li><li><button type="button" data-gui-target="13-analysis-basic-2" aria-pressed="false">2. Main workspace</button> Inspect the analysis view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="13-analysis-basic-3" aria-pressed="false">3. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="13-analysis-basic-4" aria-pressed="false">4. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
</figure>

## Review the report

Open **Report** to review the structure, measurement and fitted results. Use the sidebar to choose the report contents and export format.

<figure class="gui-figure" data-gui-figure>
<svg class="gui-capture" viewBox="0 0 1480 800" role="img" aria-label="Review the fitted structure and report — Main"><title>Review the fitted structure and report — Main</title><image href="../assets/gui/y2o3/14-report-basic.png" width="1480" height="800" /><rect class="is-active" data-gui-region="14-report-basic-1" x="0.00" y="0.00" width="1480.00" height="77.00" /><rect class="" data-gui-region="14-report-basic-2" x="0.00" y="77.00" width="770.00" height="681.00" /><rect class="" data-gui-region="14-report-basic-3" x="770.00" y="77.00" width="710.00" height="681.00" /><rect class="" data-gui-region="14-report-basic-4" x="0.00" y="758.00" width="1480.00" height="42.00" /></svg>
<figcaption>Review the fitted structure and report — Main. <a href="../assets/gui/y2o3/14-report-basic.png">Open full-size screenshot</a></figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="14-report-basic-1" aria-pressed="true">1. Workflow navigation</button> Move between Home, Project, Structure, Experiment, Analysis and Report.</li><li><button type="button" data-gui-target="14-report-basic-2" aria-pressed="false">2. Main workspace</button> Inspect the report view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="14-report-basic-3" aria-pressed="false">3. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="14-report-basic-4" aria-pressed="false">4. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
</figure>

## All page and sidebar views

Continue to the [screen reference](screen-reference.md) for every enabled tab, or [find your way around the workspace](workspace.md).
