---
template: gui.html
---

# :material-archive: Create a project from your own data

You can create a project in the app without preparing a project file first. Add the structure, describe the experiment, load the measured pattern, then choose the parameters to refine.

## Create the project

On **Project**, choose **Create a new project**. If the current project has unsaved changes, the application asks whether to save them before replacing it.

<!-- gui-guide:create-the-project -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/03-project-details.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Enter the project details and choose its location"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Enter the project details and choose its location"><title>Enter the project details and choose its location</title><defs><clipPath id="gui-clip-03-project-details-overview-new-project-create-the-project-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/03-project-details.png" width="1480" height="800" clip-path="url(#gui-clip-03-project-details-overview-new-project-create-the-project-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="03-project-details-overview-new-project-create-the-project-0-1" data-gui-parts="[[495,237,490,35]]" d="M493.000 235.000 L987.000 235.000 L987.000 274.000 L493.000 274.000 Z" /><path class="" data-gui-region="03-project-details-overview-new-project-create-the-project-0-2" data-gui-parts="[[495,305,490,35]]" d="M493.000 303.000 L987.000 303.000 L987.000 342.000 L493.000 342.000 Z" /><path class="" data-gui-region="03-project-details-overview-new-project-create-the-project-0-3" data-gui-parts="[[495,441,490,73]]" d="M493.000 439.000 L987.000 439.000 L987.000 516.000 L493.000 516.000 Z" /><path class="" data-gui-region="03-project-details-overview-new-project-create-the-project-0-4" data-gui-parts="[[495,547,490,35]]" d="M493.000 545.000 L987.000 545.000 L987.000 584.000 L493.000 584.000 Z" /></svg></a>
<figcaption>Enter the project details and choose its location.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="03-project-details-overview-new-project-create-the-project-0-1" aria-pressed="true">1. Name</button> Use a short project identifier.</li><li><button type="button" data-gui-target="03-project-details-overview-new-project-create-the-project-0-2" aria-pressed="false">2. Title</button> Give the analysis a descriptive title.</li><li><button type="button" data-gui-target="03-project-details-overview-new-project-create-the-project-0-3" aria-pressed="false">3. Description</button> Record the sample, measurement and purpose.</li><li><button type="button" data-gui-target="03-project-details-overview-new-project-create-the-project-0-4" aria-pressed="false">4. Location</button> Choose where the project will be saved.</li></ol>
</figure>
<!-- /gui-guide -->

## Add a structure

On **Structure**, choose **Create structure**. The app adds a starting structure with one atom site. Edit its space group, unit cell and atom sites to describe your sample; the starting values are a template, not a model of your material.

If you already have a structure file, use **Load structure from file** to select a CIF or `.edi` structure file. See [structures](structures.md).

<!-- gui-guide:add-a-structure -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-create.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Load, create or duplicate a structure"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Load, create or duplicate a structure"><title>Load, create or duplicate a structure</title><defs><clipPath id="gui-clip-guide-structure-create-overview-new-project-add-a-structure-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-create.png" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-create-overview-new-project-add-a-structure-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-create-overview-new-project-add-a-structure-0-1" data-gui-parts="[[784,260,334,39]]" d="M782.000 258.000 L1120.000 258.000 L1120.000 301.000 L782.000 301.000 Z" /><path class="" data-gui-region="guide-structure-create-overview-new-project-add-a-structure-0-2" data-gui-parts="[[1132,260,334,39]]" d="M1130.000 258.000 L1468.000 258.000 L1468.000 301.000 L1130.000 301.000 Z" /><path class="" data-gui-region="guide-structure-create-overview-new-project-add-a-structure-0-3" data-gui-parts="[[784,313,334,39]]" d="M782.000 311.000 L1120.000 311.000 L1120.000 354.000 L782.000 354.000 Z" /></svg></a>
<figcaption>Load, create or duplicate a structure.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-structure-create-overview-new-project-add-a-structure-0-1" aria-pressed="true">1. Load structure</button> Import the structure file for this example.</li><li><button type="button" data-gui-target="guide-structure-create-overview-new-project-add-a-structure-0-2" aria-pressed="false">2. Create structure</button> Add a starting structure to edit.</li><li><button type="button" data-gui-target="guide-structure-create-overview-new-project-add-a-structure-0-3" aria-pressed="false">3. Duplicate structure</button> Copy the selected structure.</li></ol>
</figure>
<!-- /gui-guide -->

## Create an experiment

On **Experiment**, choose **Create experiment**. The new experiment is linked to the project's structures. Until measured data are loaded, it is a simulation: choose its type and the range over which its pattern is calculated.

Set the experiment type before loading data. A measurement fixes its axis and the type control is no longer editable after data are present.

