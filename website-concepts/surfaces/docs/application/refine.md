---
template: gui.html
---

# :material-calculator: Refine a diffraction pattern

Refinement adjusts the parameters you choose to bring the calculated result closer to the measured data. Begin with a structural model and experiment that plausibly describe the measurement; refinement is not a substitute for checking those choices.

The shared [Analysis](../user-guide/analysis-workflow/analysis.md) chapter explains the scientific model; the steps below describe this interface.

## Load or prepare the project

Open an existing project or an included example on **Project**. To analyse your own measurement, follow [create a project](new-project.md).

On **Structure**, check symmetry, cell and atom sites. On **Experiment**, check the data, instrument, peak profile, [background](background.md), excluded regions and linked structures.

## Compare the starting pattern

Look at peak positions, widths, intensities and the background before fitting. An incorrect wavelength or calibration can shift peaks; a missing phase can leave intensity the model cannot explain.

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/10-experiment-loaded.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Compare the measured pattern with the initial calculation"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Compare the measured pattern with the initial calculation"><title>Compare the measured pattern with the initial calculation</title><defs><clipPath id="gui-clip-10-experiment-loaded-overview"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/10-experiment-loaded.png" width="1480" height="800" clip-path="url(#gui-clip-10-experiment-loaded-overview)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="10-experiment-loaded-overview-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="10-experiment-loaded-overview-2" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /></svg></a>
<figcaption>Compare the measured pattern with the initial calculation.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="10-experiment-loaded-overview-1" aria-pressed="true">1. Main workspace</button> Inspect the experiment view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="10-experiment-loaded-overview-2" aria-pressed="false">2. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li></ol>
</figure>


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

## Related Physics

[Least-squares objective](../physics/rietveld.md#eq-weighted-residual) · [Minimization and covariance](../physics/minimization.md) · [Agreement factors](../physics/reliability.md).
