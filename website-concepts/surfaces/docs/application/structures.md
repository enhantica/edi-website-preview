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
<div class="gui-viewer" markdown="1">


=== "<span class='gui-fa' aria-hidden='true'>&#61587;</span>Load structure"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Import the structure file for this example.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-create.png?v=b4cb960a2713" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Load structure"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Load structure"><title>Load structure</title><defs><clipPath id="gui-clip-guide-structure-create-overview-structures-load-create-or-duplicate-0-structures-load"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-create.png?v=b4cb960a2713" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-create-overview-structures-load-create-or-duplicate-0-structures-load)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-create-overview-structures-load-create-or-duplicate-0-structures-load-1" data-gui-parts="[[784,260,334,39]]" d="M782.000 258.000 L1120.000 258.000 L1120.000 301.000 L782.000 301.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>

    </figure>

=== "<span class='gui-fa' aria-hidden='true'>&#61525;</span>Create structure"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Add a starting structure to edit.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-create.png?v=b4cb960a2713" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Create structure"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Create structure"><title>Create structure</title><defs><clipPath id="gui-clip-guide-structure-create-overview-structures-load-create-or-duplicate-0-structures-create"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-create.png?v=b4cb960a2713" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-create-overview-structures-load-create-or-duplicate-0-structures-create)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-create-overview-structures-load-create-or-duplicate-0-structures-create-1" data-gui-parts="[[1132,260,334,39]]" d="M1130.000 258.000 L1468.000 258.000 L1468.000 301.000 L1130.000 301.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>

    </figure>

=== "<span class='gui-fa' aria-hidden='true'>&#62029;</span>Duplicate structure"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Copy the selected structure.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-create.png?v=b4cb960a2713" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Duplicate structure"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Duplicate structure"><title>Duplicate structure</title><defs><clipPath id="gui-clip-guide-structure-create-overview-structures-load-create-or-duplicate-0-structures-duplicate"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-create.png?v=b4cb960a2713" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-create-overview-structures-load-create-or-duplicate-0-structures-duplicate)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-create-overview-structures-load-create-or-duplicate-0-structures-duplicate-1" data-gui-parts="[[784,313,334,39]]" d="M782.000 311.000 L1120.000 311.000 L1120.000 354.000 L782.000 354.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>

    </figure>

</div>
<!-- /gui-guide -->

## Space group and setting

The **Space group** group shows the crystal system and the selected space-group setting. The number, Hermann–Mauguin name and coordinate-system code describe that same setting and update together.

Choose the setting used by your structural model. Symmetry affects which cell values and atomic coordinates are independent, so a value controlled by symmetry should not be treated as a separately adjustable parameter.

<!-- gui-guide:space-group-and-setting -->
<div class="gui-viewer" markdown="1">


=== "Space-group number"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Select the symmetry of your model.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-symmetry.png?v=4e932163a976" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Space-group number"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Space-group number"><title>Space-group number</title><defs><clipPath id="gui-clip-guide-structure-symmetry-overview-structures-space-group-and-setting-0-spaceGroup-itNumber"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-symmetry.png?v=4e932163a976" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-symmetry-overview-structures-space-group-and-setting-0-spaceGroup-itNumber)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-symmetry-overview-structures-space-group-and-setting-0-spaceGroup-itNumber-1" data-gui-parts="[[955.375,210,167.875,56]]" d="M953.375 208.000 L1125.250 208.000 L1125.250 268.000 L953.375 268.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>

    </figure>

=== "Space-group symbol"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Check the Hermann-Mauguin symbol and setting.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-symmetry.png?v=4e932163a976" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Space-group symbol"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Space-group symbol"><title>Space-group symbol</title><defs><clipPath id="gui-clip-guide-structure-symmetry-overview-structures-space-group-and-setting-0-spaceGroup-nameHM"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-symmetry.png?v=4e932163a976" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-symmetry-overview-structures-space-group-and-setting-0-spaceGroup-nameHM)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-symmetry-overview-structures-space-group-and-setting-0-spaceGroup-nameHM-1" data-gui-parts="[[1126.75,210,167.875,56]]" d="M1124.750 208.000 L1296.625 208.000 L1296.625 268.000 L1124.750 268.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>

    </figure>

