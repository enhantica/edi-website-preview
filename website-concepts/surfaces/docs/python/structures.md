# :material-puzzle: Structures and parameters

A structure describes the crystal: its symmetry, unit-cell geometry and atom sites. Experiments link the structures that contribute to their calculated data.

The shared [Structure](../user-guide/analysis-workflow/structure.md) chapter explains the scientific model; the steps below describe this interface.

## Inspect a loaded structure

```python
import edi

project = edi.Project.load('path/to/project')

for structure in project.structures:
    print(structure.name)
    print(structure.space_group.name_h_m)
    print(structure.cell.length_a.value)
```

[Cell lengths and angles](../physics/crystallography.md#eq-cell-metric) are parameters with values. A space-group name selects symmetry; it is not a floating-point fit parameter.

## Read and change a parameter

For a project with at least one structure:

```python
structure = project.structures[0]
length_a = structure.cell.length_a

print(length_a.value)
print(length_a.free)
length_a.free = True
```

The [`free` flag](../physics/minimization.md#eq-jacobian) allows a parameter to vary during refinement. Set it only when that parameter belongs in the scientific model you intend to fit. Shared [parameter concepts](../user-guide/parameters.md) explain values, uncertainties and constraints.

## Inspect the free set

```python
for parameter in project.free_parameters:
    print(parameter.name, parameter.value, parameter.units)
```

This project-level list includes structural and experimental parameters. It helps you review the analysis before running a fit.

## Read a structure file

The current factory supports structure input from CIF or edi text:

```python
structure = edi.StructureFactory.from_cif_path('structure.cif')
```

This creates a structure object; it does not by itself create a complete measurement and analysis project. A successful import also depends on the input carrying the structure information the reader supports.

For a complete runnable analysis, start from a project or a checked example. These pages intentionally document a demonstrated subset rather than claiming that all constructors and file variants are covered.

## Related Physics

[Unit cell and symmetry](../physics/crystallography.md#eq-cell-metric) · [Occupancy and scattering](../physics/diffraction.md#eq-nuclear-structure-factor) · [Atomic displacement](../physics/displacement.md#eq-anisotropic-adp).


[Compare Python paths with GUI labels, Edi keys and CIF names](../user-guide/parameter-reference.md).