<!-- gui-guide:create-an-experiment -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-create.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Load or create an experiment"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Load or create an experiment"><title>Load or create an experiment</title><defs><clipPath id="gui-clip-guide-experiment-create-overview-new-project-create-an-experiment-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-create.png" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-create-overview-new-project-create-an-experiment-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-create-overview-new-project-create-an-experiment-0-1" data-gui-parts="[[784,400,218,39]]" d="M782.000 398.000 L1004.000 398.000 L1004.000 441.000 L782.000 441.000 Z" /><path class="" data-gui-region="guide-experiment-create-overview-new-project-create-an-experiment-0-2" data-gui-parts="[[1016,400,218,39]]" d="M1014.000 398.000 L1236.000 398.000 L1236.000 441.000 L1014.000 441.000 Z" /></svg></a>
<figcaption>Load or create an experiment.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-create-overview-new-project-create-an-experiment-0-1" aria-pressed="true">1. Load experiment</button> Import the experiment file, including measured intensities and instrument settings.</li><li><button type="button" data-gui-target="guide-experiment-create-overview-new-project-create-an-experiment-0-2" aria-pressed="false">2. Create experiment</button> Add an experiment and choose its measurement type.</li></ol>
</figure>
<!-- /gui-guide -->

## Load the measured pattern

Choose **Load data…** in the experiment's **File** cell. A text file can contain `x y` or `x y sigma` columns separated by spaces, tabs or commas.

For a constant-wavelength powder experiment, `x` is 2θ in degrees. For a time-of-flight experiment it is time of flight in microseconds. Read the import message to see whether any rows were skipped or adjusted.

The measured points replace the simulation range. The instrument, peak profile, background and excluded regions remain as you set them. See [experiments and data](experiments.md) for the import rules.

<!-- gui-guide:load-the-measured-pattern -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-data.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Select an experiment or load measured data"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Select an experiment or load measured data"><title>Select an experiment or load measured data</title><defs><clipPath id="gui-clip-guide-experiment-data-overview-new-project-load-the-measured-pattern-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-data.png" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-data-overview-new-project-load-the-measured-pattern-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-data-overview-new-project-load-the-measured-pattern-0-1" data-gui-parts="[[784,168,682,78]]" d="M782.000 166.000 L1468.000 166.000 L1468.000 248.000 L782.000 248.000 Z" /><path class="" data-gui-region="guide-experiment-data-overview-new-project-load-the-measured-pattern-0-2" data-gui-parts="[[958,207,53.609375,39]]" d="M956.000 205.000 L1013.609 205.000 L1013.609 248.000 L956.000 248.000 Z" /></svg></a>
<figcaption>Select an experiment or load measured data.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-data-overview-new-project-load-the-measured-pattern-0-1" aria-pressed="true">1. Experiments</button> Select the measurement to inspect.</li><li><button type="button" data-gui-target="guide-experiment-data-overview-new-project-load-the-measured-pattern-0-2" aria-pressed="false">2. Measured-data file</button> Load the observed intensities for this experiment.</li></ol>
</figure>
<!-- /gui-guide -->

## Prepare and run the fit

Check the linked structure, scale, instrument and profile. Estimate or enter the [background](background.md). On **Analysis**, choose the parameters that should be free, then use **Start fitting**.

Follow [refine a pattern](refine.md) to assess the result.

<!-- gui-guide:prepare-and-run-the-fit -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Completed Rietveld refinement — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Completed Rietveld refinement — Main"><title>Completed Rietveld refinement — Main</title><defs><clipPath id="gui-clip-13-analysis-basic-overview-new-project-prepare-and-run-the-fit-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-overview-new-project-prepare-and-run-the-fit-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-overview-new-project-prepare-and-run-the-fit-0-1" data-gui-parts="[[0,0,1480,77]]" d="M-2.000 -2.000 L1482.000 -2.000 L1482.000 79.000 L-2.000 79.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-new-project-prepare-and-run-the-fit-0-2" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-new-project-prepare-and-run-the-fit-0-3" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-new-project-prepare-and-run-the-fit-0-4" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /></svg></a>
<figcaption>Completed Rietveld refinement — Main.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="13-analysis-basic-overview-new-project-prepare-and-run-the-fit-0-1" aria-pressed="true">1. Workflow navigation</button> Move between Home, Project, Structure, Experiment, Analysis and Report.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-new-project-prepare-and-run-the-fit-0-2" aria-pressed="false">2. Main workspace</button> Inspect the analysis view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-new-project-prepare-and-run-the-fit-0-3" aria-pressed="false">3. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-new-project-prepare-and-run-the-fit-0-4" aria-pressed="false">4. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
</figure>
<!-- /gui-guide -->

## Save your work

Use **Save project as…** to choose where to keep it. The [file handling guide](projects.md) explains folders, zip archives and browser storage. Measured data are written into the experiment's `.edi` file, so the saved project does not depend on the original text file you imported.

<!-- gui-guide:save-your-work -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-project-save.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Choose a save format or save a copy"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Choose a save format or save a copy"><title>Choose a save format or save a copy</title><defs><clipPath id="gui-clip-guide-project-save-overview-new-project-save-your-work-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-project-save.png" width="1480" height="800" clip-path="url(#gui-clip-guide-project-save-overview-new-project-save-your-work-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-project-save-overview-new-project-save-your-work-0-1" data-gui-parts="[[607,354,111.84375,93]]" d="M605.000 352.000 L720.844 352.000 L720.844 449.000 L605.000 449.000 Z" /></svg></a>
<figcaption>Choose a save format or save a copy.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-project-save-overview-new-project-save-your-work-0-1" aria-pressed="true">1. Save options</button> Choose the output format and whether to save a copy.</li></ol>
</figure>
<!-- /gui-guide -->
