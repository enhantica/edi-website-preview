# Your first refinement

Start with an included measured-data example. It supplies the structure, instrument settings, measured pattern and starting parameters together, so you can focus on the analysis workflow.

## Open the application

[Open the web app](https://enhantica.github.io/edi/webapp/) in a current browser. Go to **Project** and expand **Examples**.

Choose the LBCO example measured on HRPT for a first powder refinement. A simulation example has no measured data to fit; it is useful for calculation instead.

The example opens as a working copy. Changes will not alter the bundled input.

## Inspect the structure

Open **Structure**. Look at the space group, unit cell and atom sites. These describe the crystalline sample.

The experiment settings are separate. A peak-profile term or calibration shift does not become part of the structural model just because it changes the calculated pattern.

## Compare the initial pattern

On **Experiment**, select the experiment and inspect the calculated signal against its measured intensities.

![Measured and calculated intensities with reflection positions and residual](../assets/edi-app.png)

The reflection marks locate the expected Bragg positions, and the residual shows the observed-minus-calculated difference. Check the overall range and the mismatch around individual peaks before fitting.

The image illustrates the same pattern workspace using a Co₂SiO₄ scan; the LBCO example you open has its own pattern and parameters.

## Choose what varies

On **Analysis**, inspect the free-parameter table and fitting mode. A fit can change only the parameters allowed to vary independently.

For the first run, keep the example's supplied choices. They are part of its starting conditions. Later, change one meaningful part of the model at a time and compare the result. [Parameters](../user-guide/parameters.md) explains free, fixed and related values.

## Run the fit

Press **Start fitting**. Read how the run ended, then compare the updated calculated pattern with the observations.

A successful termination means the optimisation completed under its settings. Continue by checking the residual, fitted values and uncertainties. The [fit-quality guide](../user-guide/fit-quality.md) explains why one agreement factor is not the whole assessment.

## Inspect a report

Open **Report** to review the project and result as a document. Its contents and export formats are separate from saving the project.

Use [reports](reports.md) for the available options and the differences between a visual report, scientific CIF output and the editable project state.

## Keep your work

Use **Save project as…** to keep your own copy of the example. In a browser you may be offered a local location or a zip download, depending on the browser and where the project is being kept.

Use an external folder or archive for work you want to retain. Browser storage can be cleared. See [projects and files](projects.md).

## Continue from here

- [Create a project](new-project.md) from your own structure and observations.
- Explore [other example projects](../user-guide/examples.md).
- Run the same saved project in [Python](../python/fit.md) or [the Command Line](../cli/fit.md).
