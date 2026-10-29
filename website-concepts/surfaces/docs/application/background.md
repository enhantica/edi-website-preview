# Background and excluded regions

A background describes the smooth intensity beneath the diffraction peaks. An excluded region removes a measurement interval from the fit. They solve different problems and should be chosen deliberately.

## Choose a background representation

The application supports line-segment backgrounds, represented by points, and polynomial or Chebyshev backgrounds, represented by terms. The **Background** group shows the values for the current experiment.

Changing the background type replaces its representation; review the confirmation before removing points or terms you want to keep.

## Estimate the background

On **Experiment**, choose **Estimate** in the **Background** group. The estimate replaces the current points or terms. Undo brings the previous values back.

The **estimation mode** controls what happens next:

- **Manual** keeps the current values for editing. Estimate runs when you ask for it.
- **Auto** estimates again when the measured data or estimation settings change. The table shows the estimated values; choose manual to edit them.

You can still free or fix a value through its context menu.

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

## A practical sequence

1. Load the data and estimate the background while the model is still rough.
2. Fit the structure and profile, keeping the background fixed or freeing selected background values.
3. Inspect the residual and estimate again if the improved model makes the background clearer.

## Exclude an interval

Use **Excluded regions** on the Experiment page to declare intervals that should not be fitted. Check the boundaries against the pattern. An excluded region remains a deliberate omission from the analysis; it does not repair the model of that interval.

Save the project to keep its background settings and excluded regions.
