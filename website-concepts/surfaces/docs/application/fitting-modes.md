# Choose a fitting mode

The fitting mode determines how the project's experiments or scan datasets are fitted. It changes the relationship between fits, not the meaning of the structures and experiments.

The shared [fitting-mode guide](../user-guide/fitting-modes.md) explains single, joint, sequential and independent fitting, including their starting-state policies. This page explains the application controls.

## Select the mode in the app

Open **Analysis** and use the fitting-mode control. The choices reflect the project: with only one applicable mode the selector is disabled and explains why.

A joint fit shows the experiment weights. A scan mode shows its scan declaration. The mode is saved as part of the project and is also read by Python and Command Line analysis.

## Fit several experiments jointly

A joint fit uses all the project's experiments together. Shared structural parameters can be informed by more than one measurement, while each experiment keeps its own instrument, background and other settings.

Review the experiment weights and linked structures before running. A joint result should still be inspected experiment by experiment.

## Fit a scan

Use **sequential** when each result should seed the next fit, or **independent** when you want each dataset to start from the same template. Follow the [scan guide](scans.md) for dataset selection, progress, continuation and evolution charts.

## Fit the shown scan dataset on its own

A scan can use `single` to fit the shown dataset. That result becomes the template, and the selected file becomes the template dataset. Check the template before starting a full scan.

---

Sources: [current fitting-mode controls](https://github.com/enhantica/edi/blob/main/app/qml/Pages/Analysis/FittingModeGroup.qml), [current scan guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/sequential-fitting-in-the-app.md), [current project-analysis contract](https://github.com/enhantica/edi/blob/main/docs/user/guides/complete-project-loading.md).
