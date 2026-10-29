# Work with structures

A structure describes the crystal model used to calculate diffraction: its symmetry, unit cell, atom sites and displacement parameters. The **Structure** page displays one selected structure at a time.

The shared [Structure](../user-guide/analysis-workflow/structure.md) chapter explains the scientific model; the steps below describe this interface.

## Load, create or duplicate

The **Structures** group lists the structures in the project.

- **Load structure from file** reads a CIF or `.edi` structure file.
- **Create structure** adds a starting structure you can edit into your model.
- **Duplicate structure** adds a copy of the selected structure; the copy is not automatically linked to an experiment.

Select a row to make that structure current. You can edit its name or remove it from the list. Removing a structure also removes its links from experiments; Undo restores that change.

## Space group and setting

The **Space group** group shows the crystal system and the selected space-group setting. The number, Hermann–Mauguin name and coordinate-system code describe that same setting and update together.

Choose the setting used by your structural model. Symmetry affects which cell values and atomic coordinates are independent, so a value controlled by symmetry should not be treated as a separately adjustable parameter.

## Unit cell

The **Cell** group contains cell lengths and angles. Enter values consistent with the selected symmetry and the physical units shown beside each field.

## Atom sites

The **Atom sites** table describes each site's label, element, fractional position, occupancy and displacement-parameter representation. It also identifies its Wyckoff position. The selected symmetry can fix a coordinate or relate it to another coordinate.

Use the atom-site controls to add or duplicate a site when building a model. Check the resulting occupancy and displacement parameters as well as the position.

## Link the structure to an experiment

A structure contributes to an experiment only when that experiment links to it. On **Experiment**, the **Linked structures** group shows the participating structures and their scales.

The link can be disabled while remaining in the project. A disabled link is kept when saving but contributes to neither calculation nor fitting. See [experiments](experiments.md).

## Refine selected values

Use the **Analysis** parameter table to choose which independent structural parameters vary. Begin with a model that describes the main pattern before freeing every available value.
