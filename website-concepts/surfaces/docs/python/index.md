# Diffraction analysis in Python

Use `edi` to calculate patterns, refine a structural model and prepare a report from a script or notebook. The Python library uses the same project model as the application and command line.

## A complete analysis

Start from a complete project, inspect its model, run the analysis it declares, and save the result where you choose.

```python
import edi

project = edi.Project.load('path/to/project')
result = project.analysis.fit()
print(result.rwp, result.reduced_chi_square)

project.save_as('refined-project')
project.report.save_html('refinement.html', offline=True)
```

This example is a measured-data refinement. A simulation project can [calculate a pattern](calculate.md) without measured data.

## Follow the workflow

| What you want to do | Start here |
| --- | --- |
| Prepare Python or a notebook | [Setup](setup.md) |
| Open a folder, `project.edi` or archive | [Load and save projects](projects.md) |
| Inspect the structural model | [Structures and parameters](structures.md) |
| Inspect the measurement and its model | [Experiments and data](experiments.md) |
| Calculate from the current model | [Calculate a pattern](calculate.md) |
| Refine against measured data | [Load and fit a project](fit.md) |
| Inspect fit values and uncertainties | [Read the result](results.md) |
| Export an interactive report | [Reports](reports.md) |
| Look up the calls used in these pages | [Python reference](reference.md) |

## One project across interfaces

You can reopen the saved project in [the application](../application/index.md), or run it with [the CLI](../cli/index.md). The [shared concepts](../learn/projects.md) explain structures, experiments and analysis independently of the interface.

---

Sources: organization adapted from the [earlier library quick reference](https://docs.easydiffraction.org/lib/latest/quick-reference/); current calls checked against [edi's Python facade](https://github.com/enhantica/edi/blob/main/lib/edi/__init__.py) and [LBCO tutorial source](https://github.com/enhantica/edi/blob/main/docs/user/tutorials/pd-neut-cwl_lbco-hrpt.py).
