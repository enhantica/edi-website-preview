---
template: physics.html
---

# Rietveld refinement

Rietveld refinement compares a calculated powder pattern with measured intensities over the included observations. It refines a crystallographic model together with the relevant experiment parameters.

## Calculated powder pattern {#eq-rietveld-pattern}

A useful decomposition is

$$
y_i^{\rm calc}=b(x_i)+\sum_p s_p\sum_{h\in p}m_h\,L_h\,P_h\,A_h\,O_h\,|F_h|^2\,\Omega_p(x_i-x_h).
$$

Here $p$ labels a linked phase, $s_p$ its scale, $h$ a reflection, $m_h$ multiplicity, $L_h$ the geometry-dependent Lorentz factor, $P_h$ polarization where applicable, $A_h$ absorption, $O_h$ preferred orientation, $F_h$ the structure factor, $\Omega$ the selected peak profile and $b$ the background. This is a model decomposition: factors that do not apply to the selected experiment are unity, and instrument-specific intensity-unit conventions are carried with its scale.

Follow the terms to [crystallography](crystallography.md), [scattering](diffraction.md), [profiles](profiles.md), [absorption](corrections/absorption.md), [orientation](corrections/orientation.md), [Lorentz/polarization](corrections/intensity.md) and [background](background.md). Single-crystal reflection calculations use the corresponding integrated-intensity model, not a powder-profile sum.

## Least-squares objective {#eq-weighted-residual}

$$
r_i(\mathbf p)=\frac{y_i^{\rm calc}(\mathbf p)-y_i^{\rm obs}}{\sigma_i},\qquad
S(\mathbf p)=\sum_{i\in\mathcal I}r_i^2.
$$

$\mathcal I$ is the included observation set and $\sigma_i>0$ its standard uncertainty. Reversing every residual's sign leaves $S$ unchanged. The displayed observed-minus-calculated difference curve can therefore have the opposite sign to the solver residual.

Only independent free parameters are optimisation variables. Symmetry, constraints, the selected experiment and model type determine which quantities are independent and affect the observations. See [minimization](minimization.md).

## Single and joint fitting {#joint-refinement}

A single fit uses one experiment. A joint fit combines the residuals of several experiments, sharing their common structural quantities while retaining experiment-specific terms. If experiment weights $v_e$ are applied, its residual block is multiplied by $\sqrt{v_e}$ and its objective contribution by $v_e$.

Inspect each experiment after a joint fit. Combined agreement can hide a systematic mismatch in one dataset. [Reliability factors](reliability.md) distinguish per-experiment and pooled summaries.

## Sequential and independent scans {#scan-refinement}

Both scan modes run a sequence of fits against a template experiment. Sequential fitting starts the next dataset from the preceding result; independent fitting restarts each dataset from the same template state. The distinction is the starting model, not parallel execution. See the [fitting-mode guide](../user-guide/fitting-modes.md).

## Interpretation

Refinement improves agreement under the model and its uncertainties. Convergence does not establish that the phase model, background, calibration or uncertainty estimates are correct. Use the [practical fit assessment](../user-guide/fit-quality.md) and retain the starting project.

## References

McCusker, Von Dreele, Cox, Louër & Scardi (1999), *Rietveld refinement guidelines*, J. Appl. Cryst. 32, 36–50. The operative objective and conventions are specified by this reference and its [model catalogue](models.md).
