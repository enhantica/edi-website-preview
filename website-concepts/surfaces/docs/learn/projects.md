# Projects and experiments

A project is the complete analysis you open, change and save. It connects a model of the sample to one or more experiments, records the fitting settings, and keeps the results and reports with their inputs.

## The analysis workflow

The same sequence applies in the app, a script and a terminal:

1. **Project:** organise the analysis and identify its inputs.
2. **Structure:** describe the unit cell, symmetry and atom sites of the sample.
3. **Experiment:** describe the measurement, instrument, profile and background, and link the structures that contribute.
4. **Analysis:** calculate a pattern or refine selected parameters against measured data.
5. **Report:** review and export the model and its results.

You can revisit any step. For example, a systematic residual may lead you back to the background or instrument settings before the next fit.

## Structures

A structure describes the crystalline material: its space group, unit cell and atom sites, including positions, occupancies and displacement parameters.

A project may contain several structures. Each experiment links to the structures that contribute to its calculated intensity, with a scale for each link. This allows an experiment to represent a mixture of crystalline phases.

Structure parameters describe the sample. A peak-profile width or an instrument zero shift belongs to an experiment, even though changing it also changes the calculated pattern.

## Experiments

An experiment brings together the information needed to calculate a measurement:

- the experiment type and its independent variable, such as scattering angle or time of flight;
- instrument and peak-profile settings;
- background and excluded regions;
- measured intensities and uncertainties, or a calculation range;
- links to the contributing structures.

An experiment with a calculation range and no measured observations is a simulation. Once measured data are present, it can take part in a fit. A project may contain experiments of both kinds.

## Analysis settings

The analysis records which [parameters](parameters.md) may vary, the minimizer conditions, and the [fitting mode](fitting-modes.md). A joint fit shares structure information between experiments; a scan follows the datasets of an experiment in an explicitly chosen order.

These settings belong to the saved project. Running the project from a different interface should not require you to reconstruct the scientific model by hand.

## Files and portability

A complete project is stored as a folder containing `project.edi` and the associated `structures/`, `experiments/`, `analysis/` and `reports/` content. It can also be packaged as a `.zip` archive.

Use the full folder or archive when handing the analysis to someone else. A standalone structural CIF does not contain all the measurement and fitting information of a complete project. See [data formats](data-formats.md).

## Results and reports

Saving the project preserves its model and settings. Exporting a report produces a separate document for inspection or sharing. These are different actions: a report is useful evidence of a result, while the project is what you reopen to continue the analysis.

For interface details, see [projects and files in the app](../application/projects.md), [loading a project in Python](../python/fit.md), or [running it from the command line](../cli/fit.md).

---

Sources: [legacy analysis workflow](https://github.com/easyscience/diffraction-lib/blob/master/docs/docs/user-guide/analysis-workflow/index.md), [complete-project loading](https://github.com/enhantica/edi/blob/main/docs/user/guides/complete-project-loading.md), [opening, saving and exporting](https://github.com/enhantica/edi/blob/main/docs/user/guides/open-save-and-export.md).
