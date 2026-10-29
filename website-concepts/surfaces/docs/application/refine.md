# Refine a diffraction pattern

Refinement adjusts the parameters you choose to bring the calculated result closer to the measured data. Begin with a structural model and experiment that plausibly describe the measurement; refinement is not a substitute for checking those choices.

The shared [Analysis](../user-guide/analysis-workflow/analysis.md) chapter explains the scientific model; the steps below describe this interface.

## Load or prepare the project

Open an existing project or an included example on **Project**. To analyse your own measurement, follow [create a project](new-project.md).

On **Structure**, check symmetry, cell and atom sites. On **Experiment**, check the data, instrument, peak profile, [background](background.md), excluded regions and linked structures.

## Compare the starting pattern

Look at peak positions, widths, intensities and the background before fitting. An incorrect wavelength or calibration can shift peaks; a missing phase can leave intensity the model cannot explain.

![The pattern, residual and reflection positions](../assets/edi-app.png)

## Choose free parameters

On **Analysis**, the parameter table shows the values available to the fit. Use the **free** column to choose which independent parameters may vary. The name and variability filters help you find them.

Values fixed by symmetry or constrained to other values are not independent fit parameters. The minimum and maximum displayed in the table describe admissible model values; they are not a separate set of user-defined optimizer bounds.

Free parameters deliberately, checking the effect of each stage. Starting with every parameter free can hide an unsuitable model behind strongly correlated values.

## Select a fitting mode

The available mode depends on the project. One experiment is fitted on its own; several experiments can be fitted jointly. A scan can run sequentially or independently across its datasets. See [fitting modes](fitting-modes.md).

## Start and inspect the fit

Choose **Start fitting**. Review the calculated curve and residual as well as the reported agreement factors. Parameter uncertainties and correlations help you understand what the data constrain.

A small agreement factor alone does not establish that the structural model is correct. Inspect unmodelled features and physically implausible values before accepting the result.

## Save the project and report

Save the updated project if you want to keep working from its refined values. Use the **Report** page to prepare a separate document containing the selected model, results and figures.

The same project can be opened in [Python](../python/fit.md) or run with [the Command Line](../cli/fit.md).
