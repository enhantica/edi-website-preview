# From measurement to analysis

EasyDiffraction compares a crystallographic model with diffraction measurements. Understanding where that comparison begins helps you choose suitable inputs and recognise what a fit can establish.

## Acquisition, reduction and analysis

**Acquisition** records the detector response during an experiment. **Reduction** turns those detector measurements into the observations used for analysis, with the relevant corrections and uncertainties. **Analysis** compares those observations with a model of the sample and experiment.

EasyDiffraction focuses on the analysis stage. For a powder experiment, the starting observation is usually an intensity profile against scattering angle or time of flight. Keep the reduction history and experimental context with the project: they affect how its uncertainties and agreement factors should be interpreted.

## A model of the sample and the experiment

The calculated intensity depends on more than atom positions. EasyDiffraction separates the model into two connected parts:

| Part | Describes | Examples |
| --- | --- | --- |
| Structure | The crystalline sample | Unit cell, symmetry, atom sites, occupancies, displacement parameters |
| Experiment | How it is observed | Wavelength or time-of-flight calibration, peak profile, background, scale and excluded regions |

A disagreement between measured and calculated patterns can therefore have several causes. A peak-position error may come from the cell or calibration; a broad mismatch underneath peaks may come from the background; an intensity mismatch can involve the structure as well as experiment settings.

## Calculation before refinement

A calculation predicts the diffraction signal from the current structure and experiment. It does not need measured intensities. Use it to inspect peak positions and the influence of the model before fitting.

A refinement requires observations to compare against. It changes the parameters marked as free in order to improve agreement with those observations. Parameters that remain fixed still contribute to the calculated pattern.

## Refinement is an optimisation problem

A least-squares fit reduces a weighted difference between observations and calculations. The starting model, free-parameter set, constraints, excluded regions and minimizer conditions all influence the result.

Start from a physically meaningful model. Inspect the initial pattern, allow parameters to vary deliberately, and review the result after each meaningful change. Adding more free parameters may reduce a residual without making the model more informative.

## A result needs interpretation

Convergence describes how the optimisation ended. It does not by itself establish that the sample model is correct or that all uncertainty sources have been captured.

Inspect the observed and calculated signal, the residual, parameter uncertainties and correlations, and the physical plausibility of the result. [Fit quality](fit-quality.md) explains these checks in more detail.

## The same ideas in every interface

The app makes these relationships visible. Python lets you express them in a script or notebook. The Command Line runs the analysis already declared by a saved project. All use the same [project model](analysis-workflow/project.md).

---

Sources: [earlier library concepts](https://github.com/easyscience/diffraction-lib/blob/master/docs/docs/user-guide/concept.md), [edi project model](https://github.com/enhantica/edi/blob/main/docs/user/guides/complete-project-loading.md), [edi fit-quality guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/fit-quality.md).