</div>
<!-- /gui-guide -->

## Unit cell

The **Cell** group contains cell lengths and angles. Enter values consistent with the selected symmetry and the physical units shown beside each field.

<!-- gui-guide:unit-cell -->
<div class="gui-viewer" markdown="1">


=== "Cell length a"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Inspect the cell length and its uncertainty.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-cell.png?v=b5a310dbfa7b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Cell length a"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Cell length a"><title>Cell length a</title><defs><clipPath id="gui-clip-guide-structure-cell-overview-structures-unit-cell-0-cell-length_a"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-cell.png?v=b5a310dbfa7b" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-cell-overview-structures-unit-cell-0-cell-length_a)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-cell-overview-structures-unit-cell-0-cell-length_a-1" data-gui-parts="[[784,252,110.75,56]]" d="M782.000 250.000 L896.750 250.000 L896.750 310.000 L782.000 310.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>

    </figure>

=== "Cell length b"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Values controlled by symmetry are linked.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-cell.png?v=b5a310dbfa7b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Cell length b"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Cell length b"><title>Cell length b</title><defs><clipPath id="gui-clip-guide-structure-cell-overview-structures-unit-cell-0-cell-length_b"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-cell.png?v=b5a310dbfa7b" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-cell-overview-structures-unit-cell-0-cell-length_b)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-cell-overview-structures-unit-cell-0-cell-length_b-1" data-gui-parts="[[898.25,252,110.75,56]]" d="M896.250 250.000 L1011.000 250.000 L1011.000 310.000 L896.250 310.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>

    </figure>

=== "Cell length c"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Use the cell convention of the selected space group.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-cell.png?v=b5a310dbfa7b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Cell length c"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Cell length c"><title>Cell length c</title><defs><clipPath id="gui-clip-guide-structure-cell-overview-structures-unit-cell-0-cell-length_c"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-cell.png?v=b5a310dbfa7b" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-cell-overview-structures-unit-cell-0-cell-length_c)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-cell-overview-structures-unit-cell-0-cell-length_c-1" data-gui-parts="[[1012.5,252,110.75,56]]" d="M1010.500 250.000 L1125.250 250.000 L1125.250 310.000 L1010.500 310.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>

    </figure>

</div>
<!-- /gui-guide -->

## Atom sites

The **Atom sites** table describes each site's label, element, fractional position, occupancy and displacement-parameter representation. It also identifies its Wyckoff position. The selected symmetry can fix a coordinate or relate it to another coordinate.

Use the atom-site controls to add or duplicate a site when building a model. Check the resulting occupancy and displacement parameters as well as the position.

<!-- gui-guide:atom-sites -->
<div class="gui-viewer" markdown="1">

<figure class="gui-figure" data-gui-figure>
<p class="gui-view-description">Inspect atom types, fractional coordinates and occupancies.</p>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-structure-atoms.png?v=76f5df31dd82" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Atom sites"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Atom sites"><title>Atom sites</title><defs><clipPath id="gui-clip-guide-structure-atoms-overview-structures-atom-sites-0-atomSites-list"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-structure-atoms.png?v=76f5df31dd82" width="1480" height="800" clip-path="url(#gui-clip-guide-structure-atoms-overview-structures-atom-sites-0-atomSites-list)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-structure-atoms-overview-structures-atom-sites-0-atomSites-list-1" data-gui-parts="[[784,294.00000000007884,682,156]]" d="M782.000 292.000 L1468.000 292.000 L1468.000 452.000 L782.000 452.000 Z" /><path data-gui-navigation data-gui-parts="[[655.203125,0,72.25,77]]" d="M653.203 -2.000 L729.453 -2.000 L729.453 79.000 L653.203 79.000 Z" /></svg></a>

</figure>

</div>
<!-- /gui-guide -->

## Link the structure to an experiment

