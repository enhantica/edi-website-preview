# Parameters

Parameters describe both the sample and the experiment. Changing a cell length moves calculated reflections; changing a scale changes their contribution to intensity; changing a background coefficient changes the signal underneath the peaks.

## A value and its context

A parameter's value needs its name, units and place in the model to be meaningful. Typical groups include:

| Group | Examples | What to check |
| --- | --- | --- |
| Unit cell | Lengths and angles | Units, symmetry and plausible geometry |
| Atom sites | Fractional coordinates and occupancies | Site meaning, symmetry restrictions and composition |
| Displacements | Isotropic or anisotropic displacement parameters | Convention, units and physical interpretation |
| Instrument and profile | Calibration shifts and peak-width terms | Instrument geometry and profile definition |
| Background and scale | Background points or terms, phase scales | Baseline behaviour and how phases contribute |

The [project model](projects.md) keeps structure quantities separate from experiment quantities. They may still be correlated in a fit.

## Free and fixed

A **free** parameter is allowed to change during refinement. A **fixed** parameter contributes to the calculation but keeps the value you supplied.

In the application, inspect the variation flags on the Analysis page. Free only the quantities that the present observations can usefully determine. In Python, the project's `free_parameters` collection provides the parameters currently selected for refinement:

```python
import edi

project = edi.Project.load('path/to/project')
for parameter in project.free_parameters:
    print(parameter.name, parameter.value, parameter.units)
```

The command line runs the free-parameter choices saved in the project. It does not require a second list of free parameters on the command itself.

## Uncertainties

A fitted parameter may have a standard uncertainty. Interpret it together with the measurement uncertainties, the model and correlations with other parameters.

A small standard uncertainty describes precision under the fit's assumptions. It does not remove uncertainty from calibration, sample effects, missing phases, an unsuitable background, or another systematic source.

See [fit quality](fit-quality.md) for how parameter uncertainties relate to agreement factors and the residual.

## Constraints and symmetry

Some values are related by the crystallographic symmetry; others may be linked by a declared constraint. Such values are not independent fitting directions.

For example, a symmetry restriction on a coordinate cannot be treated as an arbitrary free coordinate simply because a table displays it. Inspect the relationship before interpreting how many independently variable quantities the fit has.

## Bounds and starting values

Use meaningful starting values. A fit begins at the project's current parameter values, and its final state can depend on that starting point.

The minimum and maximum displayed in the app describe the values the model accepts. They are model-admissibility information; the app does not expose them as controls for setting an optimiser's search interval.

When interpreting a constrained or limited value, check the applicable model and fitting settings. A result reaching a permitted limit can be a reason to inspect the starting assumptions, observations and parameter correlations.

For scan analyses, the [fitting mode](fitting-modes.md) determines whether each dataset starts from the same template values or from the previous fit.

## Names in code and files

A parameter can have a Python access path, an Edi persistence key, and a scientific CIF report name. These have different jobs. Use the current [Python documentation](../python/index.md) for code and [data formats](data-formats.md) for saved files; do not assume a name from an older library release is an interchangeable API.

---

Sources: [earlier parameter guide](https://github.com/easyscience/diffraction-lib/blob/master/docs/docs/user-guide/parameters.md), [edi project loading and free-set contract](https://github.com/enhantica/edi/blob/main/docs/user/guides/complete-project-loading.md), [current example tutorial](https://github.com/enhantica/edi/blob/main/docs/user/tutorials/pd-neut-cwl_lbco-hrpt.py).
