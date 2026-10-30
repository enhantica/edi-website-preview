---
template: gui.html
---

# Example refinement

Build a project from its separate inputs, refine the model and review the report. This example is **pd-neut-cwl_y2o3-spodi**: Y₂O₃ [Ia-3], SPODI @ FRM II.

Use the tabs to highlight parts of the interface. The [application layout](workspace.md) introduces the workspace and every enabled sidebar tab.

## Download the inputs

- [Crystal structure: y2o3.edi](../assets/gui/y2o3/inputs/structures/y2o3.edi)
- [Experiment and measured intensities: spodi.edi](../assets/gui/y2o3/inputs/experiments/spodi.edi)

The experiment input contains the measured pattern, instrument, profile, background and starting free parameters. Import these files separately; start with an empty project.

## Home

Open EasyDiffraction and press **Start**.

<div class="gui-viewer" markdown="1">

<figure class="gui-figure" data-gui-figure>
<p class="gui-view-description">Begin a new analysis on the Project page.</p>
<a class="gui-image-link" href="../assets/gui/y2o3/01-home.png?v=f6bbed100d8c" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Start"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Start"><title>Start</title><defs><clipPath id="gui-clip-01-home-overview-home-start"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/01-home.png?v=f6bbed100d8c" width="1480" height="800" clip-path="url(#gui-clip-01-home-overview-home-start)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="01-home-overview-home-start-1" data-gui-parts="[[573,404,334,39]]" d="M571.000 402.000 L909.000 402.000 L909.000 445.000 L571.000 445.000 Z" /><path data-gui-navigation data-gui-parts="[[542,0,53.46875,77]]" d="M540.000 -2.000 L597.469 -2.000 L597.469 79.000 L540.000 79.000 Z" /></svg></a>

</figure>

</div>

## Create a project

Choose **Create a new project**.

<div class="gui-viewer" markdown="1">


=== "<span class='gui-fa' aria-hidden='true'>&#61525;</span>Create a new project"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Open the project-details form.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/02-project-start.png?v=743fcb18ce5e" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Create a new project"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Create a new project"><title>Create a new project</title><defs><clipPath id="gui-clip-02-project-start-overview-project-create"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/02-project-start.png?v=743fcb18ce5e" width="1480" height="800" clip-path="url(#gui-clip-02-project-start-overview-project-create)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="02-project-start-overview-project-create-1" data-gui-parts="[[784,168,334,39]]" d="M782.000 166.000 L1120.000 166.000 L1120.000 209.000 L782.000 209.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>

    </figure>

=== "<span class='gui-fa' aria-hidden='true'>&#61749;</span>Get started"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Create a project or open an existing one.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/02-project-start.png?v=743fcb18ce5e" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Get started"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Get started"><title>Get started</title><defs><clipPath id="gui-clip-02-project-start-overview-group-getStarted"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/02-project-start.png?v=743fcb18ce5e" width="1480" height="800" clip-path="url(#gui-clip-02-project-start-overview-group-getStarted)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="02-project-start-overview-group-getStarted-1" data-gui-parts="[[770,119,710,155]]" d="M768.000 117.000 L1482.000 117.000 L1482.000 276.000 L768.000 276.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>

    </figure>

</div>

## Enter the project details

Enter a name, title, authors and description for the analysis. Choose a location on your computer, then confirm.

<div class="gui-viewer" markdown="1">


=== "Name"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Use a short project identifier.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/03-project-details.png?v=bff89e6b0ea8" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Name"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Name"><title>Name</title><defs><clipPath id="gui-clip-03-project-details-overview-createProject-name"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/03-project-details.png?v=bff89e6b0ea8" width="1480" height="800" clip-path="url(#gui-clip-03-project-details-overview-createProject-name)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="03-project-details-overview-createProject-name-1" data-gui-parts="[[495,237,490,35]]" d="M493.000 235.000 L987.000 235.000 L987.000 274.000 L493.000 274.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>

    </figure>

=== "Title"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Give the analysis a descriptive title.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/03-project-details.png?v=bff89e6b0ea8" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Title"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Title"><title>Title</title><defs><clipPath id="gui-clip-03-project-details-overview-createProject-title"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/03-project-details.png?v=bff89e6b0ea8" width="1480" height="800" clip-path="url(#gui-clip-03-project-details-overview-createProject-title)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="03-project-details-overview-createProject-title-1" data-gui-parts="[[495,305,490,35]]" d="M493.000 303.000 L987.000 303.000 L987.000 342.000 L493.000 342.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>

    </figure>

=== "Description"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Record the sample, measurement and purpose.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/03-project-details.png?v=bff89e6b0ea8" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Description"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Description"><title>Description</title><defs><clipPath id="gui-clip-03-project-details-overview-createProject-description"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/03-project-details.png?v=bff89e6b0ea8" width="1480" height="800" clip-path="url(#gui-clip-03-project-details-overview-createProject-description)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="03-project-details-overview-createProject-description-1" data-gui-parts="[[495,441,490,73]]" d="M493.000 439.000 L987.000 439.000 L987.000 516.000 L493.000 516.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>

    </figure>

=== "Location"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Choose where the project will be saved.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/03-project-details.png?v=bff89e6b0ea8" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Location"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Location"><title>Location</title><defs><clipPath id="gui-clip-03-project-details-overview-createProject-location"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/03-project-details.png?v=bff89e6b0ea8" width="1480" height="800" clip-path="url(#gui-clip-03-project-details-overview-createProject-location)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="03-project-details-overview-createProject-location-1" data-gui-parts="[[495,547,490,35]]" d="M493.000 545.000 L987.000 545.000 L987.000 584.000 L493.000 584.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>

    </figure>

</div>

## Inspect the project

The Project page keeps the analysis details together. The enabled sidebar tabs offer additional views of this state.

<div class="gui-viewer" markdown="1">


=== "Main workspace"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Inspect the project view here. Its content changes with the active page and selection.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/04-project-created.png?v=e796d4118c6b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Main workspace"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Main workspace"><title>Main workspace</title><defs><clipPath id="gui-clip-04-project-created-overview-workflow-project-mainContent"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/04-project-created.png?v=e796d4118c6b" width="1480" height="800" clip-path="url(#gui-clip-04-project-created-overview-workflow-project-mainContent)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="04-project-created-overview-workflow-project-mainContent-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>

    </figure>

=== "Sidebar"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/04-project-created.png?v=e796d4118c6b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Sidebar"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Sidebar"><title>Sidebar</title><defs><clipPath id="gui-clip-04-project-created-overview-workflow-project-manualSidebar"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/04-project-created.png?v=e796d4118c6b" width="1480" height="800" clip-path="url(#gui-clip-04-project-created-overview-workflow-project-manualSidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="04-project-created-overview-workflow-project-manualSidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>

    </figure>

</div>

## Load the structure

Open **Structure**, expand **Structures**, choose **Load** and select **y2o3.edi**.

<div class="gui-viewer" markdown="1">

<figure class="gui-figure" data-gui-figure>
<p class="gui-view-description">Import the structure file for this example.</p>
<a class="gui-image-link" href="../assets/gui/y2o3/06-structure-import.png?v=6a9e48dc194a" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Load structure"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Load structure"><title>Load structure</title><defs><clipPath id="gui-clip-06-structure-import-overview-structures-load"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/06-structure-import.png?v=6a9e48dc194a" width="1480" height="800" clip-path="url(#gui-clip-06-structure-import-overview-structures-load)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="06-structure-import-overview-structures-load-1" data-gui-parts="[[784,260,334,39]]" d="M782.000 258.000 L1120.000 258.000 L1120.000 301.000 L782.000 301.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>

</figure>

</div>

## Inspect the crystal structure

Inspect the cell, symmetry and atom sites. See [crystallography](../physics/crystallography.md) and [atomic displacement parameters](../physics/displacement.md) for their physical meaning.

<div class="gui-viewer" markdown="1">


=== "Structures"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Select the structure whose cell and atom sites you want to inspect.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/07-structure-loaded.png?v=3852e1c59f0e" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Structures"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Structures"><title>Structures</title><defs><clipPath id="gui-clip-07-structure-loaded-overview-structures-list"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/07-structure-loaded.png?v=3852e1c59f0e" width="1480" height="800" clip-path="url(#gui-clip-07-structure-loaded-overview-structures-list)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="07-structure-loaded-overview-structures-list-1" data-gui-parts="[[784,168,682,78]]" d="M782.000 166.000 L1468.000 166.000 L1468.000 248.000 L782.000 248.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>

    </figure>

=== "Main workspace"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Inspect the structure view here. Its content changes with the active page and selection.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/07-structure-loaded.png?v=3852e1c59f0e" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Main workspace"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Main workspace"><title>Main workspace</title><defs><clipPath id="gui-clip-07-structure-loaded-overview-workflow-structure-mainContent"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/07-structure-loaded.png?v=3852e1c59f0e" width="1480" height="800" clip-path="url(#gui-clip-07-structure-loaded-overview-workflow-structure-mainContent)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="07-structure-loaded-overview-workflow-structure-mainContent-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>

    </figure>

</div>

## Load the experiment

Open **Experiment**, expand **Experiments**, choose **Load** and select **spodi.edi**.

<div class="gui-viewer" markdown="1">

<figure class="gui-figure" data-gui-figure>
<p class="gui-view-description">Import the experiment file, including measured intensities and instrument settings.</p>
<a class="gui-image-link" href="../assets/gui/y2o3/09-experiment-import.png?v=1fc524605c6f" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Load experiment"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Load experiment"><title>Load experiment</title><defs><clipPath id="gui-clip-09-experiment-import-overview-experiments-load"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/09-experiment-import.png?v=1fc524605c6f" width="1480" height="800" clip-path="url(#gui-clip-09-experiment-import-overview-experiments-load)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="09-experiment-import-overview-experiments-load-1" data-gui-parts="[[784,260,218,39]]" d="M782.000 258.000 L1004.000 258.000 L1004.000 301.000 L782.000 301.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>

</figure>

</div>

## Inspect the initial pattern

Compare the measured and calculated intensities before fitting. Review the [peak profile](../physics/profiles/cw.md), [background](../physics/background.md), reflection marks and residual.

<div class="gui-viewer" markdown="1">


=== "Main workspace"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Inspect the experiment view here. Its content changes with the active page and selection.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/10-experiment-loaded.png?v=2bac8b09af44" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Main workspace"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Main workspace"><title>Main workspace</title><defs><clipPath id="gui-clip-10-experiment-loaded-overview-workflow-experiment-mainContent"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/10-experiment-loaded.png?v=2bac8b09af44" width="1480" height="800" clip-path="url(#gui-clip-10-experiment-loaded-overview-workflow-experiment-mainContent)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="10-experiment-loaded-overview-workflow-experiment-mainContent-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>

    </figure>

=== "Sidebar"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/10-experiment-loaded.png?v=2bac8b09af44" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Sidebar"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Sidebar"><title>Sidebar</title><defs><clipPath id="gui-clip-10-experiment-loaded-overview-workflow-experiment-manualSidebar"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/10-experiment-loaded.png?v=2bac8b09af44" width="1480" height="800" clip-path="url(#gui-clip-10-experiment-loaded-overview-workflow-experiment-manualSidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="10-experiment-loaded-overview-workflow-experiment-manualSidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>

    </figure>

</div>

## Refine the model

Open **Analysis**, inspect the free parameters and press **Fit**. Wait for fitting to finish, review the result and close the results popup. This screenshot shows the completed fit with that popup closed. See [Rietveld refinement](../physics/rietveld.md), [uncertainties](../physics/minimization.md) and [reliability factors](../physics/reliability.md).

<div class="gui-viewer" markdown="1">


=== "Main workspace"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Inspect the analysis view here. Its content changes with the active page and selection.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png?v=b139c582c147" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Main workspace"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Main workspace"><title>Main workspace</title><defs><clipPath id="gui-clip-13-analysis-basic-overview-workflow-analysis-mainContent"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png?v=b139c582c147" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-overview-workflow-analysis-mainContent)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="13-analysis-basic-overview-workflow-analysis-mainContent-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[812.359375,0,67.84375,77]]" d="M810.359 -2.000 L882.203 -2.000 L882.203 79.000 L810.359 79.000 Z" /></svg></a>

    </figure>

=== "Sidebar"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png?v=b139c582c147" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Sidebar"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Sidebar"><title>Sidebar</title><defs><clipPath id="gui-clip-13-analysis-basic-overview-workflow-analysis-manualSidebar"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png?v=b139c582c147" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-overview-workflow-analysis-manualSidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="13-analysis-basic-overview-workflow-analysis-manualSidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[812.359375,0,67.84375,77]]" d="M810.359 -2.000 L882.203 -2.000 L882.203 79.000 L810.359 79.000 Z" /></svg></a>

    </figure>

=== "Status bar"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Read project counts, messages, calculation and fitting state here.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png?v=b139c582c147" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Status bar"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Status bar"><title>Status bar</title><defs><clipPath id="gui-clip-13-analysis-basic-overview-statusBar"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png?v=b139c582c147" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-overview-statusBar)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="13-analysis-basic-overview-statusBar-1" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /><path data-gui-navigation data-gui-parts="[[812.359375,0,67.84375,77]]" d="M810.359 -2.000 L882.203 -2.000 L882.203 79.000 L810.359 79.000 Z" /></svg></a>

    </figure>

</div>

## Review the report

Open **Report** to review the structure, measurement and fitted results. Use the sidebar to choose the report contents and export format.

<div class="gui-viewer" markdown="1">


=== "Main workspace"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Inspect the report view here. Its content changes with the active page and selection.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/14-report-basic.png?v=27ffc18aea4b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Main workspace"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Main workspace"><title>Main workspace</title><defs><clipPath id="gui-clip-14-report-basic-overview-workflow-report-mainContent"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/14-report-basic.png?v=27ffc18aea4b" width="1480" height="800" clip-path="url(#gui-clip-14-report-basic-overview-workflow-report-mainContent)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="14-report-basic-overview-workflow-report-mainContent-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[880.203125,0,58.25,77]]" d="M878.203 -2.000 L940.453 -2.000 L940.453 79.000 L878.203 79.000 Z" /></svg></a>

    </figure>

=== "Sidebar"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/14-report-basic.png?v=27ffc18aea4b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Sidebar"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Sidebar"><title>Sidebar</title><defs><clipPath id="gui-clip-14-report-basic-overview-workflow-report-manualSidebar"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/14-report-basic.png?v=27ffc18aea4b" width="1480" height="800" clip-path="url(#gui-clip-14-report-basic-overview-workflow-report-manualSidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="14-report-basic-overview-workflow-report-manualSidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[880.203125,0,58.25,77]]" d="M878.203 -2.000 L940.453 -2.000 L940.453 79.000 L878.203 79.000 Z" /></svg></a>

    </figure>

=== "Status bar"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Read project counts, messages, calculation and fitting state here.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/14-report-basic.png?v=27ffc18aea4b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Status bar"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Status bar"><title>Status bar</title><defs><clipPath id="gui-clip-14-report-basic-overview-statusBar"><rect width="1480" height="800" rx="17.76" /></clipPath></defs><image href="../assets/gui/y2o3/14-report-basic.png?v=27ffc18aea4b" width="1480" height="800" clip-path="url(#gui-clip-14-report-basic-overview-statusBar)" /><rect class="gui-image-frame" width="1480" height="800" rx="17.76" /><path class="is-active" data-gui-region="14-report-basic-overview-statusBar-1" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /><path data-gui-navigation data-gui-parts="[[880.203125,0,58.25,77]]" d="M878.203 -2.000 L940.453 -2.000 L940.453 79.000 L878.203 79.000 Z" /></svg></a>

    </figure>

</div>

## Explore the workspace

See [Application layout](workspace.md) for an annotated overview of every workflow page and its enabled sidebar tabs.
