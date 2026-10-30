---
template: gui.html
---

# :material-calculator: Refine a diffraction pattern

Refinement adjusts the parameters you choose to bring the calculated result closer to the measured data. Begin with a structural model and experiment that plausibly describe the measurement; refinement is not a substitute for checking those choices.

The shared [Analysis](../user-guide/analysis-workflow/analysis.md) chapter explains the scientific model; the steps below describe this interface.

## Load or prepare the project

Open an existing project or an included example on **Project**. To analyse your own measurement, follow [create a project](new-project.md).

On **Structure**, check symmetry, cell and atom sites. On **Experiment**, check the data, instrument, peak profile, [background](background.md), excluded regions and linked structures.

<!-- gui-guide:load-or-prepare-the-project -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-project-actions.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Open or save the current project"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Open or save the current project"><title>Open or save the current project</title><defs><clipPath id="gui-clip-guide-project-actions-overview-refine-load-or-prepare-the-project-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-project-actions.png" width="1480" height="800" clip-path="url(#gui-clip-guide-project-actions-overview-refine-load-or-prepare-the-project-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-project-actions-overview-refine-load-or-prepare-the-project-0-1" data-gui-parts="[[1132,168,334,39]]" d="M1130.000 166.000 L1468.000 166.000 L1468.000 209.000 L1130.000 209.000 Z" /><path class="" data-gui-region="guide-project-actions-overview-refine-load-or-prepare-the-project-0-2" data-gui-parts="[[784,221,334,39]]" d="M782.000 219.000 L1120.000 219.000 L1120.000 262.000 L782.000 262.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>
<figcaption>Open or save the current project.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-project-actions-overview-refine-load-or-prepare-the-project-0-1" aria-pressed="true">1. Open project…</button> </li><li><button type="button" data-gui-target="guide-project-actions-overview-refine-load-or-prepare-the-project-0-2" aria-pressed="false">2. Save project as…</button> </li></ol>
</figure>
<!-- /gui-guide -->

## Compare the starting pattern

Look at peak positions, widths, intensities and the background before fitting. An incorrect wavelength or calibration can shift peaks; a missing phase can leave intensity the model cannot explain.

<!-- gui-guide:compare-the-starting-pattern -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/10-experiment-loaded.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Compare the measured pattern with the initial calculation"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Compare the measured pattern with the initial calculation"><title>Compare the measured pattern with the initial calculation</title><defs><clipPath id="gui-clip-10-experiment-loaded-overview-refine-compare-the-starting-pattern-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/10-experiment-loaded.png" width="1480" height="800" clip-path="url(#gui-clip-10-experiment-loaded-overview-refine-compare-the-starting-pattern-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="10-experiment-loaded-overview-refine-compare-the-starting-pattern-0-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="10-experiment-loaded-overview-refine-compare-the-starting-pattern-0-2" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>
<figcaption>Compare the measured pattern with the initial calculation.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="10-experiment-loaded-overview-refine-compare-the-starting-pattern-0-1" aria-pressed="true">1. Main workspace</button> Inspect the experiment view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="10-experiment-loaded-overview-refine-compare-the-starting-pattern-0-2" aria-pressed="false">2. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li></ol>
</figure>
<!-- /gui-guide -->

## Choose free parameters

On **Analysis**, the parameter table shows the values available to the fit. Use the **free** column to choose which independent parameters may vary. The name and variability filters help you find them.

Values fixed by symmetry or constrained to other values are not independent fit parameters. The minimum and maximum displayed in the table describe admissible model values; they are not a separate set of user-defined optimizer bounds.

Free parameters deliberately, checking the effect of each stage. Starting with every parameter free can hide an unsuitable model behind strongly correlated values.

<!-- gui-guide:choose-free-parameters -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Completed Rietveld refinement — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Completed Rietveld refinement — Main"><title>Completed Rietveld refinement — Main</title><defs><clipPath id="gui-clip-13-analysis-basic-overview-refine-choose-free-parameters-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-overview-refine-choose-free-parameters-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-overview-refine-choose-free-parameters-0-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-refine-choose-free-parameters-0-2" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-refine-choose-free-parameters-0-3" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /><path data-gui-navigation data-gui-parts="[[812.359375,0,67.84375,77]]" d="M810.359 -2.000 L882.203 -2.000 L882.203 79.000 L810.359 79.000 Z" /></svg></a>
<figcaption>Completed Rietveld refinement — Main.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="13-analysis-basic-overview-refine-choose-free-parameters-0-1" aria-pressed="true">1. Main workspace</button> Inspect the analysis view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-refine-choose-free-parameters-0-2" aria-pressed="false">2. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-refine-choose-free-parameters-0-3" aria-pressed="false">3. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
</figure>
<!-- /gui-guide -->

