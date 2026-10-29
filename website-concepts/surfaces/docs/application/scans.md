# Fit a sequence of measurements

A scan is a series of data files measured in order, for example while a sample cools. The project uses one template experiment and declares the files to fit. The application lists them as datasets and fits them through the same analysis as the command line.

## Choose a dataset

On **Experiment**, the **Experiments** table and the selector above the pattern list the datasets in fitting order. The selector supports searching when the list is long.

Before fitting, a selected dataset is shown with the template's settings. After a scan has been fitted, the page can show that dataset's fitted values and the pattern calculated from them. Selecting a dataset also updates the relevant Structure page values.

![A selected scan dataset with experiment settings](../assets/edi-app.png)

## Choose the starting-point rule

On **Analysis**, select `sequential` or `independent`:

- **Sequential** starts each dataset from the preceding dataset's fitted values.
- **Independent** starts every dataset from the same template values.

A `single` fit of the shown dataset makes its result the template. The template dataset is identified in the selector and table.

## Run, stop and continue

Choose **Start fitting**. The status bar reports progress through the files and the converged and failed counts.

**Stop fitting** keeps the results completed so far. **Continue fitting** resumes from the first unfitted file. Once every dataset has been fitted, the button is disabled. **Reset fits** clears the results so that the scan can be fitted again; Undo restores the prior results.

## Follow progress

**Follow** shows the dataset currently being fitted. Choosing another dataset turns Follow off; choose it again to resume following the run.

The Analysis page's **Settings** tab controls pattern updates during a scan. You can choose responsive adaptive updates, every-pattern display, or only the final pattern. Waiting for every redraw can make the fit take longer, while allowing the display to catch up keeps fitting independent of drawing.

## Inspect evolution and correlations

The **Evolution** tab plots a chosen fitted parameter, with its uncertainty, against an extracted dataset value or its place in the scan. Select a point to show that dataset elsewhere in the app.

The selected dataset's **Correlations** tab shows correlations from its last fit. Only the template dataset's correlations are kept when saving and reopening the project.

After editing the template, previous results remain visible but are marked out of date until a new run replaces them.

## Save the scan

The run writes a row per dataset to `analysis/results.csv` as it progresses. Use **Save project as…** to keep a working copy of an example together with its data and results.

## Related Physics

[Single and joint fitting](../physics/rietveld.md#joint-refinement) · [Sequential and independent scans](../physics/rietveld.md#scan-refinement).
