# :material-archive: Create a project from your own data

You can create a project in the app without preparing a project file first. Add the structure, describe the experiment, load the measured pattern, then choose the parameters to refine.

## Create the project

On **Project**, choose **Create a new project**. If the current project has unsaved changes, the application asks whether to save them before replacing it.

## Add a structure

On **Structure**, choose **Create structure**. The app adds a starting structure with one atom site. Edit its space group, unit cell and atom sites to describe your sample; the starting values are a template, not a model of your material.

If you already have a structure file, use **Load structure from file** to select a CIF or `.edi` structure file. See [structures](structures.md).

## Create an experiment

On **Experiment**, choose **Create experiment**. The new experiment is linked to the project's structures. Until measured data are loaded, it is a simulation: choose its type and the range over which its pattern is calculated.

Set the experiment type before loading data. A measurement fixes its axis and the type control is no longer editable after data are present.

## Load the measured pattern

Choose **Load data…** in the experiment's **File** cell. A text file can contain `x y` or `x y sigma` columns separated by spaces, tabs or commas.

For a constant-wavelength powder experiment, `x` is 2θ in degrees. For a time-of-flight experiment it is time of flight in microseconds. Read the import message to see whether any rows were skipped or adjusted.

The measured points replace the simulation range. The instrument, peak profile, background and excluded regions remain as you set them. See [experiments and data](experiments.md) for the import rules.

## Prepare and run the fit

Check the linked structure, scale, instrument and profile. Estimate or enter the [background](background.md). On **Analysis**, choose the parameters that should be free, then use **Start fitting**.

Follow [refine a pattern](refine.md) to assess the result.

## Save your work

Use **Save project as…** to choose where to keep it. The [file handling guide](projects.md) explains folders, zip archives and browser storage. Measured data are written into the experiment's `.edi` file, so the saved project does not depend on the original text file you imported.
