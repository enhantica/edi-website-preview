---
template: gui.html
---

# :material-microscope: Background and excluded regions

A background describes the smooth intensity beneath the diffraction peaks. An excluded region removes a measurement interval from the fit. They solve different problems and should be chosen deliberately.

## Choose a background representation

The application supports line-segment backgrounds, represented by points, and polynomial or Chebyshev backgrounds, represented by terms. The **Background** group shows the values for the current experiment.

Changing the background type replaces its representation; review the confirmation before removing points or terms you want to keep.

<!-- gui-guide:choose-a-background-representation -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-background.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Inspect the background representation and values"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Inspect the background representation and values"><title>Inspect the background representation and values</title><defs><clipPath id="gui-clip-guide-experiment-background-overview-background-choose-a-background-representation-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-background.png" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-background-overview-background-choose-a-background-representation-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-background-overview-background-choose-a-background-representation-0-1" data-gui-parts="[[784,210,339.25,56]]" d="M782.000 208.000 L1125.250 208.000 L1125.250 268.000 L782.000 268.000 Z" /><path class="" data-gui-region="guide-experiment-background-overview-background-choose-a-background-representation-0-2" data-gui-parts="[[784,210,682,337.5]]" d="M782.000 208.000 L1468.000 208.000 L1468.000 549.500 L782.000 549.500 Z" /></svg></a>
<figcaption>Inspect the background representation and values.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-background-overview-background-choose-a-background-representation-0-1" aria-pressed="true">1. Background model</button> Choose the background representation.</li><li><button type="button" data-gui-target="guide-experiment-background-overview-background-choose-a-background-representation-0-2" aria-pressed="false">2. Background values</button> Inspect or edit the values in the selected representation.</li></ol>
</figure>
<!-- /gui-guide -->

## Estimate the background

On **Experiment**, choose **Estimate** in the **Background** group. The estimate replaces the current points or terms. Undo brings the previous values back.

The **estimation mode** controls what happens next:

- **Manual** keeps the current values for editing. Estimate runs when you ask for it.
- **Auto** estimates again when the measured data or estimation settings change. The table shows the estimated values; choose manual to edit them.

You can still free or fix a value through its context menu.

<!-- gui-guide:estimate-the-background -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-background.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Inspect the background representation and values"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Inspect the background representation and values"><title>Inspect the background representation and values</title><defs><clipPath id="gui-clip-guide-experiment-background-overview-background-estimate-the-background-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-background.png" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-background-overview-background-estimate-the-background-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-background-overview-background-estimate-the-background-0-1" data-gui-parts="[[784,210,339.25,56]]" d="M782.000 208.000 L1125.250 208.000 L1125.250 268.000 L782.000 268.000 Z" /><path class="" data-gui-region="guide-experiment-background-overview-background-estimate-the-background-0-2" data-gui-parts="[[784,210,682,337.5]]" d="M782.000 208.000 L1468.000 208.000 L1468.000 549.500 L782.000 549.500 Z" /></svg></a>
<figcaption>Inspect the background representation and values.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-background-overview-background-estimate-the-background-0-1" aria-pressed="true">1. Background model</button> Choose the background representation.</li><li><button type="button" data-gui-target="guide-experiment-background-overview-background-estimate-the-background-0-2" aria-pressed="false">2. Background values</button> Inspect or edit the values in the selected representation.</li></ol>
</figure>
<!-- /gui-guide -->

## Estimation settings

The **Extra** tab's **Background** group holds the estimation settings. Leave a field empty to let the estimator choose where that option supports automatic selection.

| Setting | Purpose |
| --- | --- |
| Calculated peaks | Use `auto`, subtract the model's calculated peaks, or ignore them. |
| Anchor points | Control the number of points in a line-segment background. |
| Max terms | Limit the number of polynomial or Chebyshev terms. |
| Baseline method | Select the method used to find the curve under the peaks. |
| Peak width and smoothness | Control the scale on which the baseline is estimated. |
| Noise tolerance | Control how closely the points or terms follow the estimated curve. |

Subtracting calculated peaks can help where peaks overlap and the measured intensity never reaches the background. A poor model can make subtraction misleading. The default `auto` choice checks whether the model is suitable and reports its choice below the settings.

<!-- gui-guide:estimation-settings -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-estimation.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Inspect background estimation settings"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Inspect background estimation settings"><title>Inspect background estimation settings</title><defs><clipPath id="gui-clip-guide-experiment-estimation-overview-background-estimation-settings-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-estimation.png" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-estimation-overview-background-estimation-settings-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-estimation-overview-background-estimation-settings-0-1" data-gui-parts="[[770,119,710,259]]" d="M768.000 117.000 L1482.000 117.000 L1482.000 380.000 L768.000 380.000 Z" /></svg></a>
<figcaption>Inspect background estimation settings.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-estimation-overview-background-estimation-settings-0-1" aria-pressed="true">1. Background Estimate</button> Use the controls in this group.</li></ol>
</figure>
<!-- /gui-guide -->

## A practical sequence

1. Load the data and estimate the background while the model is still rough.
2. Fit the structure and profile, keeping the background fixed or freeing selected background values.
3. Inspect the residual and estimate again if the improved model makes the background clearer.

<!-- gui-guide:a-practical-sequence -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Completed Rietveld refinement — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Completed Rietveld refinement — Main"><title>Completed Rietveld refinement — Main</title><defs><clipPath id="gui-clip-13-analysis-basic-overview-background-a-practical-sequence-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-overview-background-a-practical-sequence-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-overview-background-a-practical-sequence-0-1" data-gui-parts="[[0,0,1480,77]]" d="M-2.000 -2.000 L1482.000 -2.000 L1482.000 79.000 L-2.000 79.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-background-a-practical-sequence-0-2" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-background-a-practical-sequence-0-3" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-background-a-practical-sequence-0-4" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /></svg></a>
<figcaption>Completed Rietveld refinement — Main.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="13-analysis-basic-overview-background-a-practical-sequence-0-1" aria-pressed="true">1. Workflow navigation</button> Move between Home, Project, Structure, Experiment, Analysis and Report.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-background-a-practical-sequence-0-2" aria-pressed="false">2. Main workspace</button> Inspect the analysis view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-background-a-practical-sequence-0-3" aria-pressed="false">3. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-background-a-practical-sequence-0-4" aria-pressed="false">4. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
</figure>
<!-- /gui-guide -->

## Exclude an interval

Use **Excluded regions** on the Experiment page to declare intervals that should not be fitted. Check the boundaries against the pattern. An excluded region remains a deliberate omission from the analysis; it does not repair the model of that interval.

Save the project to keep its background settings and excluded regions.

<!-- gui-guide:exclude-an-interval -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-exclusions.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Inspect excluded fitting intervals"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Inspect excluded fitting intervals"><title>Inspect excluded fitting intervals</title><defs><clipPath id="gui-clip-guide-experiment-exclusions-overview-background-exclude-an-interval-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-exclusions.png" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-exclusions-overview-background-exclude-an-interval-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-exclusions-overview-background-exclude-an-interval-0-1" data-gui-parts="[[784,336,682,117]]" d="M782.000 334.000 L1468.000 334.000 L1468.000 455.000 L782.000 455.000 Z" /></svg></a>
<figcaption>Inspect excluded fitting intervals.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-exclusions-overview-background-exclude-an-interval-0-1" aria-pressed="true">1. Excluded intervals</button> Set the boundaries of regions omitted from fitting.</li></ol>
</figure>
<!-- /gui-guide -->

## Related Physics

[Background equations and estimation](../physics/background.md) · [Excluded observations](../physics/background.md#excluded-regions).