A structure contributes to an experiment only when that experiment links to it. On **Experiment**, the **Linked structures** group shows the participating structures and their scales.

The link can be disabled while remaining in the project. A disabled link is kept when saving but contributes to neither calculation nor fitting. See [experiments](experiments.md).

<!-- gui-guide:link-the-structure-to-an-experiment -->
<div class="gui-viewer" markdown="1">

<figure class="gui-figure" data-gui-figure>
<p class="gui-view-description">Inspect phase links, scales and derived fractions.</p>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-links.png?v=01cd81e73ff0" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Linked structures"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Linked structures"><title>Linked structures</title><defs><clipPath id="gui-clip-guide-experiment-links-overview-structures-link-the-structure-to-an-experiment-0-linkedStructure-list"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-links.png?v=01cd81e73ff0" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-links-overview-structures-link-the-structure-to-an-experiment-0-linkedStructure-list)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-links-overview-structures-link-the-structure-to-an-experiment-0-linkedStructure-list-1" data-gui-parts="[[784,378,682,78]]" d="M782.000 376.000 L1468.000 376.000 L1468.000 458.000 L782.000 458.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>

</figure>

</div>
<!-- /gui-guide -->

## Refine selected values

Use the **Analysis** parameter table to choose which independent structural parameters vary. Begin with a model that describes the main pattern before freeing every available value.

<!-- gui-guide:refine-selected-values -->
<div class="gui-viewer" markdown="1">


=== "Main workspace"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Inspect the analysis view here. Its content changes with the active page and selection.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Main workspace"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Main workspace"><title>Main workspace</title><defs><clipPath id="gui-clip-13-analysis-basic-overview-structures-refine-selected-values-0-workflow-analysis-mainContent"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-overview-structures-refine-selected-values-0-workflow-analysis-mainContent)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-overview-structures-refine-selected-values-0-workflow-analysis-mainContent-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[812.359375,0,67.84375,77]]" d="M810.359 -2.000 L882.203 -2.000 L882.203 79.000 L810.359 79.000 Z" /></svg></a>

    </figure>

=== "Sidebar"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Sidebar"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Sidebar"><title>Sidebar</title><defs><clipPath id="gui-clip-13-analysis-basic-overview-structures-refine-selected-values-0-workflow-analysis-manualSidebar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-overview-structures-refine-selected-values-0-workflow-analysis-manualSidebar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-overview-structures-refine-selected-values-0-workflow-analysis-manualSidebar-1" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[812.359375,0,67.84375,77]]" d="M810.359 -2.000 L882.203 -2.000 L882.203 79.000 L810.359 79.000 Z" /></svg></a>

    </figure>

=== "Status bar"

    <figure class="gui-figure" data-gui-figure>
    <p class="gui-view-description">Read project counts, messages, calculation and fitting state here.</p>
    <a class="gui-image-link" href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Status bar"><svg class="gui-capture" data-gui-view="overview" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Status bar"><title>Status bar</title><defs><clipPath id="gui-clip-13-analysis-basic-overview-structures-refine-selected-values-0-statusBar"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/13-analysis-basic.png?v=c3a1fb56d69b" width="1480" height="800" clip-path="url(#gui-clip-13-analysis-basic-overview-structures-refine-selected-values-0-statusBar)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="13-analysis-basic-overview-structures-refine-selected-values-0-statusBar-1" data-gui-parts="[[0,758,1480,42]]" d="M-2.000 756.000 L1482.000 756.000 L1482.000 802.000 L-2.000 802.000 Z" /><path data-gui-navigation data-gui-parts="[[812.359375,0,67.84375,77]]" d="M810.359 -2.000 L882.203 -2.000 L882.203 79.000 L810.359 79.000 Z" /></svg></a>

    </figure>

</div>
<!-- /gui-guide -->

## Related Physics

[Unit cell and symmetry](../physics/crystallography.md#eq-cell-metric) · [Occupancy and scattering](../physics/diffraction.md#eq-nuclear-structure-factor) · [Atomic displacement](../physics/displacement.md#eq-anisotropic-adp).
