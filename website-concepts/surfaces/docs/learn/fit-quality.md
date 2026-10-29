# Assessing a fit

Judge a fit using the pattern, the residual, the fitted parameters and the agreement factors together. A successful optimisation is the beginning of that assessment.

## Inspect the signal and residual

Compare the measured and calculated intensities over the full range, then inspect individual peaks and regions that disagree.

- Are peak positions aligned?
- Do widths and shapes agree across the range?
- Does the model account for the observed peaks?
- Is the baseline appropriate between and under peaks?
- Does the residual contain a repeated or systematic pattern?

Reflection marks show where the structures predict Bragg positions. They help connect a profile disagreement to the contributing phases, but they do not explain every source of intensity in the measurement.

## Understand the agreement factors

For a powder profile, the principal factors compare observed intensities `yₒ` with calculated intensities `y꜀`. The weights use the observations' standard uncertainties, `w = 1/σ²`.

| Quantity | What it describes |
| --- | --- |
| R<sub>p</sub> | The summed absolute profile difference, relative to summed observed intensity |
| R<sub>wp</sub> | The weighted profile difference, normalised by the weighted observed intensity |
| R<sub>exp</sub> | The expected weighted factor for the observations and number of independent free parameters |
| Reduced χ² | The weighted squared residual per degree of freedom |

EasyDiffraction's example-comparison guide computes reduced χ² as `Σw(yₒ − y꜀)² / (N − P)`, where `N` is the number of observations and `P` the number of free parameters.

There is no universal R-factor threshold that makes every model acceptable. Data range, excluded regions, noise estimates, background, instrument resolution and the model itself affect the value.

## Check parameters and correlations

Inspect whether the result makes physical sense. Review free parameters, their uncertainties, correlations and any values that have reached their bounds.

Strong correlations can mean that several parameter combinations explain similar changes in the observations. Treat individual uncertainties and changes with care in that situation. Changing the data range or constraints changes the question the fit answers.

## Distinguish termination from correctness

Read how the minimizer ended. Reaching an iteration limit is different from satisfying its convergence condition. A converged fit may still describe an unsuitable structure or an instrument setting incorrectly.

Keep the starting model and minimizer conditions with the result so another person can repeat the same optimisation.

## Compare results fairly

A meaningful comparison between programs needs matching observations, structures, background, profile, excluded regions, free parameters and starting conditions.

The current [edi comparison tables](https://github.com/enhantica/edi/blob/main/docs/user/guides/fit-quality.md) recompute profile factors from saved observed and calculated curves on a common set of points. They also identify cases where the programs express different models. Those cases need their stated qualification rather than an unlabelled numerical ranking.

Single-crystal examples fit reflection observations rather than a powder profile. Read their example-specific references instead of applying powder-profile factors without checking the observation model.

## Keep an account of the analysis

Save both the project and an appropriate [report](../application/reports.md). Include enough information to identify the measured data, structure model, fitting mode, free set, excluded regions, software version and minimizer conditions.

For a scan, inspect failed datasets and out-of-date results before interpreting parameter evolution. See [fitting modes](fitting-modes.md).

---

Sources: [edi fit-quality definitions, comparison method and references](https://github.com/enhantica/edi/blob/main/docs/user/guides/fit-quality.md), [report guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/the-report.md), [scan guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/sequential-fitting-in-the-app.md).
