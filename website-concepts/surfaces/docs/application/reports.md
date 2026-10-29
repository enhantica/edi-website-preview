# Review and save a report

The **Report** page presents structures, experiments, fit information and correlations as one document. The shared [Report](../user-guide/analysis-workflow/report.md) stage explains the document and its relationship to the saved project. This page covers the application controls.

## Review the document

The main view shows the report with its figures and structure views. Inspect it after a fit, particularly the selected experiment, model values and charts.

The sidebar has **Export** and **Contents** groups.

## Choose the contents

**Contents** controls the optional parts of the document: charts, correlations, reflections, measured data points and, for a scan, parameter evolution. Data tables can be long, so data points are initially left out.

These choices are saved with the project. They do not change which data were fitted.

## Choose output formats

| Format | Use it for |
| --- | --- |
| HTML | An interactive document with pattern zoom, hover and structure controls |
| PDF | A paginated document with static figures |
| CIF | Not available in this version; a structural CIF input is a different document |

The HTML export option can embed the chart libraries for offline use. Without embedding, the document loads those libraries from the web when opened.

The PDF uses A4 pages and light-colour figures. The application writes PDF; Python and Command Line report generation share the report model and settings but do not write that application PDF.

## Save the report

Select the desired formats in **Export**, then choose **Save report**. The files are written to the project's `reports/` directory. The web app also downloads the report files.

Turning off a format leaves any previously saved file in place; it does not delete it.

## Keep saved reports current

Saved reports are listed with their saved time. A report is marked **out of date** when the document the project would produce now differs from it, for example after a fit or a change to Contents. **Missing** means the saved file is no longer present.

Use **Save report** again to bring the selected formats up to date. The status survives reopening the project.

## Save the project too

Saving a project keeps the working model and report settings, but does not generate a new report. Save each for its purpose: the project for continuing the analysis, the report for communicating it.

The same report settings can be used from [Python](../python/reports.md) or [the Command Line](../cli/reports.md).
