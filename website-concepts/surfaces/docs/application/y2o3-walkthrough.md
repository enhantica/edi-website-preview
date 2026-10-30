# Y₂O₃ on SPODI: a complete GUI walkthrough

!!! info "Work in progress"

    This walkthrough is being captured from the desktop application at 1480 × 800. The native capture build is in progress. The illustrated page and sidebar views will appear here as the scripted run is verified.

Build a project from its separate inputs, refine the model and review a report. The example is **pd-neut-cwl_y2o3-spodi**, constant-wavelength neutron powder diffraction from SPODI at FRM II.

## Download the inputs

- [Y₂O₃ crystal structure](../assets/gui/y2o3/inputs/y2o3.edi)
- [SPODI experiment and measured intensities](../assets/gui/y2o3/inputs/spodi.edi)

The experiment file includes the instrument, profile, background, measured pattern and starting fit settings. These are separate inputs; the walkthrough does not open a complete prepared project.

## Home

Open EasyDiffraction and press **Start**. The Project page is the first step of the analysis.

## Create the project

Choose **Create a new project**. Enter a name, title, authors, description and location, then confirm. For this example use **pd-neut-cwl_y2o3-spodi** as the name and **Y2O3 on SPODI** as the title.

The project keeps your structures, experiments, analysis and report together. Its sidebar offers the controls enabled for the current state.

## Load the structure

Open **Structure**, expand **Structures**, choose **Load** and select **y2o3.edi**.

Inspect the crystal view, unit cell, space group and atom sites. The example includes anisotropic displacement tensors tied by site symmetry. See [crystallography](../physics/crystallography.md) and [atomic displacement](../physics/displacement.md) for their meaning.

## Load the experiment

Open **Experiment**, expand **Experiments**, choose **Load** and select **spodi.edi**.

Compare the measured and calculated patterns before fitting. Inspect the reflection marks and residual, then review the instrument, peak profile and background. The supplied input declares which starting parameters are free.

See [constant-wavelength profiles](../physics/profiles/cw.md) and [background models](../physics/background.md).

## Refine

Open **Analysis**, review the free parameters and start fitting. Wait for the run to finish, read the result, then close the results popup.

Inspect the fitted pattern, residual, parameter values and uncertainties. All Analysis screenshots in the completed capture set will show this post-fit state with the popup closed.

See [Rietveld refinement](../physics/rietveld.md), [minimization and uncertainty](../physics/minimization.md) and [reliability factors](../physics/reliability.md).

## Review the report

Open **Report** to review the fitted structure, experiment and result together. Review the report contents and export controls.

The illustrated reference will include a screenshot of every enabled **Main**, **Extra**, **Text** and **Settings** sidebar tab on each workflow page.
