# Analysis workflow

A complete EasyDiffraction analysis connects the model of a sample with an experiment and keeps the decisions that produced the result. Follow these stages in any interface.

| Stage | Scientific task | Ready to continue when… |
| --- | --- | --- |
| [Project](project.md) | Organise the analysis, inputs and provenance | You can identify the measurement, model and starting conditions |
| [Structure](structure.md) | Describe the crystalline phase or phases | Symmetry, cell and atom sites represent your intended sample model |
| [Experiment](experiment.md) | Describe the observations and how they are calculated | Data or a simulation range, instrument, profile, background and structure links are consistent |
| [Analysis](analysis.md) | Calculate, refine and assess | The result has been inspected against the observations and physical model |
| [Report](report.md) | Communicate and retain the result | The report matches the saved model and the complete project is retained |

## Revisit the model

These stages are connected rather than a one-way checklist. A shifted peak may lead back to the cell or instrument calibration. An unmodelled peak may require checking the phases or measurement history. Review the starting calculation before adding more free parameters.

## Calculate or refine

A simulation uses a calculation range without measured observations. A refinement uses measured data and their uncertainties. A project can include both kinds of experiments; calculation and fitting use them according to their roles.

## Choose how to carry it out

| Interface | What its section provides |
| --- | --- |
| [Application](../../application/index.md) | Workspace, imports, parameter controls, fit progress and visual inspection |
| [Python](../../python/index.md) | Project objects, parameter access, analysis calls and result objects |
| [Command Line](../../cli/index.md) | Commands for saved projects, output options and automation |

The scientific explanations belong here; the interface pages link back to them as needed.


---

Sources: [earlier library guide](https://github.com/easyscience/diffraction-lib/blob/master/docs/docs/user-guide/analysis-workflow/index.md), [current edi guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/complete-project-loading.md).
