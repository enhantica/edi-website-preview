---
template: gui.html
---

# :material-clipboard-text: Review and save a report

The **Report** page presents structures, experiments, fit information and correlations as one document. The shared [Report](../user-guide/analysis-workflow/report.md) stage explains the document and its relationship to the saved project. This page covers the application controls.

## Review the document

The main view shows the report with its figures and structure views. Inspect it after a fit, particularly the selected experiment, model values and charts.

The sidebar has **Export** and **Contents** groups.

<!-- gui-guide:review-the-document -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/14-report-basic.png?v=1a34e2660cbe" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Review the fitted structure and report — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Review the fitted structure and report — Main"><title>Review the fitted structure and report — Main</title><defs><clipPath id="gui-clip-14-report-basic-overview-reports-review-the-document-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/14-report-basic.png?v=1a34e2660cbe" width="1480" height="800" clip-path="url(#gui-clip-14-report-basic-overview-reports-review-the-document-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="14-report-basic-overview-reports-review-the-document-0-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="14-report-basic-overview-reports-review-the-document-0-2" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="14-report-basic-overview-reports-review-the-document-0-3" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /><path data-gui-navigation data-gui-parts="[[880.203125,0,58.25,77]]" d="M878.203 -2.000 L940.453 -2.000 L940.453 79.000 L878.203 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="14-report-basic-overview-reports-review-the-document-0-1" aria-pressed="true">1. Main workspace</button> Inspect the report view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="14-report-basic-overview-reports-review-the-document-0-2" aria-pressed="false">2. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="14-report-basic-overview-reports-review-the-document-0-3" aria-pressed="false">3. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
</figure>
<!-- /gui-guide -->

## Choose the contents

**Contents** controls the optional parts of the document: charts, correlations, reflections, measured data points and, for a scan, parameter evolution. Data tables can be long, so data points are initially left out.

These choices are saved with the project. They do not change which data were fitted.