## Select a fitting mode

The available mode depends on the project. One experiment is fitted on its own; several experiments can be fitted jointly. A scan can run sequentially or independently across its datasets. See [fitting modes](fitting-modes.md).

<!-- gui-guide:select-a-fitting-mode -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-analysis-modes.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Choose a fitting mode supported by the project"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Choose a fitting mode supported by the project"><title>Choose a fitting mode supported by the project</title><defs><clipPath id="gui-clip-guide-analysis-modes-overview-refine-select-a-fitting-mode-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-analysis-modes.png" width="1480" height="800" clip-path="url(#gui-clip-guide-analysis-modes-overview-refine-select-a-fitting-mode-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-analysis-modes-overview-refine-select-a-fitting-mode-0-1" data-gui-parts="[[784,210,682,56]]" d="M782.000 208.000 L1468.000 208.000 L1468.000 268.000 L782.000 268.000 Z" /><path data-gui-navigation data-gui-parts="[[812.359375,0,67.84375,77]]" d="M810.359 -2.000 L882.203 -2.000 L882.203 79.000 L810.359 79.000 Z" /></svg></a>
<figcaption>Choose a fitting mode supported by the project.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-analysis-modes-overview-refine-select-a-fitting-mode-0-1" aria-pressed="true">1. Fitting mode</button> The available choices depend on the project.</li></ol>
</figure>
<!-- /gui-guide -->

## Start and inspect the fit

Choose **Start fitting**. Review the calculated curve and residual as well as the reported agreement factors. Parameter uncertainties and correlations help you understand what the data constrain.

A small agreement factor alone does not establish that the structural model is correct. Inspect unmodelled features and physically implausible values before accepting the result.

<!-- gui-guide:start-and-inspect-the-fit -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Completed Rietveld refinement — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Completed Rietveld refinement — Main"><title>Completed Rietveld refinement — Main</title><defs><clipPath id="gui-clip-13-analysis-basic-overview-refine-start-and-inspect-the-fit-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-overview-refine-start-and-inspect-the-fit-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-overview-refine-start-and-inspect-the-fit-0-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-refine-start-and-inspect-the-fit-0-2" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-refine-start-and-inspect-the-fit-0-3" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /><path data-gui-navigation data-gui-parts="[[812.359375,0,67.84375,77]]" d="M810.359 -2.000 L882.203 -2.000 L882.203 79.000 L810.359 79.000 Z" /></svg></a>
<figcaption>Completed Rietveld refinement — Main.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="13-analysis-basic-overview-refine-start-and-inspect-the-fit-0-1" aria-pressed="true">1. Main workspace</button> Inspect the analysis view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-refine-start-and-inspect-the-fit-0-2" aria-pressed="false">2. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-refine-start-and-inspect-the-fit-0-3" aria-pressed="false">3. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
</figure>
<!-- /gui-guide -->

## Save the project and report

Save the updated project if you want to keep working from its refined values. Use the **Report** page to prepare a separate document containing the selected model, results and figures.

The same project can be opened in [Python](../python/fit.md) or run with [the Command Line](../cli/fit.md).

<!-- gui-guide:save-the-project-and-report -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-report-saved.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Review the saved report status"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Review the saved report status"><title>Review the saved report status</title><defs><clipPath id="gui-clip-guide-report-saved-overview-refine-save-the-project-and-report-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-report-saved.png" width="1480" height="800" clip-path="url(#gui-clip-guide-report-saved-overview-refine-save-the-project-and-report-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-report-saved-overview-refine-save-the-project-and-report-0-1" data-gui-parts="[[770,119,710,249]]" d="M768.000 117.000 L1482.000 117.000 L1482.000 370.000 L768.000 370.000 Z" /><path data-gui-navigation data-gui-parts="[[880.203125,0,58.25,77]]" d="M878.203 -2.000 L940.453 -2.000 L940.453 79.000 L878.203 79.000 Z" /></svg></a>
<figcaption>Review the saved report status.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-report-saved-overview-refine-save-the-project-and-report-0-1" aria-pressed="true">1. Export</button> </li></ol>
</figure>
<!-- /gui-guide -->

## Related Physics

[Least-squares objective](../physics/rietveld.md#eq-weighted-residual) · [Minimization and covariance](../physics/minimization.md) · [Agreement factors](../physics/reliability.md).
