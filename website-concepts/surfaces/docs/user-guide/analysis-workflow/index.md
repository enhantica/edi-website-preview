# Analysis workflow

A complete EasyDiffraction analysis connects the model of a sample with an experiment and keeps the decisions that produced the result. Follow these stages in any interface.

<svg viewBox="0 0 760 105" role="img" aria-labelledby="workflow-title" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;color:var(--md-default-fg-color)">
<title id="workflow-title">Project, Structure, Experiment, Analysis, Report. Revisit earlier stages when assessing the fit.</title>
<defs><marker id="workflow-arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 6 3 0 6" fill="#0084c7"/></marker></defs>
<a href="project/"><rect x="4" y="12" width="136" height="50" rx="5" fill="#0084c7" fill-opacity=".07" stroke="#0084c7"/><text x="72" y="42" fill="currentColor" text-anchor="middle" font-size="16">Project</text></a>
<path d="M141 37h13" stroke="#0084c7" marker-end="url(#workflow-arrow)"/>
<a href="structure/"><rect x="156" y="12" width="136" height="50" rx="5" fill="#0084c7" fill-opacity=".07" stroke="#0084c7"/><text x="224" y="42" fill="currentColor" text-anchor="middle" font-size="16">Structure</text></a>
<path d="M293 37h13" stroke="#0084c7" marker-end="url(#workflow-arrow)"/>
<a href="experiment/"><rect x="308" y="12" width="136" height="50" rx="5" fill="#0084c7" fill-opacity=".07" stroke="#0084c7"/><text x="376" y="42" fill="currentColor" text-anchor="middle" font-size="16">Experiment</text></a>
<path d="M445 37h13" stroke="#0084c7" marker-end="url(#workflow-arrow)"/>
<a href="analysis/"><rect x="460" y="12" width="136" height="50" rx="5" fill="#0084c7" fill-opacity=".07" stroke="#0084c7"/><text x="528" y="42" fill="currentColor" text-anchor="middle" font-size="16">Analysis</text></a>
<path d="M597 37h13" stroke="#0084c7" marker-end="url(#workflow-arrow)"/>
<a href="report/"><rect x="612" y="12" width="136" height="50" rx="5" fill="#0084c7" fill-opacity=".07" stroke="#0084c7"/><text x="680" y="42" fill="currentColor" text-anchor="middle" font-size="16">Report</text></a>
</svg>

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
| [CLI](../../cli/index.md) | Commands for saved projects, output options and automation |

The scientific explanations belong here; the interface pages link back to them as needed.
