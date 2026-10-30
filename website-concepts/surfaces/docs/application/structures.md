---
template: gui.html
---

# :material-puzzle: Work with structures

A structure describes the crystal model used to calculate diffraction: its symmetry, unit cell, atom sites and displacement parameters. The **Structure** page displays one selected structure at a time.

The shared [Structure](../user-guide/analysis-workflow/structure.md) chapter explains the scientific model; the steps below describe this interface.

## Load, create or duplicate

The **Structures** group lists the structures in the project.

- **Load structure from file** reads a CIF or `.edi` structure file.
- **Create structure** adds a starting structure you can edit into your model.
- **Duplicate structure** adds a copy of the selected structure; the copy is not automatically linked to an experiment.

Select a row to make that structure current. You can edit its name or remove it from the list. Removing a structure also removes its links from experiments; Undo restores that change.

<!-- gui-guide:load-create-or-duplicate -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-create.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Load, create or duplicate a structure"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Load, create or duplicate a structure"><title>Load, create or duplicate a structure</title><defs><clipPath id="gui-clip-guide-structure-create-overview-structures-load-create-or-duplicate-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-create.png" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-create-overview-structures-load-create-or-duplicate-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-create-overview-structures-load-create-or-duplicate-0-1" data-gui-parts="[[784,260,334,39]]" d="M782.000 258.000 L1120.000 258.000 L1120.000 301.000 L782.000 301.000 Z" /><path class="" data-gui-region="guide-structure-create-overview-structures-load-create-or-duplicate-0-2" data-gui-parts="[[1132,260,334,39]]" d="M1130.000 258.000 L1468.000 258.000 L1468.000 301.000 L1130.000 301.000 Z" /><path class="" data-gui-region="guide-structure-create-overview-structures-load-create-or-duplicate-0-3" data-gui-parts="[[784,313,334,39]]" d="M782.000 311.000 L1120.000 311.000 L1120.000 354.000 L782.000 354.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>
<figcaption>Load, create or duplicate a structure.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-structure-create-overview-structures-load-create-or-duplicate-0-1" aria-pressed="true">1. Load structure</button> Import the structure file for this example.</li><li><button type="button" data-gui-target="guide-structure-create-overview-structures-load-create-or-duplicate-0-2" aria-pressed="false">2. Create structure</button> Add a starting structure to edit.</li><li><button type="button" data-gui-target="guide-structure-create-overview-structures-load-create-or-duplicate-0-3" aria-pressed="false">3. Duplicate structure</button> Copy the selected structure.</li></ol>
</figure>
<!-- /gui-guide -->

## Space group and setting

The **Space group** group shows the crystal system and the selected space-group setting. The number, Hermann–Mauguin name and coordinate-system code describe that same setting and update together.

Choose the setting used by your structural model. Symmetry affects which cell values and atomic coordinates are independent, so a value controlled by symmetry should not be treated as a separately adjustable parameter.

<!-- gui-guide:space-group-and-setting -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-symmetry.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Choose the crystal symmetry and setting"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Choose the crystal symmetry and setting"><title>Choose the crystal symmetry and setting</title><defs><clipPath id="gui-clip-guide-structure-symmetry-overview-structures-space-group-and-setting-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-symmetry.png" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-symmetry-overview-structures-space-group-and-setting-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-symmetry-overview-structures-space-group-and-setting-0-1" data-gui-parts="[[955.375,210,167.875,56]]" d="M953.375 208.000 L1125.250 208.000 L1125.250 268.000 L953.375 268.000 Z" /><path class="" data-gui-region="guide-structure-symmetry-overview-structures-space-group-and-setting-0-2" data-gui-parts="[[1126.75,210,167.875,56]]" d="M1124.750 208.000 L1296.625 208.000 L1296.625 268.000 L1124.750 268.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>
<figcaption>Choose the crystal symmetry and setting.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-structure-symmetry-overview-structures-space-group-and-setting-0-1" aria-pressed="true">1. Space-group number</button> Select the symmetry of your model.</li><li><button type="button" data-gui-target="guide-structure-symmetry-overview-structures-space-group-and-setting-0-2" aria-pressed="false">2. Space-group symbol</button> Check the Hermann-Mauguin symbol and setting.</li></ol>
</figure>
<!-- /gui-guide -->

## Unit cell

The **Cell** group contains cell lengths and angles. Enter values consistent with the selected symmetry and the physical units shown beside each field.

