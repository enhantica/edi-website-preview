---
template: gui.html
---

# Example refinement

Build a project from its separate inputs, refine the model and review the report. This example is **pd-neut-cwl_y2o3-spodi**: Y₂O₃ [Ia-3], SPODI @ FRM II.

Select a numbered explanation to highlight that part of the interface. The [application layout](workspace.md) introduces the workspace and every enabled sidebar tab.

## Download the inputs

- [Crystal structure: y2o3.edi](../assets/gui/y2o3/inputs/structures/y2o3.edi)
- [Experiment and measured intensities: spodi.edi](../assets/gui/y2o3/inputs/experiments/spodi.edi)

The experiment input contains the measured pattern, instrument, profile, background and starting free parameters. Import these files separately; start with an empty project.

## Home

Open EasyDiffraction and press **Start**.

<figure class="gui-figure" data-gui-figure>
<figcaption>Start a new diffraction analysis.</figcaption>
<a class="gui-image-link" href="../assets/gui/y2o3/01-home.png?v=0206c48d32c4" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Start a new diffraction analysis"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Start a new diffraction analysis"><title>Start a new diffraction analysis</title><defs><clipPath id="gui-clip-01-home-overview"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/01-home.png?v=0206c48d32c4" width="1480" height="800" clip-path="url(#gui-clip-01-home-overview)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="01-home-overview-1" data-gui-parts="[[573,404,334,39]]" d="M571.000 402.000 L909.000 402.000 L909.000 445.000 L571.000 445.000 Z" /><path data-gui-navigation data-gui-parts="[[542,0,53.46875,77]]" d="M540.000 -2.000 L597.469 -2.000 L597.469 79.000 L540.000 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="01-home-overview-1" aria-pressed="true">1. <span class="gui-fa" aria-hidden="true">&#61749;</span>Start</button> Begin a new analysis on the Project page.</li></ol>
</figure>

## Create a project

Choose **Create a new project**.

<figure class="gui-figure" data-gui-figure>
<figcaption>Choose Create a new project.</figcaption>
<a class="gui-image-link" href="../assets/gui/y2o3/02-project-start.png?v=42cd79e8ba8a" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Choose Create a new project"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Choose Create a new project"><title>Choose Create a new project</title><defs><clipPath id="gui-clip-02-project-start-overview"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/02-project-start.png?v=42cd79e8ba8a" width="1480" height="800" clip-path="url(#gui-clip-02-project-start-overview)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="02-project-start-overview-1" data-gui-parts="[[784,168,334,39]]" d="M782.000 166.000 L1120.000 166.000 L1120.000 209.000 L782.000 209.000 Z" /><path class="" data-gui-region="02-project-start-overview-2" data-gui-parts="[[770,119,710,155]]" d="M768.000 117.000 L1482.000 117.000 L1482.000 276.000 L768.000 276.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="02-project-start-overview-1" aria-pressed="true">1. <span class="gui-fa" aria-hidden="true">&#61525;</span>Create a new project</button> Open the project-details form.</li><li><button type="button" data-gui-target="02-project-start-overview-2" aria-pressed="false">2. <span class="gui-fa" aria-hidden="true">&#61749;</span>Get started</button> Create a project or open an existing one.</li></ol>
</figure>

## Enter the project details

Enter a name, title, authors and description for the analysis. Choose a location on your computer, then confirm.

<figure class="gui-figure" data-gui-figure>
<figcaption>Enter the project details and choose its location.</figcaption>
<a class="gui-image-link" href="../assets/gui/y2o3/03-project-details.png?v=5760dd5f3f61" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Enter the project details and choose its location"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Enter the project details and choose its location"><title>Enter the project details and choose its location</title><defs><clipPath id="gui-clip-03-project-details-overview"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/03-project-details.png?v=5760dd5f3f61" width="1480" height="800" clip-path="url(#gui-clip-03-project-details-overview)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="03-project-details-overview-1" data-gui-parts="[[495,237,490,35]]" d="M493.000 235.000 L987.000 235.000 L987.000 274.000 L493.000 274.000 Z" /><path class="" data-gui-region="03-project-details-overview-2" data-gui-parts="[[495,305,490,35]]" d="M493.000 303.000 L987.000 303.000 L987.000 342.000 L493.000 342.000 Z" /><path class="" data-gui-region="03-project-details-overview-3" data-gui-parts="[[495,441,490,73]]" d="M493.000 439.000 L987.000 439.000 L987.000 516.000 L493.000 516.000 Z" /><path class="" data-gui-region="03-project-details-overview-4" data-gui-parts="[[495,547,490,35]]" d="M493.000 545.000 L987.000 545.000 L987.000 584.000 L493.000 584.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="03-project-details-overview-1" aria-pressed="true">1. Name</button> Use a short project identifier.</li><li><button type="button" data-gui-target="03-project-details-overview-2" aria-pressed="false">2. Title</button> Give the analysis a descriptive title.</li><li><button type="button" data-gui-target="03-project-details-overview-3" aria-pressed="false">3. Description</button> Record the sample, measurement and purpose.</li><li><button type="button" data-gui-target="03-project-details-overview-4" aria-pressed="false">4. Location</button> Choose where the project will be saved.</li></ol>
</figure>

## Inspect the project

The Project page keeps the analysis details together. The enabled sidebar tabs offer additional views of this state.

<figure class="gui-figure" data-gui-figure>
<figcaption>Create the project.</figcaption>
<a class="gui-image-link" href="../assets/gui/y2o3/04-project-created.png?v=faf8e7a87764" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Create the project"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Create the project"><title>Create the project</title><defs><clipPath id="gui-clip-04-project-created-overview"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/04-project-created.png?v=faf8e7a87764" width="1480" height="800" clip-path="url(#gui-clip-04-project-created-overview)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="04-project-created-overview-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="04-project-created-overview-2" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="04-project-created-overview-1" aria-pressed="true">1. Main workspace</button> Inspect the project view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="04-project-created-overview-2" aria-pressed="false">2. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li></ol>
</figure>

## Load the structure

Open **Structure**, expand **Structures**, choose **Load** and select **y2o3.edi**.

<figure class="gui-figure" data-gui-figure>
<figcaption>Load the structure into the empty project.</figcaption>
<a class="gui-image-link" href="../assets/gui/y2o3/06-structure-import.png?v=b0460a0fb5f3" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Load the structure into the empty project"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Load the structure into the empty project"><title>Load the structure into the empty project</title><defs><clipPath id="gui-clip-06-structure-import-overview"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/06-structure-import.png?v=b0460a0fb5f3" width="1480" height="800" clip-path="url(#gui-clip-06-structure-import-overview)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="06-structure-import-overview-1" data-gui-parts="[[784,260,334,39]]" d="M782.000 258.000 L1120.000 258.000 L1120.000 301.000 L782.000 301.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="06-structure-import-overview-1" aria-pressed="true">1. <span class="gui-fa" aria-hidden="true">&#61587;</span>Load structure</button> Import the structure file for this example.</li></ol>
</figure>

## Inspect the crystal structure

Inspect the cell, symmetry and atom sites. See [crystallography](../physics/crystallography.md) and [atomic displacement parameters](../physics/displacement.md) for their physical meaning.

<figure class="gui-figure" data-gui-figure>
<figcaption>Inspect the imported crystal structure.</figcaption>
<a class="gui-image-link" href="../assets/gui/y2o3/07-structure-loaded.png?v=3ba62a04504a" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Inspect the imported crystal structure"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Inspect the imported crystal structure"><title>Inspect the imported crystal structure</title><defs><clipPath id="gui-clip-07-structure-loaded-overview"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/07-structure-loaded.png?v=3ba62a04504a" width="1480" height="800" clip-path="url(#gui-clip-07-structure-loaded-overview)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="07-structure-loaded-overview-1" data-gui-parts="[[784,168,682,78]]" d="M782.000 166.000 L1468.000 166.000 L1468.000 248.000 L782.000 248.000 Z" /><path class="" data-gui-region="07-structure-loaded-overview-2" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="07-structure-loaded-overview-1" aria-pressed="true">1. Structures</button> Select the structure whose cell and atom sites you want to inspect.</li><li><button type="button" data-gui-target="07-structure-loaded-overview-2" aria-pressed="false">2. Main workspace</button> Inspect the structure view here. Its content changes with the active page and selection.</li></ol>
</figure>

## Load the experiment

Open **Experiment**, expand **Experiments**, choose **Load** and select **spodi.edi**.

<figure class="gui-figure" data-gui-figure>
<figcaption>Load the experiment and measured intensities.</figcaption>
<a class="gui-image-link" href="../assets/gui/y2o3/09-experiment-import.png?v=70b91676e98e" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Load the experiment and measured intensities"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Load the experiment and measured intensities"><title>Load the experiment and measured intensities</title><defs><clipPath id="gui-clip-09-experiment-import-overview"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/09-experiment-import.png?v=70b91676e98e" width="1480" height="800" clip-path="url(#gui-clip-09-experiment-import-overview)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="09-experiment-import-overview-1" data-gui-parts="[[784,260,218,39]]" d="M782.000 258.000 L1004.000 258.000 L1004.000 301.000 L782.000 301.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="09-experiment-import-overview-1" aria-pressed="true">1. <span class="gui-fa" aria-hidden="true">&#61587;</span>Load experiment</button> Import the experiment file, including measured intensities and instrument settings.</li></ol>
</figure>

## Inspect the initial pattern

Compare the measured and calculated intensities before fitting. Review the [peak profile](../physics/profiles/cw.md), [background](../physics/background.md), reflection marks and residual.

<figure class="gui-figure" data-gui-figure>
<figcaption>Compare the measured pattern with the initial calculation.</figcaption>
<a class="gui-image-link" href="../assets/gui/y2o3/10-experiment-loaded.png?v=7f83aefad735" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Compare the measured pattern with the initial calculation"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Compare the measured pattern with the initial calculation"><title>Compare the measured pattern with the initial calculation</title><defs><clipPath id="gui-clip-10-experiment-loaded-overview"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/10-experiment-loaded.png?v=7f83aefad735" width="1480" height="800" clip-path="url(#gui-clip-10-experiment-loaded-overview)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="10-experiment-loaded-overview-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="10-experiment-loaded-overview-2" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="10-experiment-loaded-overview-1" aria-pressed="true">1. Main workspace</button> Inspect the experiment view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="10-experiment-loaded-overview-2" aria-pressed="false">2. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li></ol>
</figure>

## Refine the model

Open **Analysis**, inspect the free parameters and press **Fit**. Wait for fitting to finish, review the result and close the results popup. This screenshot shows the completed fit with that popup closed. See [Rietveld refinement](../physics/rietveld.md), [uncertainties](../physics/minimization.md) and [reliability factors](../physics/reliability.md).

<figure class="gui-figure" data-gui-figure>
<figcaption>Completed Rietveld refinement — Main.</figcaption>
<a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Completed Rietveld refinement — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Completed Rietveld refinement — Main"><title>Completed Rietveld refinement — Main</title><defs><clipPath id="gui-clip-13-analysis-basic-overview"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-overview)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-overview-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-2" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-3" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /><path data-gui-navigation data-gui-parts="[[812.359375,0,67.84375,77]]" d="M810.359 -2.000 L882.203 -2.000 L882.203 79.000 L810.359 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="13-analysis-basic-overview-1" aria-pressed="true">1. Main workspace</button> Inspect the analysis view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-2" aria-pressed="false">2. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-3" aria-pressed="false">3. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
</figure>

## Review the report

Open **Report** to review the structure, measurement and fitted results. Use the sidebar to choose the report contents and export format.

<figure class="gui-figure" data-gui-figure>
<figcaption>Review the fitted structure and report — Main.</figcaption>
<a class="gui-image-link" href="../assets/gui/y2o3/14-report-basic.png?v=1a34e2660cbe" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Review the fitted structure and report — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Review the fitted structure and report — Main"><title>Review the fitted structure and report — Main</title><defs><clipPath id="gui-clip-14-report-basic-overview"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/14-report-basic.png?v=1a34e2660cbe" width="1480" height="800" clip-path="url(#gui-clip-14-report-basic-overview)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="14-report-basic-overview-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="14-report-basic-overview-2" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="14-report-basic-overview-3" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /><path data-gui-navigation data-gui-parts="[[880.203125,0,58.25,77]]" d="M878.203 -2.000 L940.453 -2.000 L940.453 79.000 L878.203 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="14-report-basic-overview-1" aria-pressed="true">1. Main workspace</button> Inspect the report view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="14-report-basic-overview-2" aria-pressed="false">2. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="14-report-basic-overview-3" aria-pressed="false">3. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
</figure>

## Explore the workspace

See [Application layout](workspace.md) for an annotated overview of every workflow page and its enabled sidebar tabs.