<!-- gui-guide:choose-the-contents -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-report-contents.png?v=d7d709216e15" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Choose which sections appear in the report"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Choose which sections appear in the report"><title>Choose which sections appear in the report</title><defs><clipPath id="gui-clip-guide-report-contents-overview-reports-choose-the-contents-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-report-contents.png?v=d7d709216e15" width="1480" height="800" clip-path="url(#gui-clip-guide-report-contents-overview-reports-choose-the-contents-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-report-contents-overview-reports-choose-the-contents-0-1" data-gui-parts="[[770,161,710,189]]" d="M768.000 159.000 L1482.000 159.000 L1482.000 352.000 L768.000 352.000 Z" /><path data-gui-navigation data-gui-parts="[[880.203125,0,58.25,77]]" d="M878.203 -2.000 L940.453 -2.000 L940.453 79.000 L878.203 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-report-contents-overview-reports-choose-the-contents-0-1" aria-pressed="true">1. <span class="gui-fa" aria-hidden="true">&#61498;</span>Contents</button> </li></ol>
</figure>
<!-- /gui-guide -->

## Choose output formats

| Format | Use it for |
| --- | --- |
| HTML | An interactive document with pattern zoom, hover and structure controls |
| PDF | A paginated document with static figures |
| CIF | Not available in this version; a structural CIF input is a different document |

The HTML export option can embed the chart libraries for offline use. Without embedding, the document loads those libraries from the web when opened.

The PDF uses A4 pages and light-colour figures. The application writes PDF; Python and Command Line report generation share the report model and settings but do not write that application PDF.

<!-- gui-guide:choose-output-formats -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-report-export.png?v=8d21fb91bca1" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Choose report formats and export"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Choose report formats and export"><title>Choose report formats and export</title><defs><clipPath id="gui-clip-guide-report-export-overview-reports-choose-output-formats-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-report-export.png?v=8d21fb91bca1" width="1480" height="800" clip-path="url(#gui-clip-guide-report-export-overview-reports-choose-output-formats-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-report-export-overview-reports-choose-output-formats-0-1" data-gui-parts="[[784,175,70.46875,21]]" d="M782.000 173.000 L856.469 173.000 L856.469 198.000 L782.000 198.000 Z" /><path class="" data-gui-region="guide-report-export-overview-reports-choose-output-formats-0-2" data-gui-parts="[[784,224,70.46875,21]]" d="M782.000 222.000 L856.469 222.000 L856.469 247.000 L782.000 247.000 Z" /><path class="" data-gui-region="guide-report-export-overview-reports-choose-output-formats-0-3" data-gui-parts="[[784,273,70.46875,21]]" d="M782.000 271.000 L856.469 271.000 L856.469 296.000 L782.000 296.000 Z" /><path class="" data-gui-region="guide-report-export-overview-reports-choose-output-formats-0-4" data-gui-parts="[[784,315,682,39]]" d="M782.000 313.000 L1468.000 313.000 L1468.000 356.000 L782.000 356.000 Z" /><path data-gui-navigation data-gui-parts="[[880.203125,0,58.25,77]]" d="M878.203 -2.000 L940.453 -2.000 L940.453 79.000 L878.203 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-report-export-overview-reports-choose-output-formats-0-1" aria-pressed="true">1. HTML report</button> Select an HTML document.</li><li><button type="button" data-gui-target="guide-report-export-overview-reports-choose-output-formats-0-2" aria-pressed="false">2. PDF report</button> Select a PDF document.</li><li><button type="button" data-gui-target="guide-report-export-overview-reports-choose-output-formats-0-3" aria-pressed="false">3. CIF report</button> Select a crystallographic report.</li><li><button type="button" data-gui-target="guide-report-export-overview-reports-choose-output-formats-0-4" aria-pressed="false">4. <span class="gui-fa" aria-hidden="true">&#61465;</span>Save report</button> Write the selected report formats.</li></ol>
</figure>
<!-- /gui-guide -->

## Save the report

Select the desired formats in **Export**, then choose **Save report**. The files are written to the project's `reports/` directory. The web app also downloads the report files.

Turning off a format leaves any previously saved file in place; it does not delete it.

<!-- gui-guide:save-the-report -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-report-saved.png?v=87be6c625530" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Review the saved report status"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Review the saved report status"><title>Review the saved report status</title><defs><clipPath id="gui-clip-guide-report-saved-overview-reports-save-the-report-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-report-saved.png?v=87be6c625530" width="1480" height="800" clip-path="url(#gui-clip-guide-report-saved-overview-reports-save-the-report-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-report-saved-overview-reports-save-the-report-0-1" data-gui-parts="[[770,119,710,249]]" d="M768.000 117.000 L1482.000 117.000 L1482.000 370.000 L768.000 370.000 Z" /><path data-gui-navigation data-gui-parts="[[880.203125,0,58.25,77]]" d="M878.203 -2.000 L940.453 -2.000 L940.453 79.000 L878.203 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-report-saved-overview-reports-save-the-report-0-1" aria-pressed="true">1. <span class="gui-fa" aria-hidden="true">&#61465;</span>Export</button> </li></ol>
</figure>
<!-- /gui-guide -->

## Keep saved reports current

Saved reports are listed with their saved time. A report is marked **out of date** when the document the project would produce now differs from it, for example after a fit or a change to Contents. **Missing** means the saved file is no longer present.

Use **Save report** again to bring the selected formats up to date. The status survives reopening the project.

<!-- gui-guide:keep-saved-reports-current -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-report-saved.png?v=87be6c625530" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Review the saved report status"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Review the saved report status"><title>Review the saved report status</title><defs><clipPath id="gui-clip-guide-report-saved-overview-reports-keep-saved-reports-current-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-report-saved.png?v=87be6c625530" width="1480" height="800" clip-path="url(#gui-clip-guide-report-saved-overview-reports-keep-saved-reports-current-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-report-saved-overview-reports-keep-saved-reports-current-0-1" data-gui-parts="[[770,119,710,249]]" d="M768.000 117.000 L1482.000 117.000 L1482.000 370.000 L768.000 370.000 Z" /><path data-gui-navigation data-gui-parts="[[880.203125,0,58.25,77]]" d="M878.203 -2.000 L940.453 -2.000 L940.453 79.000 L878.203 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-report-saved-overview-reports-keep-saved-reports-current-0-1" aria-pressed="true">1. <span class="gui-fa" aria-hidden="true">&#61465;</span>Export</button> </li></ol>
</figure>
<!-- /gui-guide -->

## Save the project too

Saving a project keeps the working model and report settings, but does not generate a new report. Save each for its purpose: the project for continuing the analysis, the report for communicating it.

The same report settings can be used from [Python](../python/reports.md) or [the Command Line](../cli/reports.md).

<!-- gui-guide:save-the-project-too -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-project-save.png?v=de7f11c4d553" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Choose a save format or save a copy"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Choose a save format or save a copy"><title>Choose a save format or save a copy</title><defs><clipPath id="gui-clip-guide-project-save-overview-reports-save-the-project-too-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-project-save.png?v=de7f11c4d553" width="1480" height="800" clip-path="url(#gui-clip-guide-project-save-overview-reports-save-the-project-too-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-project-save-overview-reports-save-the-project-too-0-1" data-gui-parts="[[607,354,111.84375,93]]" d="M605.000 352.000 L720.844 352.000 L720.844 449.000 L605.000 449.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-project-save-overview-reports-save-the-project-too-0-1" aria-pressed="true">1. Save options</button> Choose the output format and whether to save a copy.</li></ol>
</figure>
<!-- /gui-guide -->

## Related Physics

[Agreement factors](../physics/reliability.md) · [Uncertainty and correlations](../physics/minimization.md#eq-covariance).
