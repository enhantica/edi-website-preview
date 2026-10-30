---
template: gui.html
---

# :material-calculator: Choose a fitting mode

The fitting mode determines how the project's experiments or scan datasets are fitted. It changes the relationship between fits, not the meaning of the structures and experiments.

The shared [fitting-mode guide](../user-guide/fitting-modes.md) explains single, joint, sequential and independent fitting, including their starting-state policies. This page explains the application controls.

## Select the mode in the app

Open **Analysis** and use the fitting-mode control. The choices reflect the project: with only one applicable mode the selector is disabled and explains why.

A joint fit shows the experiment weights. A scan mode shows its scan declaration. The mode is saved as part of the project and is also read by Python and Command Line analysis.

<!-- gui-guide:select-the-mode-in-the-app -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-analysis-modes.png?v=b4afc690097f" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Choose a fitting mode supported by the project"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Choose a fitting mode supported by the project"><title>Choose a fitting mode supported by the project</title><defs><clipPath id="gui-clip-guide-analysis-modes-overview-fitting-modes-select-the-mode-in-the-app-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-analysis-modes.png?v=b4afc690097f" width="1480" height="800" clip-path="url(#gui-clip-guide-analysis-modes-overview-fitting-modes-select-the-mode-in-the-app-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-analysis-modes-overview-fitting-modes-select-the-mode-in-the-app-0-1" data-gui-parts="[[784,210,682,56]]" d="M782.000 208.000 L1468.000 208.000 L1468.000 268.000 L782.000 268.000 Z" /><path data-gui-navigation data-gui-parts="[[812.359375,0,67.84375,77]]" d="M810.359 -2.000 L882.203 -2.000 L882.203 79.000 L810.359 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-analysis-modes-overview-fitting-modes-select-the-mode-in-the-app-0-1" aria-pressed="true">1. Fitting mode</button> The available choices depend on the project.</li></ol>
</figure>
<!-- /gui-guide -->

## Fit several experiments jointly

A joint fit uses all the project's experiments together. Shared structural parameters can be informed by more than one measurement, while each experiment keeps its own instrument, background and other settings.

Review the experiment weights and linked structures before running. A joint result should still be inspected experiment by experiment.

## Fit a scan

Use **sequential** when each result should seed the next fit, or **independent** when you want each dataset to start from the same template. Follow the [scan guide](scans.md) for dataset selection, progress, continuation and evolution charts.

## Fit the shown scan dataset on its own

A scan can use `single` to fit the shown dataset. That result becomes the template, and the selected file becomes the template dataset. Check the template before starting a full scan.

## Related Physics

[Single and joint fitting](../physics/rietveld.md#joint-refinement) · [Sequential and independent scans](../physics/rietveld.md#scan-refinement).