<!-- gui-guide:unit-cell -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-cell.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Inspect the unit-cell parameters"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Inspect the unit-cell parameters"><title>Inspect the unit-cell parameters</title><defs><clipPath id="gui-clip-guide-structure-cell-overview-structures-unit-cell-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-cell.png" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-cell-overview-structures-unit-cell-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-cell-overview-structures-unit-cell-0-1" data-gui-parts="[[784,252,110.75,56]]" d="M782.000 250.000 L896.750 250.000 L896.750 310.000 L782.000 310.000 Z" /><path class="" data-gui-region="guide-structure-cell-overview-structures-unit-cell-0-2" data-gui-parts="[[898.25,252,110.75,56]]" d="M896.250 250.000 L1011.000 250.000 L1011.000 310.000 L896.250 310.000 Z" /><path class="" data-gui-region="guide-structure-cell-overview-structures-unit-cell-0-3" data-gui-parts="[[1012.5,252,110.75,56]]" d="M1010.500 250.000 L1125.250 250.000 L1125.250 310.000 L1010.500 310.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>
<figcaption>Inspect the unit-cell parameters.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-structure-cell-overview-structures-unit-cell-0-1" aria-pressed="true">1. Cell length a</button> Inspect the cell length and its uncertainty.</li><li><button type="button" data-gui-target="guide-structure-cell-overview-structures-unit-cell-0-2" aria-pressed="false">2. Cell length b</button> Values controlled by symmetry are linked.</li><li><button type="button" data-gui-target="guide-structure-cell-overview-structures-unit-cell-0-3" aria-pressed="false">3. Cell length c</button> Use the cell convention of the selected space group.</li></ol>
</figure>
<!-- /gui-guide -->

## Atom sites

The **Atom sites** table describes each site's label, element, fractional position, occupancy and displacement-parameter representation. It also identifies its Wyckoff position. The selected symmetry can fix a coordinate or relate it to another coordinate.

Use the atom-site controls to add or duplicate a site when building a model. Check the resulting occupancy and displacement parameters as well as the position.

<!-- gui-guide:atom-sites -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-atoms.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Inspect atom sites, coordinates and occupancies"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Inspect atom sites, coordinates and occupancies"><title>Inspect atom sites, coordinates and occupancies</title><defs><clipPath id="gui-clip-guide-structure-atoms-overview-structures-atom-sites-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-atoms.png" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-atoms-overview-structures-atom-sites-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-atoms-overview-structures-atom-sites-0-1" data-gui-parts="[[784,294,682,156]]" d="M782.000 292.000 L1468.000 292.000 L1468.000 452.000 L782.000 452.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>
<figcaption>Inspect atom sites, coordinates and occupancies.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-structure-atoms-overview-structures-atom-sites-0-1" aria-pressed="true">1. Atom sites</button> Inspect atom types, fractional coordinates and occupancies.</li></ol>
</figure>
<!-- /gui-guide -->

## Link the structure to an experiment

A structure contributes to an experiment only when that experiment links to it. On **Experiment**, the **Linked structures** group shows the participating structures and their scales.

The link can be disabled while remaining in the project. A disabled link is kept when saving but contributes to neither calculation nor fitting. See [experiments](experiments.md).

<!-- gui-guide:link-the-structure-to-an-experiment -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-links.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Link structures and inspect phase scales"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Link structures and inspect phase scales"><title>Link structures and inspect phase scales</title><defs><clipPath id="gui-clip-guide-experiment-links-overview-structures-link-the-structure-to-an-experiment-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-links.png" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-links-overview-structures-link-the-structure-to-an-experiment-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-links-overview-structures-link-the-structure-to-an-experiment-0-1" data-gui-parts="[[784,378.00000000000614,682,78]]" d="M782.000 376.000 L1468.000 376.000 L1468.000 458.000 L782.000 458.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>
<figcaption>Link structures and inspect phase scales.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-links-overview-structures-link-the-structure-to-an-experiment-0-1" aria-pressed="true">1. Linked structures</button> Inspect phase links, scales and derived fractions.</li></ol>
</figure>
<!-- /gui-guide -->

## Refine selected values

Use the **Analysis** parameter table to choose which independent structural parameters vary. Begin with a model that describes the main pattern before freeing every available value.

<!-- gui-guide:refine-selected-values -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Completed Rietveld refinement — Main"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Completed Rietveld refinement — Main"><title>Completed Rietveld refinement — Main</title><defs><clipPath id="gui-clip-13-analysis-basic-overview-structures-refine-selected-values-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-overview-structures-refine-selected-values-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-overview-structures-refine-selected-values-0-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-structures-refine-selected-values-0-2" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path class="" data-gui-region="13-analysis-basic-overview-structures-refine-selected-values-0-3" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /><path data-gui-navigation data-gui-parts="[[812.359375,0,67.84375,77]]" d="M810.359 -2.000 L882.203 -2.000 L882.203 79.000 L810.359 79.000 Z" /></svg></a>
<figcaption>Completed Rietveld refinement — Main.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="13-analysis-basic-overview-structures-refine-selected-values-0-1" aria-pressed="true">1. Main workspace</button> Inspect the analysis view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-structures-refine-selected-values-0-2" aria-pressed="false">2. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li><li><button type="button" data-gui-target="13-analysis-basic-overview-structures-refine-selected-values-0-3" aria-pressed="false">3. Status bar</button> Read project counts, messages, calculation and fitting state here.</li></ol>
</figure>
<!-- /gui-guide -->

## Related Physics

[Unit cell and symmetry](../physics/crystallography.md#eq-cell-metric) · [Occupancy and scattering](../physics/diffraction.md#eq-nuclear-structure-factor) · [Atomic displacement](../physics/displacement.md#eq-anisotropic-adp).
