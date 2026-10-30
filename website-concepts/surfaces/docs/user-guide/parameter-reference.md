# Parameter names across interfaces

Choose the names you are working with. Each category and field links to its description and scientific meaning.

The **GUI** view shows control labels and the icon pattern used by Analysis parameters. The selected block, atom-site identifier and colours provide additional context in the app. **Edi** gives the keys shown in the Text tab and saved projects. **Python** gives access paths checked against the example projects; use `.value` or `.free` on a parameter. **CIF** gives the primary exchange name, including type-dependent forms.

A dash means no mapping was declared, or no direct Python field was found in the checked examples. It does not imply that an Edi key is an IUCr CIF item. A listed field is not necessarily applicable, editable or independently refinable in every model.

```python
parameter = project.structures[0].cell.length_a
print(parameter.value, parameter.free)
```

## Structure parameters

=== "GUI"

    **[<span class="ed-reference-icon" data-reference-category="space-group" aria-hidden="true">&#63423;</span> Space group](../physics/parameters.md#space-group)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [name](../physics/parameters.md#space-group-name-h-m) | name | — |
    | [code](../physics/parameters.md#space-group-coord-system-code) | code | — |
    | [number](../physics/parameters.md#space-group-it-number) | number | — |

    **[<span class="ed-reference-icon" data-reference-category="cell" aria-hidden="true">&#61874;</span> Cell](../physics/parameters.md#cell)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [a](../physics/parameters.md#cell-length-a) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61874;</span> <span class="ed-reference-icon" aria-hidden="true">&#62789;</span> a | Å |
    | [b](../physics/parameters.md#cell-length-b) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61874;</span> <span class="ed-reference-icon" aria-hidden="true">&#62789;</span> b | Å |
    | [c](../physics/parameters.md#cell-length-c) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61874;</span> <span class="ed-reference-icon" aria-hidden="true">&#62789;</span> c | Å |
    | [α](../physics/parameters.md#cell-angle-alpha) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61874;</span> <span class="ed-reference-icon" aria-hidden="true">&#62789;</span> α | deg |
    | [β](../physics/parameters.md#cell-angle-beta) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61874;</span> <span class="ed-reference-icon" aria-hidden="true">&#62789;</span> β | deg |
    | [γ](../physics/parameters.md#cell-angle-gamma) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61874;</span> <span class="ed-reference-icon" aria-hidden="true">&#62789;</span> γ | deg |

    **[<span class="ed-reference-icon" data-reference-category="atom-site" aria-hidden="true">&#62930;</span> Atom site](../physics/parameters.md#atom-site)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#atom-site-id) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> id | — |
    | [type](../physics/parameters.md#atom-site-type-symbol) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> type | — |
    | [WP](../physics/parameters.md#atom-site-wyckoff-letter) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> WP | — |
    | [ADP type](../physics/parameters.md#atom-site-adp-type) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> ADP type | — |
    | [x](../physics/parameters.md#atom-site-fract-x) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> <span class="ed-reference-icon" aria-hidden="true">&#62405;</span> x | — |
    | [y](../physics/parameters.md#atom-site-fract-y) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> <span class="ed-reference-icon" aria-hidden="true">&#62405;</span> y | — |
    | [z](../physics/parameters.md#atom-site-fract-z) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> <span class="ed-reference-icon" aria-hidden="true">&#62405;</span> z | — |
    | [occ](../physics/parameters.md#atom-site-occupancy) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> <span class="ed-reference-icon" aria-hidden="true">&#62837;</span> occ | — |
    | [iso/eq](../physics/parameters.md#atom-site-adp-iso) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> iso/eq | Å² |

    **[<span class="ed-reference-icon" data-reference-category="atom-site-aniso" aria-hidden="true">&#61618;</span> Atomic displacement](../physics/parameters.md#atom-site-aniso)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#atom-site-aniso-id) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> id | — |
    | [11](../physics/parameters.md#atom-site-aniso-adp-11) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> 11 | Å² |
    | [22](../physics/parameters.md#atom-site-aniso-adp-22) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> 22 | Å² |
    | [33](../physics/parameters.md#atom-site-aniso-adp-33) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> 33 | Å² |
    | [12](../physics/parameters.md#atom-site-aniso-adp-12) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> 12 | Å² |
    | [13](../physics/parameters.md#atom-site-aniso-adp-13) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> 13 | Å² |
    | [23](../physics/parameters.md#atom-site-aniso-adp-23) | <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> 23 | Å² |

    **[<span class="ed-reference-icon" data-reference-category="scattering-length" aria-hidden="true">&#62789;</span> Scattering length](../physics/parameters.md#scattering-length)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [type](../physics/parameters.md#scattering-length-type-symbol) | type | — |
    | [b](../physics/parameters.md#scattering-length-length-fm) | b | fm |

    **[<span class="ed-reference-icon" data-reference-category="geom" aria-hidden="true">&#62790;</span> Bond settings](../physics/parameters.md#geom)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [minimum distance](../physics/parameters.md#geom-min-bond-distance-cutoff) | minimum distance | Å |
    | [tolerance](../physics/parameters.md#geom-bond-distance-inc) | tolerance | Å |

    **[<span class="ed-reference-icon" data-reference-category="structure-view" aria-hidden="true">&#62783;</span> Appearance](../physics/parameters.md#structure-view)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [atoms as](../physics/parameters.md#structure-view-atom-view) | atoms as | — |
    | [colours](../physics/parameters.md#structure-view-colour-scheme) | colours | — |
    | [atom scale](../physics/parameters.md#structure-view-atom-scale) | atom scale | — |
    | [probability](../physics/parameters.md#structure-view-adp-probability) | probability | — |
    | [labels](../physics/parameters.md#structure-view-labels) | labels | — |
    | [atoms shown](../physics/parameters.md#structure-view-atoms) | atoms shown | — |
    | [bonds](../physics/parameters.md#structure-view-bonds) | bonds | — |
    | [cell](../physics/parameters.md#structure-view-cell) | cell | — |
    | [axes](../physics/parameters.md#structure-view-axes) | axes | — |

    **[<span class="ed-reference-icon" data-reference-category="space-group-symop" aria-hidden="true">&#62193;</span> Symmetry operator](../physics/parameters.md#space-group-symop)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [operation](../physics/parameters.md#space-group-symop-operation-xyz) | operation | — |

    **[<span class="ed-reference-icon" data-reference-category="expanded-atom-site" aria-hidden="true">&#62113;</span> Atom in the cell](../physics/parameters.md#expanded-atom-site)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [site](../physics/parameters.md#expanded-atom-site-atom-site-id) | site | — |
    | [symmetry](../physics/parameters.md#expanded-atom-site-site-symmetry) | symmetry | — |
    | [x](../physics/parameters.md#expanded-atom-site-fract-x) | x | — |
    | [y](../physics/parameters.md#expanded-atom-site-fract-y) | y | — |
    | [z](../physics/parameters.md#expanded-atom-site-fract-z) | z | — |
    | [X](../physics/parameters.md#expanded-atom-site-cartn-x) | X | Å |
    | [Y](../physics/parameters.md#expanded-atom-site-cartn-y) | Y | Å |
    | [Z](../physics/parameters.md#expanded-atom-site-cartn-z) | Z | Å |
    | [occ](../physics/parameters.md#expanded-atom-site-occupancy) | occ | — |
    | [U iso](../physics/parameters.md#expanded-atom-site-u-iso) | U iso | Å² |
    | [cluster](../physics/parameters.md#expanded-atom-site-cluster-id) | cluster | — |

    **[<span class="ed-reference-icon" data-reference-category="geom-bond" aria-hidden="true">&#63396;</span> Bond](../physics/parameters.md#geom-bond)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [atom 1](../physics/parameters.md#geom-bond-expanded-atom-site-id-1) | atom 1 | — |
    | [atom 2](../physics/parameters.md#geom-bond-expanded-atom-site-id-2) | atom 2 | — |
    | [site 1](../physics/parameters.md#geom-bond-atom-site-label-1) | site 1 | — |
    | [site 2](../physics/parameters.md#geom-bond-atom-site-label-2) | site 2 | — |
    | [symmetry 1](../physics/parameters.md#geom-bond-site-symmetry-1) | symmetry 1 | — |
    | [symmetry 2](../physics/parameters.md#geom-bond-site-symmetry-2) | symmetry 2 | — |
    | [distance](../physics/parameters.md#geom-bond-distance) | distance | Å |

    **[<span class="ed-reference-icon" data-reference-category="atom-sites-cartn-transform" aria-hidden="true">&#62923;</span> Cartesian frame](../physics/parameters.md#atom-sites-cartn-transform)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [M₁₁](../physics/parameters.md#atom-sites-cartn-transform-mat-11) | M₁₁ | Å |
    | [M₁₂](../physics/parameters.md#atom-sites-cartn-transform-mat-12) | M₁₂ | Å |
    | [M₁₃](../physics/parameters.md#atom-sites-cartn-transform-mat-13) | M₁₃ | Å |
    | [M₂₁](../physics/parameters.md#atom-sites-cartn-transform-mat-21) | M₂₁ | Å |
    | [M₂₂](../physics/parameters.md#atom-sites-cartn-transform-mat-22) | M₂₂ | Å |
    | [M₂₃](../physics/parameters.md#atom-sites-cartn-transform-mat-23) | M₂₃ | Å |
    | [M₃₁](../physics/parameters.md#atom-sites-cartn-transform-mat-31) | M₃₁ | Å |
    | [M₃₂](../physics/parameters.md#atom-sites-cartn-transform-mat-32) | M₃₂ | Å |
    | [M₃₃](../physics/parameters.md#atom-sites-cartn-transform-mat-33) | M₃₃ | Å |
    | [axes](../physics/parameters.md#atom-sites-cartn-transform-axes) | axes | — |

=== "Edi"

    **[<span class="ed-reference-icon" data-reference-category="space-group" aria-hidden="true">&#63423;</span> Space group](../physics/parameters.md#space-group)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [name](../physics/parameters.md#space-group-name-h-m) | <code>_space_group.name_h_m</code> | — |
    | [code](../physics/parameters.md#space-group-coord-system-code) | <code>_space_group.coord_system_code</code> | — |
    | [number](../physics/parameters.md#space-group-it-number) | <code>_space_group.it_number</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="cell" aria-hidden="true">&#61874;</span> Cell](../physics/parameters.md#cell)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [a](../physics/parameters.md#cell-length-a) | <code>_cell.length_a</code> | Å |
    | [b](../physics/parameters.md#cell-length-b) | <code>_cell.length_b</code> | Å |
    | [c](../physics/parameters.md#cell-length-c) | <code>_cell.length_c</code> | Å |
    | [α](../physics/parameters.md#cell-angle-alpha) | <code>_cell.angle_alpha</code> | deg |
    | [β](../physics/parameters.md#cell-angle-beta) | <code>_cell.angle_beta</code> | deg |
    | [γ](../physics/parameters.md#cell-angle-gamma) | <code>_cell.angle_gamma</code> | deg |

    **[<span class="ed-reference-icon" data-reference-category="atom-site" aria-hidden="true">&#62930;</span> Atom site](../physics/parameters.md#atom-site)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#atom-site-id) | <code>_atom_site.id</code> | — |
    | [type](../physics/parameters.md#atom-site-type-symbol) | <code>_atom_site.type_symbol</code> | — |
    | [WP](../physics/parameters.md#atom-site-wyckoff-letter) | <code>_atom_site.wyckoff_letter</code> | — |
    | [ADP type](../physics/parameters.md#atom-site-adp-type) | <code>_atom_site.adp_type</code> | — |
    | [x](../physics/parameters.md#atom-site-fract-x) | <code>_atom_site.fract_x</code> | — |
    | [y](../physics/parameters.md#atom-site-fract-y) | <code>_atom_site.fract_y</code> | — |
    | [z](../physics/parameters.md#atom-site-fract-z) | <code>_atom_site.fract_z</code> | — |
    | [occ](../physics/parameters.md#atom-site-occupancy) | <code>_atom_site.occupancy</code> | — |
    | [iso/eq](../physics/parameters.md#atom-site-adp-iso) | <code>_atom_site.adp_iso</code> | Å² |

    **[<span class="ed-reference-icon" data-reference-category="atom-site-aniso" aria-hidden="true">&#61618;</span> Atomic displacement](../physics/parameters.md#atom-site-aniso)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#atom-site-aniso-id) | <code>_atom_site_aniso.id</code> | — |
    | [11](../physics/parameters.md#atom-site-aniso-adp-11) | <code>_atom_site_aniso.adp_11</code> | Å² |
    | [22](../physics/parameters.md#atom-site-aniso-adp-22) | <code>_atom_site_aniso.adp_22</code> | Å² |
    | [33](../physics/parameters.md#atom-site-aniso-adp-33) | <code>_atom_site_aniso.adp_33</code> | Å² |
    | [12](../physics/parameters.md#atom-site-aniso-adp-12) | <code>_atom_site_aniso.adp_12</code> | Å² |
    | [13](../physics/parameters.md#atom-site-aniso-adp-13) | <code>_atom_site_aniso.adp_13</code> | Å² |
    | [23](../physics/parameters.md#atom-site-aniso-adp-23) | <code>_atom_site_aniso.adp_23</code> | Å² |

    **[<span class="ed-reference-icon" data-reference-category="scattering-length" aria-hidden="true">&#62789;</span> Scattering length](../physics/parameters.md#scattering-length)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [type](../physics/parameters.md#scattering-length-type-symbol) | <code>_scattering_length.type_symbol</code> | — |
    | [b](../physics/parameters.md#scattering-length-length-fm) | <code>_scattering_length.length_fm</code> | fm |

    **[<span class="ed-reference-icon" data-reference-category="geom" aria-hidden="true">&#62790;</span> Bond settings](../physics/parameters.md#geom)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [minimum distance](../physics/parameters.md#geom-min-bond-distance-cutoff) | <code>_geom.min_bond_distance_cutoff</code> | Å |
    | [tolerance](../physics/parameters.md#geom-bond-distance-inc) | <code>_geom.bond_distance_inc</code> | Å |

    **[<span class="ed-reference-icon" data-reference-category="structure-view" aria-hidden="true">&#62783;</span> Appearance](../physics/parameters.md#structure-view)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [atoms as](../physics/parameters.md#structure-view-atom-view) | <code>_structure_view.atom_view</code> | — |
    | [colours](../physics/parameters.md#structure-view-colour-scheme) | <code>_structure_view.colour_scheme</code> | — |
    | [atom scale](../physics/parameters.md#structure-view-atom-scale) | <code>_structure_view.atom_scale</code> | — |
    | [probability](../physics/parameters.md#structure-view-adp-probability) | <code>_structure_view.adp_probability</code> | — |
    | [labels](../physics/parameters.md#structure-view-labels) | <code>_structure_view.labels</code> | — |
    | [atoms shown](../physics/parameters.md#structure-view-atoms) | <code>_structure_view.atoms</code> | — |
    | [bonds](../physics/parameters.md#structure-view-bonds) | <code>_structure_view.bonds</code> | — |
    | [cell](../physics/parameters.md#structure-view-cell) | <code>_structure_view.cell</code> | — |
    | [axes](../physics/parameters.md#structure-view-axes) | <code>_structure_view.axes</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="space-group-symop" aria-hidden="true">&#62193;</span> Symmetry operator](../physics/parameters.md#space-group-symop)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [operation](../physics/parameters.md#space-group-symop-operation-xyz) | <code>_space_group_symop.operation_xyz</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="expanded-atom-site" aria-hidden="true">&#62113;</span> Atom in the cell](../physics/parameters.md#expanded-atom-site)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [site](../physics/parameters.md#expanded-atom-site-atom-site-id) | <code>_expanded_atom_site.atom_site_id</code> | — |
    | [symmetry](../physics/parameters.md#expanded-atom-site-site-symmetry) | <code>_expanded_atom_site.site_symmetry</code> | — |
    | [x](../physics/parameters.md#expanded-atom-site-fract-x) | <code>_expanded_atom_site.fract_x</code> | — |
    | [y](../physics/parameters.md#expanded-atom-site-fract-y) | <code>_expanded_atom_site.fract_y</code> | — |
    | [z](../physics/parameters.md#expanded-atom-site-fract-z) | <code>_expanded_atom_site.fract_z</code> | — |
    | [X](../physics/parameters.md#expanded-atom-site-cartn-x) | <code>_expanded_atom_site.cartn_x</code> | Å |
    | [Y](../physics/parameters.md#expanded-atom-site-cartn-y) | <code>_expanded_atom_site.cartn_y</code> | Å |
    | [Z](../physics/parameters.md#expanded-atom-site-cartn-z) | <code>_expanded_atom_site.cartn_z</code> | Å |
    | [occ](../physics/parameters.md#expanded-atom-site-occupancy) | <code>_expanded_atom_site.occupancy</code> | — |
    | [U iso](../physics/parameters.md#expanded-atom-site-u-iso) | <code>_expanded_atom_site.u_iso</code> | Å² |
    | [cluster](../physics/parameters.md#expanded-atom-site-cluster-id) | <code>_expanded_atom_site.cluster_id</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="geom-bond" aria-hidden="true">&#63396;</span> Bond](../physics/parameters.md#geom-bond)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [atom 1](../physics/parameters.md#geom-bond-expanded-atom-site-id-1) | <code>_geom_bond.expanded_atom_site_id_1</code> | — |
    | [atom 2](../physics/parameters.md#geom-bond-expanded-atom-site-id-2) | <code>_geom_bond.expanded_atom_site_id_2</code> | — |
    | [site 1](../physics/parameters.md#geom-bond-atom-site-label-1) | <code>_geom_bond.atom_site_label_1</code> | — |
    | [site 2](../physics/parameters.md#geom-bond-atom-site-label-2) | <code>_geom_bond.atom_site_label_2</code> | — |
    | [symmetry 1](../physics/parameters.md#geom-bond-site-symmetry-1) | <code>_geom_bond.site_symmetry_1</code> | — |
    | [symmetry 2](../physics/parameters.md#geom-bond-site-symmetry-2) | <code>_geom_bond.site_symmetry_2</code> | — |
    | [distance](../physics/parameters.md#geom-bond-distance) | <code>_geom_bond.distance</code> | Å |

    **[<span class="ed-reference-icon" data-reference-category="atom-sites-cartn-transform" aria-hidden="true">&#62923;</span> Cartesian frame](../physics/parameters.md#atom-sites-cartn-transform)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [M₁₁](../physics/parameters.md#atom-sites-cartn-transform-mat-11) | <code>_atom_sites_cartn_transform.mat_11</code> | Å |
    | [M₁₂](../physics/parameters.md#atom-sites-cartn-transform-mat-12) | <code>_atom_sites_cartn_transform.mat_12</code> | Å |
    | [M₁₃](../physics/parameters.md#atom-sites-cartn-transform-mat-13) | <code>_atom_sites_cartn_transform.mat_13</code> | Å |
    | [M₂₁](../physics/parameters.md#atom-sites-cartn-transform-mat-21) | <code>_atom_sites_cartn_transform.mat_21</code> | Å |
    | [M₂₂](../physics/parameters.md#atom-sites-cartn-transform-mat-22) | <code>_atom_sites_cartn_transform.mat_22</code> | Å |
    | [M₂₃](../physics/parameters.md#atom-sites-cartn-transform-mat-23) | <code>_atom_sites_cartn_transform.mat_23</code> | Å |
    | [M₃₁](../physics/parameters.md#atom-sites-cartn-transform-mat-31) | <code>_atom_sites_cartn_transform.mat_31</code> | Å |
    | [M₃₂](../physics/parameters.md#atom-sites-cartn-transform-mat-32) | <code>_atom_sites_cartn_transform.mat_32</code> | Å |
    | [M₃₃](../physics/parameters.md#atom-sites-cartn-transform-mat-33) | <code>_atom_sites_cartn_transform.mat_33</code> | Å |
    | [axes](../physics/parameters.md#atom-sites-cartn-transform-axes) | <code>_atom_sites_cartn_transform.axes</code> | — |

=== "Python"

    **[<span class="ed-reference-icon" data-reference-category="space-group" aria-hidden="true">&#63423;</span> Space group](../physics/parameters.md#space-group)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [name](../physics/parameters.md#space-group-name-h-m) | <code>project.structures[0].space_group.name_h_m</code> | — |
    | [code](../physics/parameters.md#space-group-coord-system-code) | <code>project.structures[0].space_group.coord_system_code</code> | — |
    | [number](../physics/parameters.md#space-group-it-number) | <code>project.structures[0].space_group.it_number</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="cell" aria-hidden="true">&#61874;</span> Cell](../physics/parameters.md#cell)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [a](../physics/parameters.md#cell-length-a) | <code>project.structures[0].cell.length_a</code> | Å |
    | [b](../physics/parameters.md#cell-length-b) | <code>project.structures[0].cell.length_b</code> | Å |
    | [c](../physics/parameters.md#cell-length-c) | <code>project.structures[0].cell.length_c</code> | Å |
    | [α](../physics/parameters.md#cell-angle-alpha) | <code>project.structures[0].cell.angle_alpha</code> | deg |
    | [β](../physics/parameters.md#cell-angle-beta) | <code>project.structures[0].cell.angle_beta</code> | deg |
    | [γ](../physics/parameters.md#cell-angle-gamma) | <code>project.structures[0].cell.angle_gamma</code> | deg |

    **[<span class="ed-reference-icon" data-reference-category="atom-site" aria-hidden="true">&#62930;</span> Atom site](../physics/parameters.md#atom-site)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#atom-site-id) | <code>project.structures[0].atom_sites[0].id</code> | — |
    | [type](../physics/parameters.md#atom-site-type-symbol) | <code>project.structures[0].atom_sites[0].type_symbol</code> | — |
    | [WP](../physics/parameters.md#atom-site-wyckoff-letter) | <code>project.structures[0].atom_sites[0].wyckoff_letter</code> | — |
    | [ADP type](../physics/parameters.md#atom-site-adp-type) | <code>project.structures[0].atom_sites[0].adp_type</code> | — |
    | [x](../physics/parameters.md#atom-site-fract-x) | <code>project.structures[0].atom_sites[0].fract_x</code> | — |
    | [y](../physics/parameters.md#atom-site-fract-y) | <code>project.structures[0].atom_sites[0].fract_y</code> | — |
    | [z](../physics/parameters.md#atom-site-fract-z) | <code>project.structures[0].atom_sites[0].fract_z</code> | — |
    | [occ](../physics/parameters.md#atom-site-occupancy) | <code>project.structures[0].atom_sites[0].occupancy</code> | — |
    | [iso/eq](../physics/parameters.md#atom-site-adp-iso) | <code>project.structures[0].atom_sites[0].adp_iso</code> | Å² |

    **[<span class="ed-reference-icon" data-reference-category="atom-site-aniso" aria-hidden="true">&#61618;</span> Atomic displacement](../physics/parameters.md#atom-site-aniso)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#atom-site-aniso-id) | <code>project.structures[0].atom_site_aniso[0].id</code> | — |
    | [11](../physics/parameters.md#atom-site-aniso-adp-11) | <code>project.structures[0].atom_site_aniso[0].adp_11</code> | Å² |
    | [22](../physics/parameters.md#atom-site-aniso-adp-22) | <code>project.structures[0].atom_site_aniso[0].adp_22</code> | Å² |
    | [33](../physics/parameters.md#atom-site-aniso-adp-33) | <code>project.structures[0].atom_site_aniso[0].adp_33</code> | Å² |
    | [12](../physics/parameters.md#atom-site-aniso-adp-12) | <code>project.structures[0].atom_site_aniso[0].adp_12</code> | Å² |
    | [13](../physics/parameters.md#atom-site-aniso-adp-13) | <code>project.structures[0].atom_site_aniso[0].adp_13</code> | Å² |
    | [23](../physics/parameters.md#atom-site-aniso-adp-23) | <code>project.structures[0].atom_site_aniso[0].adp_23</code> | Å² |

    **[<span class="ed-reference-icon" data-reference-category="scattering-length" aria-hidden="true">&#62789;</span> Scattering length](../physics/parameters.md#scattering-length)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [type](../physics/parameters.md#scattering-length-type-symbol) | — | — |
    | [b](../physics/parameters.md#scattering-length-length-fm) | — | fm |

    **[<span class="ed-reference-icon" data-reference-category="geom" aria-hidden="true">&#62790;</span> Bond settings](../physics/parameters.md#geom)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [minimum distance](../physics/parameters.md#geom-min-bond-distance-cutoff) | <code>project.structures[0].geom.min_bond_distance_cutoff</code> | Å |
    | [tolerance](../physics/parameters.md#geom-bond-distance-inc) | <code>project.structures[0].geom.bond_distance_inc</code> | Å |

    **[<span class="ed-reference-icon" data-reference-category="structure-view" aria-hidden="true">&#62783;</span> Appearance](../physics/parameters.md#structure-view)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [atoms as](../physics/parameters.md#structure-view-atom-view) | — | — |
    | [colours](../physics/parameters.md#structure-view-colour-scheme) | — | — |
    | [atom scale](../physics/parameters.md#structure-view-atom-scale) | — | — |
    | [probability](../physics/parameters.md#structure-view-adp-probability) | — | — |
    | [labels](../physics/parameters.md#structure-view-labels) | — | — |
    | [atoms shown](../physics/parameters.md#structure-view-atoms) | — | — |
    | [bonds](../physics/parameters.md#structure-view-bonds) | — | — |
    | [cell](../physics/parameters.md#structure-view-cell) | — | — |
    | [axes](../physics/parameters.md#structure-view-axes) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="space-group-symop" aria-hidden="true">&#62193;</span> Symmetry operator](../physics/parameters.md#space-group-symop)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [operation](../physics/parameters.md#space-group-symop-operation-xyz) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="expanded-atom-site" aria-hidden="true">&#62113;</span> Atom in the cell](../physics/parameters.md#expanded-atom-site)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [site](../physics/parameters.md#expanded-atom-site-atom-site-id) | — | — |
    | [symmetry](../physics/parameters.md#expanded-atom-site-site-symmetry) | — | — |
    | [x](../physics/parameters.md#expanded-atom-site-fract-x) | — | — |
    | [y](../physics/parameters.md#expanded-atom-site-fract-y) | — | — |
    | [z](../physics/parameters.md#expanded-atom-site-fract-z) | — | — |
    | [X](../physics/parameters.md#expanded-atom-site-cartn-x) | — | Å |
    | [Y](../physics/parameters.md#expanded-atom-site-cartn-y) | — | Å |
    | [Z](../physics/parameters.md#expanded-atom-site-cartn-z) | — | Å |
    | [occ](../physics/parameters.md#expanded-atom-site-occupancy) | — | — |
    | [U iso](../physics/parameters.md#expanded-atom-site-u-iso) | — | Å² |
    | [cluster](../physics/parameters.md#expanded-atom-site-cluster-id) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="geom-bond" aria-hidden="true">&#63396;</span> Bond](../physics/parameters.md#geom-bond)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [atom 1](../physics/parameters.md#geom-bond-expanded-atom-site-id-1) | — | — |
    | [atom 2](../physics/parameters.md#geom-bond-expanded-atom-site-id-2) | — | — |
    | [site 1](../physics/parameters.md#geom-bond-atom-site-label-1) | — | — |
    | [site 2](../physics/parameters.md#geom-bond-atom-site-label-2) | — | — |
    | [symmetry 1](../physics/parameters.md#geom-bond-site-symmetry-1) | — | — |
    | [symmetry 2](../physics/parameters.md#geom-bond-site-symmetry-2) | — | — |
    | [distance](../physics/parameters.md#geom-bond-distance) | — | Å |

    **[<span class="ed-reference-icon" data-reference-category="atom-sites-cartn-transform" aria-hidden="true">&#62923;</span> Cartesian frame](../physics/parameters.md#atom-sites-cartn-transform)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [M₁₁](../physics/parameters.md#atom-sites-cartn-transform-mat-11) | — | Å |
    | [M₁₂](../physics/parameters.md#atom-sites-cartn-transform-mat-12) | — | Å |
    | [M₁₃](../physics/parameters.md#atom-sites-cartn-transform-mat-13) | — | Å |
    | [M₂₁](../physics/parameters.md#atom-sites-cartn-transform-mat-21) | — | Å |
    | [M₂₂](../physics/parameters.md#atom-sites-cartn-transform-mat-22) | — | Å |
    | [M₂₃](../physics/parameters.md#atom-sites-cartn-transform-mat-23) | — | Å |
    | [M₃₁](../physics/parameters.md#atom-sites-cartn-transform-mat-31) | — | Å |
    | [M₃₂](../physics/parameters.md#atom-sites-cartn-transform-mat-32) | — | Å |
    | [M₃₃](../physics/parameters.md#atom-sites-cartn-transform-mat-33) | — | Å |
    | [axes](../physics/parameters.md#atom-sites-cartn-transform-axes) | — | — |

=== "CIF"

    **[<span class="ed-reference-icon" data-reference-category="space-group" aria-hidden="true">&#63423;</span> Space group](../physics/parameters.md#space-group)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [name](../physics/parameters.md#space-group-name-h-m) | <code>_space_group.name_H-M_alt</code> | — |
    | [code](../physics/parameters.md#space-group-coord-system-code) | <code>_space_group.IT_coordinate_system_code</code> | — |
    | [number](../physics/parameters.md#space-group-it-number) | <code>_space_group.IT_number</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="cell" aria-hidden="true">&#61874;</span> Cell](../physics/parameters.md#cell)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [a](../physics/parameters.md#cell-length-a) | <code>_cell.length_a</code> | Å |
    | [b](../physics/parameters.md#cell-length-b) | <code>_cell.length_b</code> | Å |
    | [c](../physics/parameters.md#cell-length-c) | <code>_cell.length_c</code> | Å |
    | [α](../physics/parameters.md#cell-angle-alpha) | <code>_cell.angle_alpha</code> | deg |
    | [β](../physics/parameters.md#cell-angle-beta) | <code>_cell.angle_beta</code> | deg |
    | [γ](../physics/parameters.md#cell-angle-gamma) | <code>_cell.angle_gamma</code> | deg |

    **[<span class="ed-reference-icon" data-reference-category="atom-site" aria-hidden="true">&#62930;</span> Atom site](../physics/parameters.md#atom-site)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#atom-site-id) | <code>_atom_site.label</code> | — |
    | [type](../physics/parameters.md#atom-site-type-symbol) | <code>_atom_site.type_symbol</code> | — |
    | [WP](../physics/parameters.md#atom-site-wyckoff-letter) | <code>_atom_site.Wyckoff_symbol</code> | — |
    | [ADP type](../physics/parameters.md#atom-site-adp-type) | <code>_atom_site.ADP_type</code> | — |
    | [x](../physics/parameters.md#atom-site-fract-x) | <code>_atom_site.fract_x</code> | — |
    | [y](../physics/parameters.md#atom-site-fract-y) | <code>_atom_site.fract_y</code> | — |
    | [z](../physics/parameters.md#atom-site-fract-z) | <code>_atom_site.fract_z</code> | — |
    | [occ](../physics/parameters.md#atom-site-occupancy) | <code>_atom_site.occupancy</code> | — |
    | [iso/eq](../physics/parameters.md#atom-site-adp-iso) | <code>Biso</code>: <code>_atom_site.B_iso_or_equiv</code><br><code>Uiso</code>: <code>_atom_site.U_iso_or_equiv</code><br><code>Bani</code>: <code>_atom_site.B_iso_or_equiv</code><br><code>Uani</code>: <code>_atom_site.U_iso_or_equiv</code><br><code>beta</code>: <code>_atom_site.B_iso_or_equiv</code> | Å² |

    **[<span class="ed-reference-icon" data-reference-category="atom-site-aniso" aria-hidden="true">&#61618;</span> Atomic displacement](../physics/parameters.md#atom-site-aniso)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#atom-site-aniso-id) | <code>_atom_site_aniso.label</code> | — |
    | [11](../physics/parameters.md#atom-site-aniso-adp-11) | <code>Uani</code>: <code>_atom_site_aniso.U_11</code><br><code>Bani</code>: <code>_atom_site_aniso.B_11</code><br><code>beta</code>: <code>_atom_site_aniso.beta_11</code> | Å² |
    | [22](../physics/parameters.md#atom-site-aniso-adp-22) | <code>Uani</code>: <code>_atom_site_aniso.U_22</code><br><code>Bani</code>: <code>_atom_site_aniso.B_22</code><br><code>beta</code>: <code>_atom_site_aniso.beta_22</code> | Å² |
    | [33](../physics/parameters.md#atom-site-aniso-adp-33) | <code>Uani</code>: <code>_atom_site_aniso.U_33</code><br><code>Bani</code>: <code>_atom_site_aniso.B_33</code><br><code>beta</code>: <code>_atom_site_aniso.beta_33</code> | Å² |
    | [12](../physics/parameters.md#atom-site-aniso-adp-12) | <code>Uani</code>: <code>_atom_site_aniso.U_12</code><br><code>Bani</code>: <code>_atom_site_aniso.B_12</code><br><code>beta</code>: <code>_atom_site_aniso.beta_12</code> | Å² |
    | [13](../physics/parameters.md#atom-site-aniso-adp-13) | <code>Uani</code>: <code>_atom_site_aniso.U_13</code><br><code>Bani</code>: <code>_atom_site_aniso.B_13</code><br><code>beta</code>: <code>_atom_site_aniso.beta_13</code> | Å² |
    | [23](../physics/parameters.md#atom-site-aniso-adp-23) | <code>Uani</code>: <code>_atom_site_aniso.U_23</code><br><code>Bani</code>: <code>_atom_site_aniso.B_23</code><br><code>beta</code>: <code>_atom_site_aniso.beta_23</code> | Å² |

    **[<span class="ed-reference-icon" data-reference-category="scattering-length" aria-hidden="true">&#62789;</span> Scattering length](../physics/parameters.md#scattering-length)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [type](../physics/parameters.md#scattering-length-type-symbol) | <code>_edi_scattering_length.type_symbol</code> | — |
    | [b](../physics/parameters.md#scattering-length-length-fm) | <code>_edi_scattering_length.length_fm</code> | fm |

    **[<span class="ed-reference-icon" data-reference-category="geom" aria-hidden="true">&#62790;</span> Bond settings](../physics/parameters.md#geom)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [minimum distance](../physics/parameters.md#geom-min-bond-distance-cutoff) | <code>_geom.min_bond_distance_cutoff</code> | Å |
    | [tolerance](../physics/parameters.md#geom-bond-distance-inc) | <code>_geom.bond_distance_incr</code> | Å |

    **[<span class="ed-reference-icon" data-reference-category="structure-view" aria-hidden="true">&#62783;</span> Appearance](../physics/parameters.md#structure-view)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [atoms as](../physics/parameters.md#structure-view-atom-view) | <code>_edi_structure_view.atom_view</code> | — |
    | [colours](../physics/parameters.md#structure-view-colour-scheme) | <code>_edi_structure_view.colour_scheme</code> | — |
    | [atom scale](../physics/parameters.md#structure-view-atom-scale) | <code>_edi_structure_view.atom_scale</code> | — |
    | [probability](../physics/parameters.md#structure-view-adp-probability) | <code>_edi_structure_view.adp_probability</code> | — |
    | [labels](../physics/parameters.md#structure-view-labels) | <code>_edi_structure_view.labels</code> | — |
    | [atoms shown](../physics/parameters.md#structure-view-atoms) | <code>_edi_structure_view.atoms</code> | — |
    | [bonds](../physics/parameters.md#structure-view-bonds) | <code>_edi_structure_view.bonds</code> | — |
    | [cell](../physics/parameters.md#structure-view-cell) | <code>_edi_structure_view.cell</code> | — |
    | [axes](../physics/parameters.md#structure-view-axes) | <code>_edi_structure_view.axes</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="space-group-symop" aria-hidden="true">&#62193;</span> Symmetry operator](../physics/parameters.md#space-group-symop)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [operation](../physics/parameters.md#space-group-symop-operation-xyz) | <code>_space_group_symop.operation_xyz</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="expanded-atom-site" aria-hidden="true">&#62113;</span> Atom in the cell](../physics/parameters.md#expanded-atom-site)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [site](../physics/parameters.md#expanded-atom-site-atom-site-id) | <code>_edi_expanded_atom_site.atom_site_id</code> | — |
    | [symmetry](../physics/parameters.md#expanded-atom-site-site-symmetry) | <code>_edi_expanded_atom_site.site_symmetry</code> | — |
    | [x](../physics/parameters.md#expanded-atom-site-fract-x) | <code>_edi_expanded_atom_site.fract_x</code> | — |
    | [y](../physics/parameters.md#expanded-atom-site-fract-y) | <code>_edi_expanded_atom_site.fract_y</code> | — |
    | [z](../physics/parameters.md#expanded-atom-site-fract-z) | <code>_edi_expanded_atom_site.fract_z</code> | — |
    | [X](../physics/parameters.md#expanded-atom-site-cartn-x) | <code>_edi_expanded_atom_site.cartn_x</code> | Å |
    | [Y](../physics/parameters.md#expanded-atom-site-cartn-y) | <code>_edi_expanded_atom_site.cartn_y</code> | Å |
    | [Z](../physics/parameters.md#expanded-atom-site-cartn-z) | <code>_edi_expanded_atom_site.cartn_z</code> | Å |
    | [occ](../physics/parameters.md#expanded-atom-site-occupancy) | <code>_edi_expanded_atom_site.occupancy</code> | — |
    | [U iso](../physics/parameters.md#expanded-atom-site-u-iso) | <code>_edi_expanded_atom_site.u_iso</code> | Å² |
    | [cluster](../physics/parameters.md#expanded-atom-site-cluster-id) | <code>_edi_expanded_atom_site.cluster_id</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="geom-bond" aria-hidden="true">&#63396;</span> Bond](../physics/parameters.md#geom-bond)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [atom 1](../physics/parameters.md#geom-bond-expanded-atom-site-id-1) | <code>_edi_geom_bond.expanded_atom_site_id_1</code> | — |
    | [atom 2](../physics/parameters.md#geom-bond-expanded-atom-site-id-2) | <code>_edi_geom_bond.expanded_atom_site_id_2</code> | — |
    | [site 1](../physics/parameters.md#geom-bond-atom-site-label-1) | <code>_geom_bond.atom_site_label_1</code> | — |
    | [site 2](../physics/parameters.md#geom-bond-atom-site-label-2) | <code>_geom_bond.atom_site_label_2</code> | — |
    | [symmetry 1](../physics/parameters.md#geom-bond-site-symmetry-1) | <code>_geom_bond.site_symmetry_1</code> | — |
    | [symmetry 2](../physics/parameters.md#geom-bond-site-symmetry-2) | <code>_geom_bond.site_symmetry_2</code> | — |
    | [distance](../physics/parameters.md#geom-bond-distance) | <code>_geom_bond.distance</code> | Å |

    **[<span class="ed-reference-icon" data-reference-category="atom-sites-cartn-transform" aria-hidden="true">&#62923;</span> Cartesian frame](../physics/parameters.md#atom-sites-cartn-transform)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [M₁₁](../physics/parameters.md#atom-sites-cartn-transform-mat-11) | <code>_atom_sites_Cartn_transform.mat_11</code> | Å |
    | [M₁₂](../physics/parameters.md#atom-sites-cartn-transform-mat-12) | <code>_atom_sites_Cartn_transform.mat_12</code> | Å |
    | [M₁₃](../physics/parameters.md#atom-sites-cartn-transform-mat-13) | <code>_atom_sites_Cartn_transform.mat_13</code> | Å |
    | [M₂₁](../physics/parameters.md#atom-sites-cartn-transform-mat-21) | <code>_atom_sites_Cartn_transform.mat_21</code> | Å |
    | [M₂₂](../physics/parameters.md#atom-sites-cartn-transform-mat-22) | <code>_atom_sites_Cartn_transform.mat_22</code> | Å |
    | [M₂₃](../physics/parameters.md#atom-sites-cartn-transform-mat-23) | <code>_atom_sites_Cartn_transform.mat_23</code> | Å |
    | [M₃₁](../physics/parameters.md#atom-sites-cartn-transform-mat-31) | <code>_atom_sites_Cartn_transform.mat_31</code> | Å |
    | [M₃₂](../physics/parameters.md#atom-sites-cartn-transform-mat-32) | <code>_atom_sites_Cartn_transform.mat_32</code> | Å |
    | [M₃₃](../physics/parameters.md#atom-sites-cartn-transform-mat-33) | <code>_atom_sites_Cartn_transform.mat_33</code> | Å |
    | [axes](../physics/parameters.md#atom-sites-cartn-transform-axes) | <code>_atom_sites_Cartn_transform.axes</code> | — |

## Experiment parameters

=== "GUI"

    **[<span class="ed-reference-icon" data-reference-category="experiment-type" aria-hidden="true">&#63417;</span> Experiment type](../physics/parameters.md#experiment-type)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [beam mode](../physics/parameters.md#experiment-type-beam-mode) | beam mode | — |
    | [sample form](../physics/parameters.md#experiment-type-sample-form) | sample form | — |
    | [probe](../physics/parameters.md#experiment-type-radiation-probe) | probe | — |
    | [scattering type](../physics/parameters.md#experiment-type-scattering-type) | scattering type | — |
    | [dimensionality](../physics/parameters.md#experiment-type-dimensionality) | dimensionality | — |
    | [polarisation](../physics/parameters.md#experiment-type-polarisation) | polarisation | — |

    **[<span class="ed-reference-icon" data-reference-category="data-range" aria-hidden="true">&#62263;</span> Calculation range](../physics/parameters.md#data-range)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [min](../physics/parameters.md#data-range-two-theta-min) | min | deg |
    | [max](../physics/parameters.md#data-range-two-theta-max) | max | deg |
    | [step](../physics/parameters.md#data-range-two-theta-step) | step | deg |
    | [2θ](../physics/parameters.md#data-range-two-theta) | 2θ | deg |
    | [min](../physics/parameters.md#data-range-time-of-flight-min) | min | µs |
    | [max](../physics/parameters.md#data-range-time-of-flight-max) | max | µs |
    | [step](../physics/parameters.md#data-range-time-of-flight-step) | step | µs |
    | [TOF](../physics/parameters.md#data-range-time-of-flight) | TOF | µs |

    **[<span class="ed-reference-icon" data-reference-category="background" aria-hidden="true">&#63550;</span> Background](../physics/parameters.md#background)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [intensity](../physics/parameters.md#background-intensity) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> <span class="ed-reference-icon" aria-hidden="true">&#63228;</span> intensity | — |
    | [position](../physics/parameters.md#background-position) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> position | µs |
    | [coefficient](../physics/parameters.md#background-coef) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> coefficient | — |
    | [order](../physics/parameters.md#background-order) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> order | — |
    | [origin](../physics/parameters.md#background-origin) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> origin | — |
    | [x min](../physics/parameters.md#background-x-min) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> x min | — |
    | [x max](../physics/parameters.md#background-x-max) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> x max | — |
    | [type](../physics/parameters.md#background-type) | type | — |
    | [id](../physics/parameters.md#background-id) | id | — |

    **[<span class="ed-reference-icon" data-reference-category="background-estimate" aria-hidden="true">&#61648;</span> Background estimation](../physics/parameters.md#background-estimate)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [estimation mode](../physics/parameters.md#background-estimate-mode) | estimation mode | — |
    | [method](../physics/parameters.md#background-estimate-method) | method | — |
    | [peak width](../physics/parameters.md#background-estimate-width) | peak width | — |
    | [smoothness](../physics/parameters.md#background-estimate-smoothness) | smoothness | — |
    | [points](../physics/parameters.md#background-estimate-n-points) | points | — |
    | [tolerance](../physics/parameters.md#background-estimate-tolerance) | tolerance | — |
    | [points in peaks](../physics/parameters.md#background-estimate-in-peaks) | points in peaks | — |
    | [calculated peaks](../physics/parameters.md#background-estimate-use-model) | calculated peaks | — |
    | [max terms](../physics/parameters.md#background-estimate-max-terms) | max terms | — |
    | [inputs digest](../physics/parameters.md#background-estimate-inputs-digest) | inputs digest | — |
    | [points digest](../physics/parameters.md#background-estimate-points-digest) | points digest | — |

    **[<span class="ed-reference-icon" data-reference-category="instrument" aria-hidden="true">&#62992;</span> Instrument](../physics/parameters.md#instrument)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [TOF offset](../physics/parameters.md#instrument-calib-d-to-tof-offset) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62263;</span> TOF offset | µs |
    | [TOF linear](../physics/parameters.md#instrument-calib-d-to-tof-linear) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63417;</span> TOF linear | µs/Å |
    | [TOF quadratic](../physics/parameters.md#instrument-calib-d-to-tof-quadratic) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63417;</span> TOF quadratic | µs/Å² |
    | [TOF reciprocal](../physics/parameters.md#instrument-calib-d-to-tof-reciprocal) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63417;</span> TOF reciprocal | µs·Å |
    | [2θ offset](../physics/parameters.md#instrument-calib-twotheta-offset) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62263;</span> 2θ offset | deg |
    | [Wavelength](../physics/parameters.md#instrument-setup-wavelength) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63417;</span> Wavelength | Å |
    | [Sample displacement](../physics/parameters.md#instrument-calib-sample-displacement) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62263;</span> Sample displacement | deg |
    | [Sample transparency](../physics/parameters.md#instrument-calib-sample-transparency) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62263;</span> Sample transparency | deg |
    | [Polarization coefficient](../physics/parameters.md#instrument-setup-polarization-coefficient) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> Polarization coefficient | — |
    | [Monochromator 2θ](../physics/parameters.md#instrument-setup-monochromator-twotheta) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> Monochromator 2θ | deg |
    | [Wavelength 2](../physics/parameters.md#instrument-setup-wavelength-2) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63417;</span> Wavelength 2 | Å |
    | [Intensity ratio 2/1](../physics/parameters.md#instrument-setup-wavelength-2-to-1-ratio) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63417;</span> Intensity ratio 2/1 | — |
    | [instrument](../physics/parameters.md#instrument-name) | instrument | — |
    | [facility](../physics/parameters.md#instrument-facility) | facility | — |
    | [2θ bank](../physics/parameters.md#instrument-setup-twotheta-bank) | 2θ bank | deg |

    **[<span class="ed-reference-icon" data-reference-category="peak" aria-hidden="true">&#63007;</span> Peak profile](../physics/parameters.md#peak)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [α₀](../physics/parameters.md#peak-rise-alpha-0) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> α₀ | — |
    | [α₁](../physics/parameters.md#peak-rise-alpha-1) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> α₁ | — |
    | [β₀](../physics/parameters.md#peak-decay-beta-0) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> β₀ | — |
    | [β₁](../physics/parameters.md#peak-decay-beta-1) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> β₁ | — |
    | [σ₀²](../physics/parameters.md#peak-broad-gauss-sigma-0) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> σ₀² | µs² |
    | [σ₁²](../physics/parameters.md#peak-broad-gauss-sigma-1) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> σ₁² | µs²/Å² |
    | [σ₂²](../physics/parameters.md#peak-broad-gauss-sigma-2) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> σ₂² | µs²/Å⁴ |
    | [size G](../physics/parameters.md#peak-broad-gauss-size) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> size G | — |
    | [strain G](../physics/parameters.md#peak-broad-gauss-strain) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> strain G | — |
    | [γ₀](../physics/parameters.md#peak-broad-lorentz-gamma-0) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> γ₀ | µs |
    | [γ₁](../physics/parameters.md#peak-broad-lorentz-gamma-1) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> γ₁ | µs/Å |
    | [γ₂](../physics/parameters.md#peak-broad-lorentz-gamma-2) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> γ₂ | µs/Å² |
    | [size L](../physics/parameters.md#peak-broad-lorentz-size) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> size L | — |
    | [strain L](../physics/parameters.md#peak-broad-lorentz-strain) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> strain L | — |
    | [U](../physics/parameters.md#peak-broad-gauss-u) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> U | deg² |
    | [V](../physics/parameters.md#peak-broad-gauss-v) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> V | deg² |
    | [W](../physics/parameters.md#peak-broad-gauss-w) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> W | deg² |
    | [X](../physics/parameters.md#peak-broad-lorentz-x) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> X | deg |
    | [Y](../physics/parameters.md#peak-broad-lorentz-y) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> Y | deg |
    | [Eta0](../physics/parameters.md#peak-mixing-eta-0) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> Eta0 | — |
    | [Eta1](../physics/parameters.md#peak-mixing-eta-1) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> Eta1 | 1/deg |
    | [S/L](../physics/parameters.md#peak-asym-fcj-1) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> S/L | — |
    | [D/L](../physics/parameters.md#peak-asym-fcj-2) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> D/L | — |
    | [A₀](../physics/parameters.md#peak-asym-beba-a0) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> A₀ | — |
    | [B₀](../physics/parameters.md#peak-asym-beba-b0) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> B₀ | — |
    | [A₁](../physics/parameters.md#peak-asym-beba-a1) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> A₁ | — |
    | [B₁](../physics/parameters.md#peak-asym-beba-b1) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> B₁ | — |
    | [AsyLim](../physics/parameters.md#peak-asym-beba-limit) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> AsyLim | deg |
    | [profile](../physics/parameters.md#peak-type) | profile | — |
    | [cutoff (FWHM)](../physics/parameters.md#peak-cutoff-fwhm) | cutoff (FWHM) | — |

    **[<span class="ed-reference-icon" data-reference-category="excluded-region" aria-hidden="true">&#61741;</span> Excluded region](../physics/parameters.md#excluded-region)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#excluded-region-id) | id | — |
    | [start](../physics/parameters.md#excluded-region-start) | start | deg |
    | [end](../physics/parameters.md#excluded-region-end) | end | deg |

    **[<span class="ed-reference-icon" data-reference-category="extinction" aria-hidden="true">&#62373;</span> Extinction](../physics/parameters.md#extinction)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [Domain radius](../physics/parameters.md#extinction-domain-radius) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> Domain radius | μm |
    | [Mosaic spread](../physics/parameters.md#extinction-mosaic-spread) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> Mosaic spread | rad⁻¹ |
    | [Crystal radius](../physics/parameters.md#extinction-crystal-radius) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> Crystal radius | mm |
    | [Extinction coefficient](../physics/parameters.md#extinction-coefficient) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> Extinction coefficient | — |
    | [x11](../physics/parameters.md#extinction-coefficient-11) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> x11 | — |
    | [x22](../physics/parameters.md#extinction-coefficient-22) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> x22 | — |
    | [x33](../physics/parameters.md#extinction-coefficient-33) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> x33 | — |
    | [x12](../physics/parameters.md#extinction-coefficient-12) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> x12 | — |
    | [x13](../physics/parameters.md#extinction-coefficient-13) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> x13 | — |
    | [x23](../physics/parameters.md#extinction-coefficient-23) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> x23 | — |
    | [type](../physics/parameters.md#extinction-type) | type | — |
    | [mosaic distribution](../physics/parameters.md#extinction-mosaic-distribution) | mosaic distribution | — |

    **[<span class="ed-reference-icon" data-reference-category="linked-structure" aria-hidden="true">&#62973;</span> Linked structure](../physics/parameters.md#linked-structure)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [scale](../physics/parameters.md#linked-structure-scale) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62614;</span> scale | — |
    | [structure](../physics/parameters.md#linked-structure-structure-id) | structure | — |
    | [enabled](../physics/parameters.md#linked-structure-enabled) | enabled | — |
    | [weight fraction](../physics/parameters.md#linked-structure-weight-fraction) | weight fraction | — |

    **[<span class="ed-reference-icon" data-reference-category="absorption" aria-hidden="true">&#61507;</span> Absorption](../physics/parameters.md#absorption)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [ABSCOR1](../physics/parameters.md#absorption-abscor1) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#61507;</span> ABSCOR1 | Å⁻¹ |
    | [ABSCOR2](../physics/parameters.md#absorption-abscor2) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#61507;</span> ABSCOR2 | — |
    | [μR](../physics/parameters.md#absorption-mu-r) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#61507;</span> μR | — |
    | [type](../physics/parameters.md#absorption-type) | type | — |

    **[<span class="ed-reference-icon" data-reference-category="preferred-orientation" aria-hidden="true">&#61774;</span> Preferred orientation](../physics/parameters.md#preferred-orientation)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [r](../physics/parameters.md#preferred-orientation-march-r) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#61774;</span> r | — |
    | [f rand](../physics/parameters.md#preferred-orientation-march-random-fract) | <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#61774;</span> f rand | — |
    | [structure](../physics/parameters.md#preferred-orientation-structure-id) | structure | — |
    | [h](../physics/parameters.md#preferred-orientation-index-h) | h | — |
    | [k](../physics/parameters.md#preferred-orientation-index-k) | k | — |
    | [l](../physics/parameters.md#preferred-orientation-index-l) | l | — |

    **[<span class="ed-reference-icon" data-reference-category="reflns" aria-hidden="true">&#61616;</span> Observed reflections](../physics/parameters.md#reflns)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [observed above (su)](../physics/parameters.md#reflns-threshold-sigma) | observed above (su) | — |
    | [on](../physics/parameters.md#reflns-threshold-basis) | on | — |
    | [threshold](../physics/parameters.md#reflns-threshold-expression) | threshold | — |

    **[<span class="ed-reference-icon" data-reference-category="scattering-source" aria-hidden="true">&#62930;</span> Scattering source](../physics/parameters.md#scattering-source)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [X-ray form factors](../physics/parameters.md#scattering-source-xray-form-factor) | X-ray form factors | — |
    | [X-ray dispersion](../physics/parameters.md#scattering-source-xray-dispersion) | X-ray dispersion | — |
    | [neutron scattering lengths](../physics/parameters.md#scattering-source-neutron-scattering-length) | neutron scattering lengths | — |

    **[<span class="ed-reference-icon" data-reference-category="data-source" aria-hidden="true">&#62831;</span> Data source](../physics/parameters.md#data-source)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [data file](../physics/parameters.md#data-source-file-name) | data file | — |

    **[<span class="ed-reference-icon" data-reference-category="data" aria-hidden="true">&#62263;</span> Measured data point](../physics/parameters.md#data)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [2θ](../physics/parameters.md#data-two-theta) | 2θ | deg |
    | [TOF](../physics/parameters.md#data-time-of-flight) | TOF | µs |
    | [meas](../physics/parameters.md#data-intensity-meas) | meas | — |
    | [s.u.](../physics/parameters.md#data-intensity-meas-su) | s.u. | — |
    | [d](../physics/parameters.md#data-d-spacing) | d | Å |
    | [calc](../physics/parameters.md#data-intensity-calc) | calc | — |
    | [bkg](../physics/parameters.md#data-intensity-bkg) | bkg | — |
    | [status](../physics/parameters.md#data-calc-status) | status | — |

    **[<span class="ed-reference-icon" data-reference-category="data-calc" aria-hidden="true">&#61950;</span> Calculated point](../physics/parameters.md#data-calc)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [point](../physics/parameters.md#data-calc-point-id) | point | — |

    **[<span class="ed-reference-icon" data-reference-category="pd-calc-overall" aria-hidden="true">&#61950;</span> Structure curves](../physics/parameters.md#pd-calc-overall)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [structure order](../physics/parameters.md#pd-calc-overall-component-presentation-order) | structure order | — |

    **[<span class="ed-reference-icon" data-reference-category="pd-calc" aria-hidden="true">&#61950;</span> Structure curve](../physics/parameters.md#pd-calc)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [structure calc](../physics/parameters.md#pd-calc-component-intensities-net) | structure calc | — |

    **[<span class="ed-reference-icon" data-reference-category="refln" aria-hidden="true">&#61498;</span> Reflection](../physics/parameters.md#refln)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [structure](../physics/parameters.md#refln-structure-id) | structure | — |
    | [d](../physics/parameters.md#refln-d-spacing) | d | Å |
    | [sin θ/λ](../physics/parameters.md#refln-sin-theta-over-lambda) | sin θ/λ | 1/Å |
    | [h](../physics/parameters.md#refln-index-h) | h | — |
    | [k](../physics/parameters.md#refln-index-k) | k | — |
    | [l](../physics/parameters.md#refln-index-l) | l | — |
    | [F calc](../physics/parameters.md#refln-f-calc) | F calc | — |
    | [F meas](../physics/parameters.md#refln-f-meas) | F meas | — |
    | [F² calc](../physics/parameters.md#refln-f-squared-calc) | F² calc | — |
    | [F² meas](../physics/parameters.md#refln-intensity-meas) | F² meas | — |
    | [s.u.](../physics/parameters.md#refln-intensity-meas-su) | s.u. | — |
    | [F² calc](../physics/parameters.md#refln-intensity-calc) | F² calc | — |
    | [λ](../physics/parameters.md#refln-wavelength) | λ | Å |
    | [2θ](../physics/parameters.md#refln-two-theta) | 2θ | deg |
    | [TOF](../physics/parameters.md#refln-time-of-flight) | TOF | µs |

=== "Edi"

    **[<span class="ed-reference-icon" data-reference-category="experiment-type" aria-hidden="true">&#63417;</span> Experiment type](../physics/parameters.md#experiment-type)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [beam mode](../physics/parameters.md#experiment-type-beam-mode) | <code>_experiment_type.beam_mode</code> | — |
    | [sample form](../physics/parameters.md#experiment-type-sample-form) | <code>_experiment_type.sample_form</code> | — |
    | [probe](../physics/parameters.md#experiment-type-radiation-probe) | <code>_experiment_type.radiation_probe</code> | — |
    | [scattering type](../physics/parameters.md#experiment-type-scattering-type) | <code>_experiment_type.scattering_type</code> | — |
    | [dimensionality](../physics/parameters.md#experiment-type-dimensionality) | <code>_experiment_type.dimensionality</code> | — |
    | [polarisation](../physics/parameters.md#experiment-type-polarisation) | <code>_experiment_type.polarisation</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="data-range" aria-hidden="true">&#62263;</span> Calculation range](../physics/parameters.md#data-range)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [min](../physics/parameters.md#data-range-two-theta-min) | <code>_data_range.two_theta_min</code> | deg |
    | [max](../physics/parameters.md#data-range-two-theta-max) | <code>_data_range.two_theta_max</code> | deg |
    | [step](../physics/parameters.md#data-range-two-theta-step) | <code>_data_range.two_theta_step</code> | deg |
    | [2θ](../physics/parameters.md#data-range-two-theta) | <code>_data_range.two_theta</code> | deg |
    | [min](../physics/parameters.md#data-range-time-of-flight-min) | <code>_data_range.time_of_flight_min</code> | µs |
    | [max](../physics/parameters.md#data-range-time-of-flight-max) | <code>_data_range.time_of_flight_max</code> | µs |
    | [step](../physics/parameters.md#data-range-time-of-flight-step) | <code>_data_range.time_of_flight_step</code> | µs |
    | [TOF](../physics/parameters.md#data-range-time-of-flight) | <code>_data_range.time_of_flight</code> | µs |

    **[<span class="ed-reference-icon" data-reference-category="background" aria-hidden="true">&#63550;</span> Background](../physics/parameters.md#background)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [intensity](../physics/parameters.md#background-intensity) | <code>_background.intensity</code> | — |
    | [position](../physics/parameters.md#background-position) | <code>_background.position</code> | µs |
    | [coefficient](../physics/parameters.md#background-coef) | <code>_background.coef</code> | — |
    | [order](../physics/parameters.md#background-order) | <code>_background.order</code> | — |
    | [origin](../physics/parameters.md#background-origin) | <code>_background.origin</code> | — |
    | [x min](../physics/parameters.md#background-x-min) | <code>_background.x_min</code> | — |
    | [x max](../physics/parameters.md#background-x-max) | <code>_background.x_max</code> | — |
    | [type](../physics/parameters.md#background-type) | <code>_background.type</code> | — |
    | [id](../physics/parameters.md#background-id) | <code>_background.id</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="background-estimate" aria-hidden="true">&#61648;</span> Background estimation](../physics/parameters.md#background-estimate)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [estimation mode](../physics/parameters.md#background-estimate-mode) | <code>_background_estimate.mode</code> | — |
    | [method](../physics/parameters.md#background-estimate-method) | <code>_background_estimate.method</code> | — |
    | [peak width](../physics/parameters.md#background-estimate-width) | <code>_background_estimate.width</code> | — |
    | [smoothness](../physics/parameters.md#background-estimate-smoothness) | <code>_background_estimate.smoothness</code> | — |
    | [points](../physics/parameters.md#background-estimate-n-points) | <code>_background_estimate.n_points</code> | — |
    | [tolerance](../physics/parameters.md#background-estimate-tolerance) | <code>_background_estimate.tolerance</code> | — |
    | [points in peaks](../physics/parameters.md#background-estimate-in-peaks) | <code>_background_estimate.in_peaks</code> | — |
    | [calculated peaks](../physics/parameters.md#background-estimate-use-model) | <code>_background_estimate.use_model</code> | — |
    | [max terms](../physics/parameters.md#background-estimate-max-terms) | <code>_background_estimate.max_terms</code> | — |
    | [inputs digest](../physics/parameters.md#background-estimate-inputs-digest) | <code>_background_estimate.inputs_digest</code> | — |
    | [points digest](../physics/parameters.md#background-estimate-points-digest) | <code>_background_estimate.points_digest</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="instrument" aria-hidden="true">&#62992;</span> Instrument](../physics/parameters.md#instrument)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [TOF offset](../physics/parameters.md#instrument-calib-d-to-tof-offset) | <code>_instrument.calib_d_to_tof_offset</code> | µs |
    | [TOF linear](../physics/parameters.md#instrument-calib-d-to-tof-linear) | <code>_instrument.calib_d_to_tof_linear</code> | µs/Å |
    | [TOF quadratic](../physics/parameters.md#instrument-calib-d-to-tof-quadratic) | <code>_instrument.calib_d_to_tof_quadratic</code> | µs/Å² |
    | [TOF reciprocal](../physics/parameters.md#instrument-calib-d-to-tof-reciprocal) | <code>_instrument.calib_d_to_tof_reciprocal</code> | µs·Å |
    | [2θ offset](../physics/parameters.md#instrument-calib-twotheta-offset) | <code>_instrument.calib_twotheta_offset</code> | deg |
    | [Wavelength](../physics/parameters.md#instrument-setup-wavelength) | <code>_instrument.setup_wavelength</code> | Å |
    | [Sample displacement](../physics/parameters.md#instrument-calib-sample-displacement) | <code>_instrument.calib_sample_displacement</code> | deg |
    | [Sample transparency](../physics/parameters.md#instrument-calib-sample-transparency) | <code>_instrument.calib_sample_transparency</code> | deg |
    | [Polarization coefficient](../physics/parameters.md#instrument-setup-polarization-coefficient) | <code>_instrument.setup_polarization_coefficient</code> | — |
    | [Monochromator 2θ](../physics/parameters.md#instrument-setup-monochromator-twotheta) | <code>_instrument.setup_monochromator_twotheta</code> | deg |
    | [Wavelength 2](../physics/parameters.md#instrument-setup-wavelength-2) | <code>_instrument.setup_wavelength_2</code> | Å |
    | [Intensity ratio 2/1](../physics/parameters.md#instrument-setup-wavelength-2-to-1-ratio) | <code>_instrument.setup_wavelength_2_to_1_ratio</code> | — |
    | [instrument](../physics/parameters.md#instrument-name) | <code>_instrument.name</code> | — |
    | [facility](../physics/parameters.md#instrument-facility) | <code>_instrument.facility</code> | — |
    | [2θ bank](../physics/parameters.md#instrument-setup-twotheta-bank) | <code>_instrument.setup_twotheta_bank</code> | deg |

    **[<span class="ed-reference-icon" data-reference-category="peak" aria-hidden="true">&#63007;</span> Peak profile](../physics/parameters.md#peak)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [α₀](../physics/parameters.md#peak-rise-alpha-0) | <code>_peak.rise_alpha_0</code> | — |
    | [α₁](../physics/parameters.md#peak-rise-alpha-1) | <code>_peak.rise_alpha_1</code> | — |
    | [β₀](../physics/parameters.md#peak-decay-beta-0) | <code>_peak.decay_beta_0</code> | — |
    | [β₁](../physics/parameters.md#peak-decay-beta-1) | <code>_peak.decay_beta_1</code> | — |
    | [σ₀²](../physics/parameters.md#peak-broad-gauss-sigma-0) | <code>_peak.broad_gauss_sigma_0</code> | µs² |
    | [σ₁²](../physics/parameters.md#peak-broad-gauss-sigma-1) | <code>_peak.broad_gauss_sigma_1</code> | µs²/Å² |
    | [σ₂²](../physics/parameters.md#peak-broad-gauss-sigma-2) | <code>_peak.broad_gauss_sigma_2</code> | µs²/Å⁴ |
    | [size G](../physics/parameters.md#peak-broad-gauss-size) | <code>_peak.broad_gauss_size</code> | — |
    | [strain G](../physics/parameters.md#peak-broad-gauss-strain) | <code>_peak.broad_gauss_strain</code> | — |
    | [γ₀](../physics/parameters.md#peak-broad-lorentz-gamma-0) | <code>_peak.broad_lorentz_gamma_0</code> | µs |
    | [γ₁](../physics/parameters.md#peak-broad-lorentz-gamma-1) | <code>_peak.broad_lorentz_gamma_1</code> | µs/Å |
    | [γ₂](../physics/parameters.md#peak-broad-lorentz-gamma-2) | <code>_peak.broad_lorentz_gamma_2</code> | µs/Å² |
    | [size L](../physics/parameters.md#peak-broad-lorentz-size) | <code>_peak.broad_lorentz_size</code> | — |
    | [strain L](../physics/parameters.md#peak-broad-lorentz-strain) | <code>_peak.broad_lorentz_strain</code> | — |
    | [U](../physics/parameters.md#peak-broad-gauss-u) | <code>_peak.broad_gauss_u</code> | deg² |
    | [V](../physics/parameters.md#peak-broad-gauss-v) | <code>_peak.broad_gauss_v</code> | deg² |
    | [W](../physics/parameters.md#peak-broad-gauss-w) | <code>_peak.broad_gauss_w</code> | deg² |
    | [X](../physics/parameters.md#peak-broad-lorentz-x) | <code>_peak.broad_lorentz_x</code> | deg |
    | [Y](../physics/parameters.md#peak-broad-lorentz-y) | <code>_peak.broad_lorentz_y</code> | deg |
    | [Eta0](../physics/parameters.md#peak-mixing-eta-0) | <code>_peak.mixing_eta_0</code> | — |
    | [Eta1](../physics/parameters.md#peak-mixing-eta-1) | <code>_peak.mixing_eta_1</code> | 1/deg |
    | [S/L](../physics/parameters.md#peak-asym-fcj-1) | <code>_peak.asym_fcj_1</code> | — |
    | [D/L](../physics/parameters.md#peak-asym-fcj-2) | <code>_peak.asym_fcj_2</code> | — |
    | [A₀](../physics/parameters.md#peak-asym-beba-a0) | <code>_peak.asym_beba_a0</code> | — |
    | [B₀](../physics/parameters.md#peak-asym-beba-b0) | <code>_peak.asym_beba_b0</code> | — |
    | [A₁](../physics/parameters.md#peak-asym-beba-a1) | <code>_peak.asym_beba_a1</code> | — |
    | [B₁](../physics/parameters.md#peak-asym-beba-b1) | <code>_peak.asym_beba_b1</code> | — |
    | [AsyLim](../physics/parameters.md#peak-asym-beba-limit) | <code>_peak.asym_beba_limit</code> | deg |
    | [profile](../physics/parameters.md#peak-type) | <code>_peak.type</code> | — |
    | [cutoff (FWHM)](../physics/parameters.md#peak-cutoff-fwhm) | <code>_peak.cutoff_fwhm</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="excluded-region" aria-hidden="true">&#61741;</span> Excluded region](../physics/parameters.md#excluded-region)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#excluded-region-id) | <code>_excluded_region.id</code> | — |
    | [start](../physics/parameters.md#excluded-region-start) | <code>_excluded_region.start</code> | deg |
    | [end](../physics/parameters.md#excluded-region-end) | <code>_excluded_region.end</code> | deg |

    **[<span class="ed-reference-icon" data-reference-category="extinction" aria-hidden="true">&#62373;</span> Extinction](../physics/parameters.md#extinction)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [Domain radius](../physics/parameters.md#extinction-domain-radius) | <code>_extinction.domain_radius</code> | μm |
    | [Mosaic spread](../physics/parameters.md#extinction-mosaic-spread) | <code>_extinction.mosaic_spread</code> | rad⁻¹ |
    | [Crystal radius](../physics/parameters.md#extinction-crystal-radius) | <code>_extinction.crystal_radius</code> | mm |
    | [Extinction coefficient](../physics/parameters.md#extinction-coefficient) | <code>_extinction.coefficient</code> | — |
    | [x11](../physics/parameters.md#extinction-coefficient-11) | <code>_extinction.coefficient_11</code> | — |
    | [x22](../physics/parameters.md#extinction-coefficient-22) | <code>_extinction.coefficient_22</code> | — |
    | [x33](../physics/parameters.md#extinction-coefficient-33) | <code>_extinction.coefficient_33</code> | — |
    | [x12](../physics/parameters.md#extinction-coefficient-12) | <code>_extinction.coefficient_12</code> | — |
    | [x13](../physics/parameters.md#extinction-coefficient-13) | <code>_extinction.coefficient_13</code> | — |
    | [x23](../physics/parameters.md#extinction-coefficient-23) | <code>_extinction.coefficient_23</code> | — |
    | [type](../physics/parameters.md#extinction-type) | <code>_extinction.type</code> | — |
    | [mosaic distribution](../physics/parameters.md#extinction-mosaic-distribution) | <code>_extinction.mosaic_distribution</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="linked-structure" aria-hidden="true">&#62973;</span> Linked structure](../physics/parameters.md#linked-structure)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [scale](../physics/parameters.md#linked-structure-scale) | <code>_linked_structure.scale</code> | — |
    | [structure](../physics/parameters.md#linked-structure-structure-id) | <code>_linked_structure.structure_id</code> | — |
    | [enabled](../physics/parameters.md#linked-structure-enabled) | <code>_linked_structure.enabled</code> | — |
    | [weight fraction](../physics/parameters.md#linked-structure-weight-fraction) | <code>_linked_structure.weight_fraction</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="absorption" aria-hidden="true">&#61507;</span> Absorption](../physics/parameters.md#absorption)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [ABSCOR1](../physics/parameters.md#absorption-abscor1) | <code>_absorption.abscor1</code> | Å⁻¹ |
    | [ABSCOR2](../physics/parameters.md#absorption-abscor2) | <code>_absorption.abscor2</code> | — |
    | [μR](../physics/parameters.md#absorption-mu-r) | <code>_absorption.mu_r</code> | — |
    | [type](../physics/parameters.md#absorption-type) | <code>_absorption.type</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="preferred-orientation" aria-hidden="true">&#61774;</span> Preferred orientation](../physics/parameters.md#preferred-orientation)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [r](../physics/parameters.md#preferred-orientation-march-r) | <code>_preferred_orientation.march_r</code> | — |
    | [f rand](../physics/parameters.md#preferred-orientation-march-random-fract) | <code>_preferred_orientation.march_random_fract</code> | — |
    | [structure](../physics/parameters.md#preferred-orientation-structure-id) | <code>_preferred_orientation.structure_id</code> | — |
    | [h](../physics/parameters.md#preferred-orientation-index-h) | <code>_preferred_orientation.index_h</code> | — |
    | [k](../physics/parameters.md#preferred-orientation-index-k) | <code>_preferred_orientation.index_k</code> | — |
    | [l](../physics/parameters.md#preferred-orientation-index-l) | <code>_preferred_orientation.index_l</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="reflns" aria-hidden="true">&#61616;</span> Observed reflections](../physics/parameters.md#reflns)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [observed above (su)](../physics/parameters.md#reflns-threshold-sigma) | <code>_reflns.threshold_sigma</code> | — |
    | [on](../physics/parameters.md#reflns-threshold-basis) | <code>_reflns.threshold_basis</code> | — |
    | [threshold](../physics/parameters.md#reflns-threshold-expression) | <code>_reflns.threshold_expression</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="scattering-source" aria-hidden="true">&#62930;</span> Scattering source](../physics/parameters.md#scattering-source)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [X-ray form factors](../physics/parameters.md#scattering-source-xray-form-factor) | <code>_scattering_source.xray_form_factor</code> | — |
    | [X-ray dispersion](../physics/parameters.md#scattering-source-xray-dispersion) | <code>_scattering_source.xray_dispersion</code> | — |
    | [neutron scattering lengths](../physics/parameters.md#scattering-source-neutron-scattering-length) | <code>_scattering_source.neutron_scattering_length</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="data-source" aria-hidden="true">&#62831;</span> Data source](../physics/parameters.md#data-source)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [data file](../physics/parameters.md#data-source-file-name) | <code>_data_source.file_name</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="data" aria-hidden="true">&#62263;</span> Measured data point](../physics/parameters.md#data)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [2θ](../physics/parameters.md#data-two-theta) | <code>_data.two_theta</code> | deg |
    | [TOF](../physics/parameters.md#data-time-of-flight) | <code>_data.time_of_flight</code> | µs |
    | [meas](../physics/parameters.md#data-intensity-meas) | <code>_data.intensity_meas</code> | — |
    | [s.u.](../physics/parameters.md#data-intensity-meas-su) | <code>_data.intensity_meas_su</code> | — |
    | [d](../physics/parameters.md#data-d-spacing) | <code>_data.d_spacing</code> | Å |
    | [calc](../physics/parameters.md#data-intensity-calc) | <code>_data.intensity_calc</code> | — |
    | [bkg](../physics/parameters.md#data-intensity-bkg) | <code>_data.intensity_bkg</code> | — |
    | [status](../physics/parameters.md#data-calc-status) | <code>_data.calc_status</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="data-calc" aria-hidden="true">&#61950;</span> Calculated point](../physics/parameters.md#data-calc)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [point](../physics/parameters.md#data-calc-point-id) | <code>_data_calc.point_id</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="pd-calc-overall" aria-hidden="true">&#61950;</span> Structure curves](../physics/parameters.md#pd-calc-overall)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [structure order](../physics/parameters.md#pd-calc-overall-component-presentation-order) | <code>_pd_calc_overall.component_presentation_order</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="pd-calc" aria-hidden="true">&#61950;</span> Structure curve](../physics/parameters.md#pd-calc)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [structure calc](../physics/parameters.md#pd-calc-component-intensities-net) | <code>_pd_calc.component_intensities_net</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="refln" aria-hidden="true">&#61498;</span> Reflection](../physics/parameters.md#refln)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [structure](../physics/parameters.md#refln-structure-id) | <code>_refln.structure_id</code> | — |
    | [d](../physics/parameters.md#refln-d-spacing) | <code>_refln.d_spacing</code> | Å |
    | [sin θ/λ](../physics/parameters.md#refln-sin-theta-over-lambda) | <code>_refln.sin_theta_over_lambda</code> | 1/Å |
    | [h](../physics/parameters.md#refln-index-h) | <code>_refln.index_h</code> | — |
    | [k](../physics/parameters.md#refln-index-k) | <code>_refln.index_k</code> | — |
    | [l](../physics/parameters.md#refln-index-l) | <code>_refln.index_l</code> | — |
    | [F calc](../physics/parameters.md#refln-f-calc) | <code>_refln.f_calc</code> | — |
    | [F meas](../physics/parameters.md#refln-f-meas) | <code>_refln.f_meas</code> | — |
    | [F² calc](../physics/parameters.md#refln-f-squared-calc) | <code>_refln.f_squared_calc</code> | — |
    | [F² meas](../physics/parameters.md#refln-intensity-meas) | <code>_refln.intensity_meas</code> | — |
    | [s.u.](../physics/parameters.md#refln-intensity-meas-su) | <code>_refln.intensity_meas_su</code> | — |
    | [F² calc](../physics/parameters.md#refln-intensity-calc) | <code>_refln.intensity_calc</code> | — |
    | [λ](../physics/parameters.md#refln-wavelength) | <code>_refln.wavelength</code> | Å |
    | [2θ](../physics/parameters.md#refln-two-theta) | <code>_refln.two_theta</code> | deg |
    | [TOF](../physics/parameters.md#refln-time-of-flight) | <code>_refln.time_of_flight</code> | µs |

=== "Python"

    **[<span class="ed-reference-icon" data-reference-category="experiment-type" aria-hidden="true">&#63417;</span> Experiment type](../physics/parameters.md#experiment-type)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [beam mode](../physics/parameters.md#experiment-type-beam-mode) | <code>project.experiments[0].experiment_type.beam_mode</code> | — |
    | [sample form](../physics/parameters.md#experiment-type-sample-form) | <code>project.experiments[0].experiment_type.sample_form</code> | — |
    | [probe](../physics/parameters.md#experiment-type-radiation-probe) | <code>project.experiments[0].experiment_type.radiation_probe</code> | — |
    | [scattering type](../physics/parameters.md#experiment-type-scattering-type) | <code>project.experiments[0].experiment_type.scattering_type</code> | — |
    | [dimensionality](../physics/parameters.md#experiment-type-dimensionality) | <code>project.experiments[0].experiment_type.dimensionality</code> | — |
    | [polarisation](../physics/parameters.md#experiment-type-polarisation) | <code>project.experiments[0].experiment_type.polarisation</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="data-range" aria-hidden="true">&#62263;</span> Calculation range](../physics/parameters.md#data-range)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [min](../physics/parameters.md#data-range-two-theta-min) | — | deg |
    | [max](../physics/parameters.md#data-range-two-theta-max) | — | deg |
    | [step](../physics/parameters.md#data-range-two-theta-step) | — | deg |
    | [2θ](../physics/parameters.md#data-range-two-theta) | — | deg |
    | [min](../physics/parameters.md#data-range-time-of-flight-min) | — | µs |
    | [max](../physics/parameters.md#data-range-time-of-flight-max) | — | µs |
    | [step](../physics/parameters.md#data-range-time-of-flight-step) | — | µs |
    | [TOF](../physics/parameters.md#data-range-time-of-flight) | — | µs |

    **[<span class="ed-reference-icon" data-reference-category="background" aria-hidden="true">&#63550;</span> Background](../physics/parameters.md#background)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [intensity](../physics/parameters.md#background-intensity) | <code>project.experiments[0].background[0].intensity</code> | — |
    | [position](../physics/parameters.md#background-position) | <code>project.experiments[0].background[0].position</code> | µs |
    | [coefficient](../physics/parameters.md#background-coef) | — | — |
    | [order](../physics/parameters.md#background-order) | — | — |
    | [origin](../physics/parameters.md#background-origin) | <code>project.experiments[0].background_origin</code> | — |
    | [x min](../physics/parameters.md#background-x-min) | <code>project.experiments[0].background_x_min</code> | — |
    | [x max](../physics/parameters.md#background-x-max) | <code>project.experiments[0].background_x_max</code> | — |
    | [type](../physics/parameters.md#background-type) | <code>project.experiments[0].background_type</code> | — |
    | [id](../physics/parameters.md#background-id) | <code>project.experiments[0].background[0].id</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="background-estimate" aria-hidden="true">&#61648;</span> Background estimation](../physics/parameters.md#background-estimate)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [estimation mode](../physics/parameters.md#background-estimate-mode) | — | — |
    | [method](../physics/parameters.md#background-estimate-method) | — | — |
    | [peak width](../physics/parameters.md#background-estimate-width) | — | — |
    | [smoothness](../physics/parameters.md#background-estimate-smoothness) | — | — |
    | [points](../physics/parameters.md#background-estimate-n-points) | — | — |
    | [tolerance](../physics/parameters.md#background-estimate-tolerance) | — | — |
    | [points in peaks](../physics/parameters.md#background-estimate-in-peaks) | — | — |
    | [calculated peaks](../physics/parameters.md#background-estimate-use-model) | — | — |
    | [max terms](../physics/parameters.md#background-estimate-max-terms) | — | — |
    | [inputs digest](../physics/parameters.md#background-estimate-inputs-digest) | — | — |
    | [points digest](../physics/parameters.md#background-estimate-points-digest) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="instrument" aria-hidden="true">&#62992;</span> Instrument](../physics/parameters.md#instrument)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [TOF offset](../physics/parameters.md#instrument-calib-d-to-tof-offset) | <code>project.experiments[0].instrument.calib_d_to_tof_offset</code> | µs |
    | [TOF linear](../physics/parameters.md#instrument-calib-d-to-tof-linear) | <code>project.experiments[0].instrument.calib_d_to_tof_linear</code> | µs/Å |
    | [TOF quadratic](../physics/parameters.md#instrument-calib-d-to-tof-quadratic) | <code>project.experiments[0].instrument.calib_d_to_tof_quadratic</code> | µs/Å² |
    | [TOF reciprocal](../physics/parameters.md#instrument-calib-d-to-tof-reciprocal) | <code>project.experiments[0].instrument.calib_d_to_tof_reciprocal</code> | µs·Å |
    | [2θ offset](../physics/parameters.md#instrument-calib-twotheta-offset) | <code>project.experiments[0].instrument.calib_twotheta_offset</code> | deg |
    | [Wavelength](../physics/parameters.md#instrument-setup-wavelength) | <code>project.experiments[0].instrument.setup_wavelength</code> | Å |
    | [Sample displacement](../physics/parameters.md#instrument-calib-sample-displacement) | <code>project.experiments[0].instrument.calib_sample_displacement</code> | deg |
    | [Sample transparency](../physics/parameters.md#instrument-calib-sample-transparency) | <code>project.experiments[0].instrument.calib_sample_transparency</code> | deg |
    | [Polarization coefficient](../physics/parameters.md#instrument-setup-polarization-coefficient) | <code>project.experiments[0].instrument.setup_polarization_coefficient</code> | — |
    | [Monochromator 2θ](../physics/parameters.md#instrument-setup-monochromator-twotheta) | <code>project.experiments[0].instrument.setup_monochromator_twotheta</code> | deg |
    | [Wavelength 2](../physics/parameters.md#instrument-setup-wavelength-2) | <code>project.experiments[0].instrument.setup_wavelength_2</code> | Å |
    | [Intensity ratio 2/1](../physics/parameters.md#instrument-setup-wavelength-2-to-1-ratio) | <code>project.experiments[0].instrument.setup_wavelength_2_to_1_ratio</code> | — |
    | [instrument](../physics/parameters.md#instrument-name) | <code>project.experiments[0].instrument.name</code> | — |
    | [facility](../physics/parameters.md#instrument-facility) | <code>project.experiments[0].instrument.facility</code> | — |
    | [2θ bank](../physics/parameters.md#instrument-setup-twotheta-bank) | <code>project.experiments[0].instrument.setup_twotheta_bank</code> | deg |

    **[<span class="ed-reference-icon" data-reference-category="peak" aria-hidden="true">&#63007;</span> Peak profile](../physics/parameters.md#peak)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [α₀](../physics/parameters.md#peak-rise-alpha-0) | <code>project.experiments[0].peak.rise_alpha_0</code> | — |
    | [α₁](../physics/parameters.md#peak-rise-alpha-1) | <code>project.experiments[0].peak.rise_alpha_1</code> | — |
    | [β₀](../physics/parameters.md#peak-decay-beta-0) | <code>project.experiments[0].peak.decay_beta_0</code> | — |
    | [β₁](../physics/parameters.md#peak-decay-beta-1) | <code>project.experiments[0].peak.decay_beta_1</code> | — |
    | [σ₀²](../physics/parameters.md#peak-broad-gauss-sigma-0) | <code>project.experiments[0].peak.broad_gauss_sigma_0</code> | µs² |
    | [σ₁²](../physics/parameters.md#peak-broad-gauss-sigma-1) | <code>project.experiments[0].peak.broad_gauss_sigma_1</code> | µs²/Å² |
    | [σ₂²](../physics/parameters.md#peak-broad-gauss-sigma-2) | <code>project.experiments[0].peak.broad_gauss_sigma_2</code> | µs²/Å⁴ |
    | [size G](../physics/parameters.md#peak-broad-gauss-size) | <code>project.experiments[0].peak.broad_gauss_size</code> | — |
    | [strain G](../physics/parameters.md#peak-broad-gauss-strain) | <code>project.experiments[0].peak.broad_gauss_strain</code> | — |
    | [γ₀](../physics/parameters.md#peak-broad-lorentz-gamma-0) | <code>project.experiments[0].peak.broad_lorentz_gamma_0</code> | µs |
    | [γ₁](../physics/parameters.md#peak-broad-lorentz-gamma-1) | <code>project.experiments[0].peak.broad_lorentz_gamma_1</code> | µs/Å |
    | [γ₂](../physics/parameters.md#peak-broad-lorentz-gamma-2) | <code>project.experiments[0].peak.broad_lorentz_gamma_2</code> | µs/Å² |
    | [size L](../physics/parameters.md#peak-broad-lorentz-size) | <code>project.experiments[0].peak.broad_lorentz_size</code> | — |
    | [strain L](../physics/parameters.md#peak-broad-lorentz-strain) | <code>project.experiments[0].peak.broad_lorentz_strain</code> | — |
    | [U](../physics/parameters.md#peak-broad-gauss-u) | <code>project.experiments[0].peak.broad_gauss_u</code> | deg² |
    | [V](../physics/parameters.md#peak-broad-gauss-v) | <code>project.experiments[0].peak.broad_gauss_v</code> | deg² |
    | [W](../physics/parameters.md#peak-broad-gauss-w) | <code>project.experiments[0].peak.broad_gauss_w</code> | deg² |
    | [X](../physics/parameters.md#peak-broad-lorentz-x) | <code>project.experiments[0].peak.broad_lorentz_x</code> | deg |
    | [Y](../physics/parameters.md#peak-broad-lorentz-y) | <code>project.experiments[0].peak.broad_lorentz_y</code> | deg |
    | [Eta0](../physics/parameters.md#peak-mixing-eta-0) | <code>project.experiments[0].peak.mixing_eta_0</code> | — |
    | [Eta1](../physics/parameters.md#peak-mixing-eta-1) | <code>project.experiments[0].peak.mixing_eta_1</code> | 1/deg |
    | [S/L](../physics/parameters.md#peak-asym-fcj-1) | <code>project.experiments[0].peak.asym_fcj_1</code> | — |
    | [D/L](../physics/parameters.md#peak-asym-fcj-2) | <code>project.experiments[0].peak.asym_fcj_2</code> | — |
    | [A₀](../physics/parameters.md#peak-asym-beba-a0) | <code>project.experiments[0].peak.asym_beba_a0</code> | — |
    | [B₀](../physics/parameters.md#peak-asym-beba-b0) | <code>project.experiments[0].peak.asym_beba_b0</code> | — |
    | [A₁](../physics/parameters.md#peak-asym-beba-a1) | <code>project.experiments[0].peak.asym_beba_a1</code> | — |
    | [B₁](../physics/parameters.md#peak-asym-beba-b1) | <code>project.experiments[0].peak.asym_beba_b1</code> | — |
    | [AsyLim](../physics/parameters.md#peak-asym-beba-limit) | <code>project.experiments[0].peak.asym_beba_limit</code> | deg |
    | [profile](../physics/parameters.md#peak-type) | <code>project.experiments[0].peak.type</code> | — |
    | [cutoff (FWHM)](../physics/parameters.md#peak-cutoff-fwhm) | <code>project.experiments[0].peak.cutoff_fwhm</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="excluded-region" aria-hidden="true">&#61741;</span> Excluded region](../physics/parameters.md#excluded-region)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#excluded-region-id) | — | — |
    | [start](../physics/parameters.md#excluded-region-start) | — | deg |
    | [end](../physics/parameters.md#excluded-region-end) | — | deg |

    **[<span class="ed-reference-icon" data-reference-category="extinction" aria-hidden="true">&#62373;</span> Extinction](../physics/parameters.md#extinction)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [Domain radius](../physics/parameters.md#extinction-domain-radius) | — | μm |
    | [Mosaic spread](../physics/parameters.md#extinction-mosaic-spread) | — | rad⁻¹ |
    | [Crystal radius](../physics/parameters.md#extinction-crystal-radius) | — | mm |
    | [Extinction coefficient](../physics/parameters.md#extinction-coefficient) | — | — |
    | [x11](../physics/parameters.md#extinction-coefficient-11) | — | — |
    | [x22](../physics/parameters.md#extinction-coefficient-22) | — | — |
    | [x33](../physics/parameters.md#extinction-coefficient-33) | — | — |
    | [x12](../physics/parameters.md#extinction-coefficient-12) | — | — |
    | [x13](../physics/parameters.md#extinction-coefficient-13) | — | — |
    | [x23](../physics/parameters.md#extinction-coefficient-23) | — | — |
    | [type](../physics/parameters.md#extinction-type) | — | — |
    | [mosaic distribution](../physics/parameters.md#extinction-mosaic-distribution) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="linked-structure" aria-hidden="true">&#62973;</span> Linked structure](../physics/parameters.md#linked-structure)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [scale](../physics/parameters.md#linked-structure-scale) | <code>project.experiments[0].linked_structures[0].scale</code> | — |
    | [structure](../physics/parameters.md#linked-structure-structure-id) | <code>project.experiments[0].linked_structures[0].structure_id</code> | — |
    | [enabled](../physics/parameters.md#linked-structure-enabled) | <code>project.experiments[0].linked_structures[0].enabled</code> | — |
    | [weight fraction](../physics/parameters.md#linked-structure-weight-fraction) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="absorption" aria-hidden="true">&#61507;</span> Absorption](../physics/parameters.md#absorption)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [ABSCOR1](../physics/parameters.md#absorption-abscor1) | <code>project.experiments[0].absorption.abscor1</code> | Å⁻¹ |
    | [ABSCOR2](../physics/parameters.md#absorption-abscor2) | <code>project.experiments[0].absorption.abscor2</code> | — |
    | [μR](../physics/parameters.md#absorption-mu-r) | <code>project.experiments[0].absorption.mu_r</code> | — |
    | [type](../physics/parameters.md#absorption-type) | <code>project.experiments[0].absorption.type</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="preferred-orientation" aria-hidden="true">&#61774;</span> Preferred orientation](../physics/parameters.md#preferred-orientation)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [r](../physics/parameters.md#preferred-orientation-march-r) | — | — |
    | [f rand](../physics/parameters.md#preferred-orientation-march-random-fract) | — | — |
    | [structure](../physics/parameters.md#preferred-orientation-structure-id) | — | — |
    | [h](../physics/parameters.md#preferred-orientation-index-h) | — | — |
    | [k](../physics/parameters.md#preferred-orientation-index-k) | — | — |
    | [l](../physics/parameters.md#preferred-orientation-index-l) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="reflns" aria-hidden="true">&#61616;</span> Observed reflections](../physics/parameters.md#reflns)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [observed above (su)](../physics/parameters.md#reflns-threshold-sigma) | — | — |
    | [on](../physics/parameters.md#reflns-threshold-basis) | — | — |
    | [threshold](../physics/parameters.md#reflns-threshold-expression) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="scattering-source" aria-hidden="true">&#62930;</span> Scattering source](../physics/parameters.md#scattering-source)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [X-ray form factors](../physics/parameters.md#scattering-source-xray-form-factor) | — | — |
    | [X-ray dispersion](../physics/parameters.md#scattering-source-xray-dispersion) | — | — |
    | [neutron scattering lengths](../physics/parameters.md#scattering-source-neutron-scattering-length) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="data-source" aria-hidden="true">&#62831;</span> Data source](../physics/parameters.md#data-source)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [data file](../physics/parameters.md#data-source-file-name) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="data" aria-hidden="true">&#62263;</span> Measured data point](../physics/parameters.md#data)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [2θ](../physics/parameters.md#data-two-theta) | — | deg |
    | [TOF](../physics/parameters.md#data-time-of-flight) | — | µs |
    | [meas](../physics/parameters.md#data-intensity-meas) | — | — |
    | [s.u.](../physics/parameters.md#data-intensity-meas-su) | — | — |
    | [d](../physics/parameters.md#data-d-spacing) | — | Å |
    | [calc](../physics/parameters.md#data-intensity-calc) | — | — |
    | [bkg](../physics/parameters.md#data-intensity-bkg) | — | — |
    | [status](../physics/parameters.md#data-calc-status) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="data-calc" aria-hidden="true">&#61950;</span> Calculated point](../physics/parameters.md#data-calc)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [point](../physics/parameters.md#data-calc-point-id) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="pd-calc-overall" aria-hidden="true">&#61950;</span> Structure curves](../physics/parameters.md#pd-calc-overall)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [structure order](../physics/parameters.md#pd-calc-overall-component-presentation-order) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="pd-calc" aria-hidden="true">&#61950;</span> Structure curve](../physics/parameters.md#pd-calc)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [structure calc](../physics/parameters.md#pd-calc-component-intensities-net) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="refln" aria-hidden="true">&#61498;</span> Reflection](../physics/parameters.md#refln)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [structure](../physics/parameters.md#refln-structure-id) | — | — |
    | [d](../physics/parameters.md#refln-d-spacing) | — | Å |
    | [sin θ/λ](../physics/parameters.md#refln-sin-theta-over-lambda) | — | 1/Å |
    | [h](../physics/parameters.md#refln-index-h) | — | — |
    | [k](../physics/parameters.md#refln-index-k) | — | — |
    | [l](../physics/parameters.md#refln-index-l) | — | — |
    | [F calc](../physics/parameters.md#refln-f-calc) | — | — |
    | [F meas](../physics/parameters.md#refln-f-meas) | — | — |
    | [F² calc](../physics/parameters.md#refln-f-squared-calc) | — | — |
    | [F² meas](../physics/parameters.md#refln-intensity-meas) | — | — |
    | [s.u.](../physics/parameters.md#refln-intensity-meas-su) | — | — |
    | [F² calc](../physics/parameters.md#refln-intensity-calc) | — | — |
    | [λ](../physics/parameters.md#refln-wavelength) | — | Å |
    | [2θ](../physics/parameters.md#refln-two-theta) | — | deg |
    | [TOF](../physics/parameters.md#refln-time-of-flight) | — | µs |

=== "CIF"

    **[<span class="ed-reference-icon" data-reference-category="experiment-type" aria-hidden="true">&#63417;</span> Experiment type](../physics/parameters.md#experiment-type)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [beam mode](../physics/parameters.md#experiment-type-beam-mode) | <code>_edi_experiment_type.beam_mode</code> | — |
    | [sample form](../physics/parameters.md#experiment-type-sample-form) | <code>_edi_experiment_type.sample_form</code> | — |
    | [probe](../physics/parameters.md#experiment-type-radiation-probe) | <code>_diffrn_radiation.probe</code> | — |
    | [scattering type](../physics/parameters.md#experiment-type-scattering-type) | <code>_edi_experiment_type.scattering_type</code> | — |
    | [dimensionality](../physics/parameters.md#experiment-type-dimensionality) | <code>_edi_experiment_type.dimensionality</code> | — |
    | [polarisation](../physics/parameters.md#experiment-type-polarisation) | <code>_edi_experiment_type.polarisation</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="data-range" aria-hidden="true">&#62263;</span> Calculation range](../physics/parameters.md#data-range)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [min](../physics/parameters.md#data-range-two-theta-min) | <code>_pd_meas.2theta_range_min</code> | deg |
    | [max](../physics/parameters.md#data-range-two-theta-max) | <code>_pd_meas.2theta_range_max</code> | deg |
    | [step](../physics/parameters.md#data-range-two-theta-step) | <code>_pd_meas.2theta_range_inc</code> | deg |
    | [2θ](../physics/parameters.md#data-range-two-theta) | <code>_edi_data_range.two_theta</code> | deg |
    | [min](../physics/parameters.md#data-range-time-of-flight-min) | <code>_edi_data_range.time_of_flight_min</code> | µs |
    | [max](../physics/parameters.md#data-range-time-of-flight-max) | <code>_edi_data_range.time_of_flight_max</code> | µs |
    | [step](../physics/parameters.md#data-range-time-of-flight-step) | <code>_edi_data_range.time_of_flight_step</code> | µs |
    | [TOF](../physics/parameters.md#data-range-time-of-flight) | <code>_edi_data_range.time_of_flight</code> | µs |

    **[<span class="ed-reference-icon" data-reference-category="background" aria-hidden="true">&#63550;</span> Background](../physics/parameters.md#background)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [intensity](../physics/parameters.md#background-intensity) | <code>_pd_background.line_segment_intensity</code> | — |
    | [position](../physics/parameters.md#background-position) | <code>_pd_background.line_segment_X</code> | µs |
    | [coefficient](../physics/parameters.md#background-coef) | <code>_pd_background.Chebyshev_coef</code> | — |
    | [order](../physics/parameters.md#background-order) | <code>_pd_background.Chebyshev_order</code> | — |
    | [origin](../physics/parameters.md#background-origin) | <code>_edi_background.origin</code> | — |
    | [x min](../physics/parameters.md#background-x-min) | <code>_edi_background.x_min</code> | — |
    | [x max](../physics/parameters.md#background-x-max) | <code>_edi_background.x_max</code> | — |
    | [type](../physics/parameters.md#background-type) | <code>_edi_background.type</code> | — |
    | [id](../physics/parameters.md#background-id) | <code>_pd_background.id</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="background-estimate" aria-hidden="true">&#61648;</span> Background estimation](../physics/parameters.md#background-estimate)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [estimation mode](../physics/parameters.md#background-estimate-mode) | <code>_edi_background_estimate.mode</code> | — |
    | [method](../physics/parameters.md#background-estimate-method) | <code>_edi_background_estimate.method</code> | — |
    | [peak width](../physics/parameters.md#background-estimate-width) | <code>_edi_background_estimate.width</code> | — |
    | [smoothness](../physics/parameters.md#background-estimate-smoothness) | <code>_edi_background_estimate.smoothness</code> | — |
    | [points](../physics/parameters.md#background-estimate-n-points) | <code>_edi_background_estimate.n_points</code> | — |
    | [tolerance](../physics/parameters.md#background-estimate-tolerance) | <code>_edi_background_estimate.tolerance</code> | — |
    | [points in peaks](../physics/parameters.md#background-estimate-in-peaks) | <code>_edi_background_estimate.in_peaks</code> | — |
    | [calculated peaks](../physics/parameters.md#background-estimate-use-model) | <code>_edi_background_estimate.use_model</code> | — |
    | [max terms](../physics/parameters.md#background-estimate-max-terms) | <code>_edi_background_estimate.max_terms</code> | — |
    | [inputs digest](../physics/parameters.md#background-estimate-inputs-digest) | <code>_edi_background_estimate.inputs_digest</code> | — |
    | [points digest](../physics/parameters.md#background-estimate-points-digest) | <code>_edi_background_estimate.points_digest</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="instrument" aria-hidden="true">&#62992;</span> Instrument](../physics/parameters.md#instrument)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [TOF offset](../physics/parameters.md#instrument-calib-d-to-tof-offset) | <code>_edi_instrument.calib_d_to_tof_offset</code> | µs |
    | [TOF linear](../physics/parameters.md#instrument-calib-d-to-tof-linear) | <code>_edi_instrument.calib_d_to_tof_linear</code> | µs/Å |
    | [TOF quadratic](../physics/parameters.md#instrument-calib-d-to-tof-quadratic) | <code>_edi_instrument.calib_d_to_tof_quadratic</code> | µs/Å² |
    | [TOF reciprocal](../physics/parameters.md#instrument-calib-d-to-tof-reciprocal) | <code>_edi_instrument.calib_d_to_tof_reciprocal</code> | µs·Å |
    | [2θ offset](../physics/parameters.md#instrument-calib-twotheta-offset) | <code>_pd_calib.2theta_offset</code> | deg |
    | [Wavelength](../physics/parameters.md#instrument-setup-wavelength) | <code>_diffrn_radiation_wavelength.value</code> | Å |
    | [Sample displacement](../physics/parameters.md#instrument-calib-sample-displacement) | <code>_edi_instrument.calib_sample_displacement</code> | deg |
    | [Sample transparency](../physics/parameters.md#instrument-calib-sample-transparency) | <code>_edi_instrument.calib_sample_transparency</code> | deg |
    | [Polarization coefficient](../physics/parameters.md#instrument-setup-polarization-coefficient) | <code>_edi_instrument.setup_polarization_coefficient</code> | — |
    | [Monochromator 2θ](../physics/parameters.md#instrument-setup-monochromator-twotheta) | <code>_edi_instrument.setup_monochromator_twotheta</code> | deg |
    | [Wavelength 2](../physics/parameters.md#instrument-setup-wavelength-2) | <code>_edi_instrument.setup_wavelength_2</code> | Å |
    | [Intensity ratio 2/1](../physics/parameters.md#instrument-setup-wavelength-2-to-1-ratio) | <code>_edi_instrument.setup_wavelength_2_to_1_ratio</code> | — |
    | [instrument](../physics/parameters.md#instrument-name) | <code>_diffrn_source.beamline</code> | — |
    | [facility](../physics/parameters.md#instrument-facility) | <code>_diffrn_source.facility</code> | — |
    | [2θ bank](../physics/parameters.md#instrument-setup-twotheta-bank) | <code>_pd_meas.2theta_fixed</code> | deg |

    **[<span class="ed-reference-icon" data-reference-category="peak" aria-hidden="true">&#63007;</span> Peak profile](../physics/parameters.md#peak)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [α₀](../physics/parameters.md#peak-rise-alpha-0) | <code>_edi_peak.rise_alpha_0</code> | — |
    | [α₁](../physics/parameters.md#peak-rise-alpha-1) | <code>_edi_peak.rise_alpha_1</code> | — |
    | [β₀](../physics/parameters.md#peak-decay-beta-0) | <code>_edi_peak.decay_beta_0</code> | — |
    | [β₁](../physics/parameters.md#peak-decay-beta-1) | <code>_edi_peak.decay_beta_1</code> | — |
    | [σ₀²](../physics/parameters.md#peak-broad-gauss-sigma-0) | <code>_edi_peak.broad_gauss_sigma_0</code> | µs² |
    | [σ₁²](../physics/parameters.md#peak-broad-gauss-sigma-1) | <code>_edi_peak.broad_gauss_sigma_1</code> | µs²/Å² |
    | [σ₂²](../physics/parameters.md#peak-broad-gauss-sigma-2) | <code>_edi_peak.broad_gauss_sigma_2</code> | µs²/Å⁴ |
    | [size G](../physics/parameters.md#peak-broad-gauss-size) | <code>_edi_peak.broad_gauss_size</code> | — |
    | [strain G](../physics/parameters.md#peak-broad-gauss-strain) | <code>_edi_peak.broad_gauss_strain</code> | — |
    | [γ₀](../physics/parameters.md#peak-broad-lorentz-gamma-0) | <code>_edi_peak.broad_lorentz_gamma_0</code> | µs |
    | [γ₁](../physics/parameters.md#peak-broad-lorentz-gamma-1) | <code>_edi_peak.broad_lorentz_gamma_1</code> | µs/Å |
    | [γ₂](../physics/parameters.md#peak-broad-lorentz-gamma-2) | <code>_edi_peak.broad_lorentz_gamma_2</code> | µs/Å² |
    | [size L](../physics/parameters.md#peak-broad-lorentz-size) | <code>_edi_peak.broad_lorentz_size</code> | — |
    | [strain L](../physics/parameters.md#peak-broad-lorentz-strain) | <code>_edi_peak.broad_lorentz_strain</code> | — |
    | [U](../physics/parameters.md#peak-broad-gauss-u) | <code>_edi_peak.broad_gauss_u</code> | deg² |
    | [V](../physics/parameters.md#peak-broad-gauss-v) | <code>_edi_peak.broad_gauss_v</code> | deg² |
    | [W](../physics/parameters.md#peak-broad-gauss-w) | <code>_edi_peak.broad_gauss_w</code> | deg² |
    | [X](../physics/parameters.md#peak-broad-lorentz-x) | <code>_edi_peak.broad_lorentz_x</code> | deg |
    | [Y](../physics/parameters.md#peak-broad-lorentz-y) | <code>_edi_peak.broad_lorentz_y</code> | deg |
    | [Eta0](../physics/parameters.md#peak-mixing-eta-0) | <code>_edi_peak.mixing_eta_0</code> | — |
    | [Eta1](../physics/parameters.md#peak-mixing-eta-1) | <code>_edi_peak.mixing_eta_1</code> | 1/deg |
    | [S/L](../physics/parameters.md#peak-asym-fcj-1) | <code>_edi_peak.asym_fcj_1</code> | — |
    | [D/L](../physics/parameters.md#peak-asym-fcj-2) | <code>_edi_peak.asym_fcj_2</code> | — |
    | [A₀](../physics/parameters.md#peak-asym-beba-a0) | <code>_edi_peak.asym_beba_a0</code> | — |
    | [B₀](../physics/parameters.md#peak-asym-beba-b0) | <code>_edi_peak.asym_beba_b0</code> | — |
    | [A₁](../physics/parameters.md#peak-asym-beba-a1) | <code>_edi_peak.asym_beba_a1</code> | — |
    | [B₁](../physics/parameters.md#peak-asym-beba-b1) | <code>_edi_peak.asym_beba_b1</code> | — |
    | [AsyLim](../physics/parameters.md#peak-asym-beba-limit) | <code>_edi_peak.asym_beba_limit</code> | deg |
    | [profile](../physics/parameters.md#peak-type) | <code>_edi_peak.type</code> | — |
    | [cutoff (FWHM)](../physics/parameters.md#peak-cutoff-fwhm) | <code>_edi_peak.cutoff_fwhm</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="excluded-region" aria-hidden="true">&#61741;</span> Excluded region](../physics/parameters.md#excluded-region)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#excluded-region-id) | <code>_edi_excluded_region.id</code> | — |
    | [start](../physics/parameters.md#excluded-region-start) | <code>_edi_excluded_region.start</code> | deg |
    | [end](../physics/parameters.md#excluded-region-end) | <code>_edi_excluded_region.end</code> | deg |

    **[<span class="ed-reference-icon" data-reference-category="extinction" aria-hidden="true">&#62373;</span> Extinction](../physics/parameters.md#extinction)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [Domain radius](../physics/parameters.md#extinction-domain-radius) | <code>_edi_extinction.domain_radius</code> | μm |
    | [Mosaic spread](../physics/parameters.md#extinction-mosaic-spread) | <code>_edi_extinction.mosaic_spread</code> | rad⁻¹ |
    | [Crystal radius](../physics/parameters.md#extinction-crystal-radius) | <code>_exptl_crystal.size_rad</code> | mm |
    | [Extinction coefficient](../physics/parameters.md#extinction-coefficient) | <code>_edi_extinction.coefficient</code> | — |
    | [x11](../physics/parameters.md#extinction-coefficient-11) | <code>_edi_extinction.coefficient_11</code> | — |
    | [x22](../physics/parameters.md#extinction-coefficient-22) | <code>_edi_extinction.coefficient_22</code> | — |
    | [x33](../physics/parameters.md#extinction-coefficient-33) | <code>_edi_extinction.coefficient_33</code> | — |
    | [x12](../physics/parameters.md#extinction-coefficient-12) | <code>_edi_extinction.coefficient_12</code> | — |
    | [x13](../physics/parameters.md#extinction-coefficient-13) | <code>_edi_extinction.coefficient_13</code> | — |
    | [x23](../physics/parameters.md#extinction-coefficient-23) | <code>_edi_extinction.coefficient_23</code> | — |
    | [type](../physics/parameters.md#extinction-type) | <code>_edi_extinction.type</code> | — |
    | [mosaic distribution](../physics/parameters.md#extinction-mosaic-distribution) | <code>_edi_extinction.mosaic_distribution</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="linked-structure" aria-hidden="true">&#62973;</span> Linked structure](../physics/parameters.md#linked-structure)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [scale](../physics/parameters.md#linked-structure-scale) | <code>_edi_linked_structure.scale</code> | — |
    | [structure](../physics/parameters.md#linked-structure-structure-id) | <code>_pd_phase_block.id</code> | — |
    | [enabled](../physics/parameters.md#linked-structure-enabled) | <code>_edi_linked_structure.enabled</code> | — |
    | [weight fraction](../physics/parameters.md#linked-structure-weight-fraction) | <code>_edi_linked_structure.weight_fraction</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="absorption" aria-hidden="true">&#61507;</span> Absorption](../physics/parameters.md#absorption)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [ABSCOR1](../physics/parameters.md#absorption-abscor1) | <code>_edi_absorption.abscor1</code> | Å⁻¹ |
    | [ABSCOR2](../physics/parameters.md#absorption-abscor2) | <code>_edi_absorption.abscor2</code> | — |
    | [μR](../physics/parameters.md#absorption-mu-r) | <code>_edi_absorption.mu_r</code> | — |
    | [type](../physics/parameters.md#absorption-type) | <code>_edi_absorption.type</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="preferred-orientation" aria-hidden="true">&#61774;</span> Preferred orientation](../physics/parameters.md#preferred-orientation)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [r](../physics/parameters.md#preferred-orientation-march-r) | <code>_pd_pref_orient_March_Dollase.r</code> | — |
    | [f rand](../physics/parameters.md#preferred-orientation-march-random-fract) | <code>_edi_preferred_orientation.march_random_fract</code> | — |
    | [structure](../physics/parameters.md#preferred-orientation-structure-id) | <code>_pd_pref_orient_March_Dollase.phase_id</code> | — |
    | [h](../physics/parameters.md#preferred-orientation-index-h) | <code>_pd_pref_orient_March_Dollase.index_h</code> | — |
    | [k](../physics/parameters.md#preferred-orientation-index-k) | <code>_pd_pref_orient_March_Dollase.index_k</code> | — |
    | [l](../physics/parameters.md#preferred-orientation-index-l) | <code>_pd_pref_orient_March_Dollase.index_l</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="reflns" aria-hidden="true">&#61616;</span> Observed reflections](../physics/parameters.md#reflns)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [observed above (su)](../physics/parameters.md#reflns-threshold-sigma) | <code>_edi_reflns.threshold_sigma</code> | — |
    | [on](../physics/parameters.md#reflns-threshold-basis) | <code>_edi_reflns.threshold_basis</code> | — |
    | [threshold](../physics/parameters.md#reflns-threshold-expression) | <code>_reflns.threshold_expression</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="scattering-source" aria-hidden="true">&#62930;</span> Scattering source](../physics/parameters.md#scattering-source)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [X-ray form factors](../physics/parameters.md#scattering-source-xray-form-factor) | <code>_edi_scattering_source.xray_form_factor</code> | — |
    | [X-ray dispersion](../physics/parameters.md#scattering-source-xray-dispersion) | <code>_edi_scattering_source.xray_dispersion</code> | — |
    | [neutron scattering lengths](../physics/parameters.md#scattering-source-neutron-scattering-length) | <code>_edi_scattering_source.neutron_scattering_length</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="data-source" aria-hidden="true">&#62831;</span> Data source](../physics/parameters.md#data-source)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [data file](../physics/parameters.md#data-source-file-name) | <code>_edi_data_source.file_name</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="data" aria-hidden="true">&#62263;</span> Measured data point](../physics/parameters.md#data)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [2θ](../physics/parameters.md#data-two-theta) | <code>_pd_meas.2theta_scan</code> | deg |
    | [TOF](../physics/parameters.md#data-time-of-flight) | <code>_pd_meas.time_of_flight</code> | µs |
    | [meas](../physics/parameters.md#data-intensity-meas) | <code>_pd_meas.intensity_total</code> | — |
    | [s.u.](../physics/parameters.md#data-intensity-meas-su) | <code>_pd_meas.intensity_total_su</code> | — |
    | [d](../physics/parameters.md#data-d-spacing) | <code>_pd_proc.d_spacing</code> | Å |
    | [calc](../physics/parameters.md#data-intensity-calc) | <code>_pd_calc.intensity_total</code> | — |
    | [bkg](../physics/parameters.md#data-intensity-bkg) | <code>_pd_calc.intensity_bkg</code> | — |
    | [status](../physics/parameters.md#data-calc-status) | <code>_edi_data.calc_status</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="data-calc" aria-hidden="true">&#61950;</span> Calculated point](../physics/parameters.md#data-calc)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [point](../physics/parameters.md#data-calc-point-id) | <code>_pd_data.point_id</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="pd-calc-overall" aria-hidden="true">&#61950;</span> Structure curves](../physics/parameters.md#pd-calc-overall)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [structure order](../physics/parameters.md#pd-calc-overall-component-presentation-order) | <code>_edi_pd_calc_overall.component_presentation_order</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="pd-calc" aria-hidden="true">&#61950;</span> Structure curve](../physics/parameters.md#pd-calc)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [structure calc](../physics/parameters.md#pd-calc-component-intensities-net) | <code>_pd_calc.component_intensities_net</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="refln" aria-hidden="true">&#61498;</span> Reflection](../physics/parameters.md#refln)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [structure](../physics/parameters.md#refln-structure-id) | <code>_pd_refln.phase_id</code> | — |
    | [d](../physics/parameters.md#refln-d-spacing) | <code>_refln.d_spacing</code> | Å |
    | [sin θ/λ](../physics/parameters.md#refln-sin-theta-over-lambda) | <code>_refln.sin_theta_over_lambda</code> | 1/Å |
    | [h](../physics/parameters.md#refln-index-h) | <code>_refln.index_h</code> | — |
    | [k](../physics/parameters.md#refln-index-k) | <code>_refln.index_k</code> | — |
    | [l](../physics/parameters.md#refln-index-l) | <code>_refln.index_l</code> | — |
    | [F calc](../physics/parameters.md#refln-f-calc) | <code>_refln.F_calc</code> | — |
    | [F meas](../physics/parameters.md#refln-f-meas) | <code>_refln.F_meas</code> | — |
    | [F² calc](../physics/parameters.md#refln-f-squared-calc) | <code>_refln.F_squared_calc</code> | — |
    | [F² meas](../physics/parameters.md#refln-intensity-meas) | <code>_refln.intensity_meas</code> | — |
    | [s.u.](../physics/parameters.md#refln-intensity-meas-su) | <code>_refln.intensity_meas_su</code> | — |
    | [F² calc](../physics/parameters.md#refln-intensity-calc) | <code>_refln.intensity_calc</code> | — |
    | [λ](../physics/parameters.md#refln-wavelength) | <code>_refln.wavelength</code> | Å |
    | [2θ](../physics/parameters.md#refln-two-theta) | <code>_edi_refln.two_theta</code> | deg |
    | [TOF](../physics/parameters.md#refln-time-of-flight) | <code>_edi_refln.time_of_flight</code> | µs |

## Project and analysis settings

=== "GUI"

    **[<span class="ed-reference-icon" data-reference-category="metadata" aria-hidden="true">&#61831;</span> Project](../physics/parameters.md#metadata)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [name](../physics/parameters.md#metadata-name) | name | — |
    | [title](../physics/parameters.md#metadata-title) | title | — |
    | [description](../physics/parameters.md#metadata-description) | description | — |
    | [authors](../physics/parameters.md#metadata-authors) | authors | — |
    | [location](../physics/parameters.md#metadata-path) | location | — |
    | [created](../physics/parameters.md#metadata-created) | created | — |
    | [last modified](../physics/parameters.md#metadata-last-modified) | last modified | — |
    | [timestamp](../physics/parameters.md#metadata-timestamp) | timestamp | — |

    **[<span class="ed-reference-icon" data-reference-category="su-format" aria-hidden="true">&#62030;</span> Standard uncertainties](../physics/parameters.md#su-format)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [rule](../physics/parameters.md#su-format-rule) | rule | — |

    **[<span class="ed-reference-icon" data-reference-category="report" aria-hidden="true">&#61788;</span> Report](../physics/parameters.md#report)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [HTML](../physics/parameters.md#report-html) | HTML | — |
    | [PDF](../physics/parameters.md#report-pdf) | PDF | — |
    | [CIF](../physics/parameters.md#report-cif) | CIF | — |
    | [embed chart libraries](../physics/parameters.md#report-html-offline) | embed chart libraries | — |
    | [excluded](../physics/parameters.md#report-excluded) | excluded | — |

    **[<span class="ed-reference-icon" data-reference-category="correlation-chart" aria-hidden="true">&#61450;</span> Correlation chart](../physics/parameters.md#correlation-chart)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [threshold](../physics/parameters.md#correlation-chart-threshold) | threshold | — |

    **[<span class="ed-reference-icon" data-reference-category="pattern-chart" aria-hidden="true">&#61953;</span> Pattern chart](../physics/parameters.md#pattern-chart)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [x-axis](../physics/parameters.md#pattern-chart-x-axis) | x-axis | — |

    **[<span class="ed-reference-icon" data-reference-category="calculator" aria-hidden="true">&#61932;</span> Calculator](../physics/parameters.md#calculator)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [calculator](../physics/parameters.md#calculator-type) | calculator | — |

    **[<span class="ed-reference-icon" data-reference-category="minimizer" aria-hidden="true">&#62398;</span> Minimizer](../physics/parameters.md#minimizer)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [minimizer](../physics/parameters.md#minimizer-type) | minimizer | — |
    | [max iterations](../physics/parameters.md#minimizer-max-iterations) | max iterations | — |
    | [descent](../physics/parameters.md#minimizer-descent) | descent | — |
    | [tolerance](../physics/parameters.md#minimizer-chi-square-tolerance) | tolerance | — |

    **[<span class="ed-reference-icon" data-reference-category="fitting-mode" aria-hidden="true">&#61918;</span> Fitting mode](../physics/parameters.md#fitting-mode)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [mode](../physics/parameters.md#fitting-mode-type) | mode | — |

    **[<span class="ed-reference-icon" data-reference-category="refine-ls" aria-hidden="true">&#61636;</span> Fitted reflections](../physics/parameters.md#refine-ls)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [fit reflections above (su)](../physics/parameters.md#refine-ls-threshold-sigma) | fit reflections above (su) | — |

    **[<span class="ed-reference-icon" data-reference-category="alias" aria-hidden="true">&#61483;</span> Alias](../physics/parameters.md#alias)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [alias](../physics/parameters.md#alias-id) | alias | — |
    | [parameter](../physics/parameters.md#alias-parameter-unique-name) | parameter | — |

    **[<span class="ed-reference-icon" data-reference-category="constraint" aria-hidden="true">&#62764;</span> Constraint](../physics/parameters.md#constraint)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#constraint-id) | id | — |
    | [expression](../physics/parameters.md#constraint-expression) | expression | — |
    | [enabled](../physics/parameters.md#constraint-enabled) | enabled | — |

    **[<span class="ed-reference-icon" data-reference-category="joint-fit" aria-hidden="true">&#61633;</span> Joint-fit weights](../physics/parameters.md#joint-fit)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [weight](../physics/parameters.md#joint-fit-weight) | weight | — |

    **[<span class="ed-reference-icon" data-reference-category="sequential-fit" aria-hidden="true">&#61643;</span> Sequential fit](../physics/parameters.md#sequential-fit)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [data directory](../physics/parameters.md#sequential-fit-data-dir) | data directory | — |
    | [files](../physics/parameters.md#sequential-fit-file-pattern) | files | — |
    | [reverse](../physics/parameters.md#sequential-fit-reverse) | reverse | — |
    | [template](../physics/parameters.md#sequential-fit-template-file) | template | — |

    **[<span class="ed-reference-icon" data-reference-category="sequential-fit-extract" aria-hidden="true">&#61616;</span> Scan extraction rule](../physics/parameters.md#sequential-fit-extract)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#sequential-fit-extract-id) | id | — |
    | [target](../physics/parameters.md#sequential-fit-extract-target) | target | — |
    | [pattern](../physics/parameters.md#sequential-fit-extract-pattern) | pattern | — |
    | [required](../physics/parameters.md#sequential-fit-extract-required) | required | — |

    **[<span class="ed-reference-icon" data-reference-category="edi" aria-hidden="true">&#61897;</span> File header](../physics/parameters.md#edi)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [schema version](../physics/parameters.md#edi-schema-version) | schema version | — |

    **[<span class="ed-reference-icon" data-reference-category="report-file" aria-hidden="true">&#61787;</span> Saved report](../physics/parameters.md#report-file)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [format](../physics/parameters.md#report-file-format) | format | — |
    | [file](../physics/parameters.md#report-file-name) | file | — |
    | [saved](../physics/parameters.md#report-file-saved) | saved | — |
    | [project saved](../physics/parameters.md#report-file-project-last-modified) | project saved | — |
    | [digest](../physics/parameters.md#report-file-digest) | digest | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-parameter" aria-hidden="true">&#61914;</span> Fit start value](../physics/parameters.md#fit-parameter)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [parameter](../physics/parameters.md#fit-parameter-id) | parameter | — |
    | [start value](../physics/parameters.md#fit-parameter-start-value) | start value | — |
    | [start error](../physics/parameters.md#fit-parameter-start-uncertainty) | start error | — |
    | [start tied](../physics/parameters.md#fit-parameter-start-tied) | start tied | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-result" aria-hidden="true">&#61528;</span> Fit result](../physics/parameters.md#fit-result)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [kind](../physics/parameters.md#fit-result-result-kind) | kind | — |
    | [success](../physics/parameters.md#fit-result-success) | success | — |
    | [message](../physics/parameters.md#fit-result-message) | message | — |
    | [iterations](../physics/parameters.md#fit-result-iterations) | iterations | — |
    | [time](../physics/parameters.md#fit-result-fitting-time) | time | s |
    | [reduced χ²](../physics/parameters.md#fit-result-reduced-chi-square) | reduced χ² | — |
    | [objective](../physics/parameters.md#fit-result-objective-name) | objective | — |
    | [objective value](../physics/parameters.md#fit-result-objective-value) | objective value | — |
    | [points](../physics/parameters.md#fit-result-n-data-points) | points | — |
    | [parameters](../physics/parameters.md#fit-result-n-parameters) | parameters | — |
    | [free parameters](../physics/parameters.md#fit-result-n-free-parameters) | free parameters | — |
    | [degrees of freedom](../physics/parameters.md#fit-result-degrees-of-freedom) | degrees of freedom | — |
    | [covariance](../physics/parameters.md#fit-result-covariance-available) | covariance | — |
    | [exit reason](../physics/parameters.md#fit-result-exit-reason) | exit reason | — |
    | [Rwp](../physics/parameters.md#fit-result-prof-wr-factor) | Rwp | % |
    | [Rp](../physics/parameters.md#fit-result-prof-r-factor) | Rp | % |
    | [Rexp](../physics/parameters.md#fit-result-prof-wr-expected) | Rexp | % |
    | [cRp](../physics/parameters.md#fit-result-prof-cr-factor) | cRp | % |
    | [cRwp](../physics/parameters.md#fit-result-prof-cwr-factor) | cRwp | % |
    | [profile](../physics/parameters.md#fit-result-profile-function) | profile | — |
    | [background](../physics/parameters.md#fit-result-background-function) | background | — |
    | [descent](../physics/parameters.md#fit-result-descent) | descent | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-result-bank" aria-hidden="true">&#61452;</span> Experiment fit result](../physics/parameters.md#fit-result-bank)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [points](../physics/parameters.md#fit-result-bank-n-data-points) | points | — |
    | [Rp](../physics/parameters.md#fit-result-bank-prof-r-factor) | Rp | % |
    | [Rwp](../physics/parameters.md#fit-result-bank-prof-wr-factor) | Rwp | % |
    | [Rexp](../physics/parameters.md#fit-result-bank-prof-wr-expected) | Rexp | % |
    | [cRp](../physics/parameters.md#fit-result-bank-prof-cr-factor) | cRp | % |
    | [cRwp](../physics/parameters.md#fit-result-bank-prof-cwr-factor) | cRwp | % |
    | [reduced χ²](../physics/parameters.md#fit-result-bank-chi-square) | reduced χ² | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-result-phase" aria-hidden="true">&#61452;</span> Structure fit result](../physics/parameters.md#fit-result-phase)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [R Bragg](../physics/parameters.md#fit-result-phase-bragg-r-factor) | R Bragg | % |
    | [R F](../physics/parameters.md#fit-result-phase-f-r-factor) | R F | % |

    **[<span class="ed-reference-icon" data-reference-category="fit-parameter-correlation" aria-hidden="true">&#61449;</span> Correlation](../physics/parameters.md#fit-parameter-correlation)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#fit-parameter-correlation-id) | id | — |
    | [source](../physics/parameters.md#fit-parameter-correlation-source-kind) | source | — |
    | [parameter 1](../physics/parameters.md#fit-parameter-correlation-parameter-unique-name-i) | parameter 1 | — |
    | [parameter 2](../physics/parameters.md#fit-parameter-correlation-parameter-unique-name-j) | parameter 2 | — |
    | [correlation](../physics/parameters.md#fit-parameter-correlation-correlation) | correlation | — |
    | [file](../physics/parameters.md#fit-parameter-correlation-file-path) | file | — |

    **[<span class="ed-reference-icon" data-reference-category="pd-block" aria-hidden="true">&#61897;</span> Report block](../physics/parameters.md#pd-block)**

    | Parameter or field | GUI name | Units |
    | --- | --- | --- |
    | [block](../physics/parameters.md#pd-block-id) | block | — |

=== "Edi"

    **[<span class="ed-reference-icon" data-reference-category="metadata" aria-hidden="true">&#61831;</span> Project](../physics/parameters.md#metadata)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [name](../physics/parameters.md#metadata-name) | <code>_metadata.name</code> | — |
    | [title](../physics/parameters.md#metadata-title) | <code>_metadata.title</code> | — |
    | [description](../physics/parameters.md#metadata-description) | <code>_metadata.description</code> | — |
    | [authors](../physics/parameters.md#metadata-authors) | <code>_metadata.authors</code> | — |
    | [location](../physics/parameters.md#metadata-path) | <code>_metadata.path</code> | — |
    | [created](../physics/parameters.md#metadata-created) | <code>_metadata.created</code> | — |
    | [last modified](../physics/parameters.md#metadata-last-modified) | <code>_metadata.last_modified</code> | — |
    | [timestamp](../physics/parameters.md#metadata-timestamp) | <code>_metadata.timestamp</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="su-format" aria-hidden="true">&#62030;</span> Standard uncertainties](../physics/parameters.md#su-format)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [rule](../physics/parameters.md#su-format-rule) | <code>_su_format.rule</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="report" aria-hidden="true">&#61788;</span> Report](../physics/parameters.md#report)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [HTML](../physics/parameters.md#report-html) | <code>_report.html</code> | — |
    | [PDF](../physics/parameters.md#report-pdf) | <code>_report.pdf</code> | — |
    | [CIF](../physics/parameters.md#report-cif) | <code>_report.cif</code> | — |
    | [embed chart libraries](../physics/parameters.md#report-html-offline) | <code>_report.html_offline</code> | — |
    | [excluded](../physics/parameters.md#report-excluded) | <code>_report.excluded</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="correlation-chart" aria-hidden="true">&#61450;</span> Correlation chart](../physics/parameters.md#correlation-chart)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [threshold](../physics/parameters.md#correlation-chart-threshold) | <code>_correlation_chart.threshold</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="pattern-chart" aria-hidden="true">&#61953;</span> Pattern chart](../physics/parameters.md#pattern-chart)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [x-axis](../physics/parameters.md#pattern-chart-x-axis) | <code>_pattern_chart.x_axis</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="calculator" aria-hidden="true">&#61932;</span> Calculator](../physics/parameters.md#calculator)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [calculator](../physics/parameters.md#calculator-type) | <code>_calculator.type</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="minimizer" aria-hidden="true">&#62398;</span> Minimizer](../physics/parameters.md#minimizer)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [minimizer](../physics/parameters.md#minimizer-type) | <code>_minimizer.type</code> | — |
    | [max iterations](../physics/parameters.md#minimizer-max-iterations) | <code>_minimizer.max_iterations</code> | — |
    | [descent](../physics/parameters.md#minimizer-descent) | <code>_minimizer.descent</code> | — |
    | [tolerance](../physics/parameters.md#minimizer-chi-square-tolerance) | <code>_minimizer.chi_square_tolerance</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="fitting-mode" aria-hidden="true">&#61918;</span> Fitting mode](../physics/parameters.md#fitting-mode)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [mode](../physics/parameters.md#fitting-mode-type) | <code>_fitting_mode.type</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="refine-ls" aria-hidden="true">&#61636;</span> Fitted reflections](../physics/parameters.md#refine-ls)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [fit reflections above (su)](../physics/parameters.md#refine-ls-threshold-sigma) | <code>_refine_ls.threshold_sigma</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="alias" aria-hidden="true">&#61483;</span> Alias](../physics/parameters.md#alias)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [alias](../physics/parameters.md#alias-id) | <code>_alias.id</code> | — |
    | [parameter](../physics/parameters.md#alias-parameter-unique-name) | <code>_alias.parameter_unique_name</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="constraint" aria-hidden="true">&#62764;</span> Constraint](../physics/parameters.md#constraint)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#constraint-id) | <code>_constraint.id</code> | — |
    | [expression](../physics/parameters.md#constraint-expression) | <code>_constraint.expression</code> | — |
    | [enabled](../physics/parameters.md#constraint-enabled) | <code>_constraint.enabled</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="joint-fit" aria-hidden="true">&#61633;</span> Joint-fit weights](../physics/parameters.md#joint-fit)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [weight](../physics/parameters.md#joint-fit-weight) | <code>_joint_fit.weight</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="sequential-fit" aria-hidden="true">&#61643;</span> Sequential fit](../physics/parameters.md#sequential-fit)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [data directory](../physics/parameters.md#sequential-fit-data-dir) | <code>_sequential_fit.data_dir</code> | — |
    | [files](../physics/parameters.md#sequential-fit-file-pattern) | <code>_sequential_fit.file_pattern</code> | — |
    | [reverse](../physics/parameters.md#sequential-fit-reverse) | <code>_sequential_fit.reverse</code> | — |
    | [template](../physics/parameters.md#sequential-fit-template-file) | <code>_sequential_fit.template_file</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="sequential-fit-extract" aria-hidden="true">&#61616;</span> Scan extraction rule](../physics/parameters.md#sequential-fit-extract)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#sequential-fit-extract-id) | <code>_sequential_fit_extract.id</code> | — |
    | [target](../physics/parameters.md#sequential-fit-extract-target) | <code>_sequential_fit_extract.target</code> | — |
    | [pattern](../physics/parameters.md#sequential-fit-extract-pattern) | <code>_sequential_fit_extract.pattern</code> | — |
    | [required](../physics/parameters.md#sequential-fit-extract-required) | <code>_sequential_fit_extract.required</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="edi" aria-hidden="true">&#61897;</span> File header](../physics/parameters.md#edi)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [schema version](../physics/parameters.md#edi-schema-version) | <code>_edi.schema_version</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="report-file" aria-hidden="true">&#61787;</span> Saved report](../physics/parameters.md#report-file)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [format](../physics/parameters.md#report-file-format) | <code>_report_file.format</code> | — |
    | [file](../physics/parameters.md#report-file-name) | <code>_report_file.name</code> | — |
    | [saved](../physics/parameters.md#report-file-saved) | <code>_report_file.saved</code> | — |
    | [project saved](../physics/parameters.md#report-file-project-last-modified) | <code>_report_file.project_last_modified</code> | — |
    | [digest](../physics/parameters.md#report-file-digest) | <code>_report_file.digest</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-parameter" aria-hidden="true">&#61914;</span> Fit start value](../physics/parameters.md#fit-parameter)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [parameter](../physics/parameters.md#fit-parameter-id) | <code>_fit_parameter.id</code> | — |
    | [start value](../physics/parameters.md#fit-parameter-start-value) | <code>_fit_parameter.start_value</code> | — |
    | [start error](../physics/parameters.md#fit-parameter-start-uncertainty) | <code>_fit_parameter.start_uncertainty</code> | — |
    | [start tied](../physics/parameters.md#fit-parameter-start-tied) | <code>_fit_parameter.start_tied</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-result" aria-hidden="true">&#61528;</span> Fit result](../physics/parameters.md#fit-result)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [kind](../physics/parameters.md#fit-result-result-kind) | <code>_fit_result.result_kind</code> | — |
    | [success](../physics/parameters.md#fit-result-success) | <code>_fit_result.success</code> | — |
    | [message](../physics/parameters.md#fit-result-message) | <code>_fit_result.message</code> | — |
    | [iterations](../physics/parameters.md#fit-result-iterations) | <code>_fit_result.iterations</code> | — |
    | [time](../physics/parameters.md#fit-result-fitting-time) | <code>_fit_result.fitting_time</code> | s |
    | [reduced χ²](../physics/parameters.md#fit-result-reduced-chi-square) | <code>_fit_result.reduced_chi_square</code> | — |
    | [objective](../physics/parameters.md#fit-result-objective-name) | <code>_fit_result.objective_name</code> | — |
    | [objective value](../physics/parameters.md#fit-result-objective-value) | <code>_fit_result.objective_value</code> | — |
    | [points](../physics/parameters.md#fit-result-n-data-points) | <code>_fit_result.n_data_points</code> | — |
    | [parameters](../physics/parameters.md#fit-result-n-parameters) | <code>_fit_result.n_parameters</code> | — |
    | [free parameters](../physics/parameters.md#fit-result-n-free-parameters) | <code>_fit_result.n_free_parameters</code> | — |
    | [degrees of freedom](../physics/parameters.md#fit-result-degrees-of-freedom) | <code>_fit_result.degrees_of_freedom</code> | — |
    | [covariance](../physics/parameters.md#fit-result-covariance-available) | <code>_fit_result.covariance_available</code> | — |
    | [exit reason](../physics/parameters.md#fit-result-exit-reason) | <code>_fit_result.exit_reason</code> | — |
    | [Rwp](../physics/parameters.md#fit-result-prof-wr-factor) | <code>_fit_result.prof_wr_factor</code> | % |
    | [Rp](../physics/parameters.md#fit-result-prof-r-factor) | <code>_fit_result.prof_r_factor</code> | % |
    | [Rexp](../physics/parameters.md#fit-result-prof-wr-expected) | <code>_fit_result.prof_wr_expected</code> | % |
    | [cRp](../physics/parameters.md#fit-result-prof-cr-factor) | <code>_fit_result.prof_cr_factor</code> | % |
    | [cRwp](../physics/parameters.md#fit-result-prof-cwr-factor) | <code>_fit_result.prof_cwr_factor</code> | % |
    | [profile](../physics/parameters.md#fit-result-profile-function) | <code>_fit_result.profile_function</code> | — |
    | [background](../physics/parameters.md#fit-result-background-function) | <code>_fit_result.background_function</code> | — |
    | [descent](../physics/parameters.md#fit-result-descent) | <code>_fit_result.descent</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-result-bank" aria-hidden="true">&#61452;</span> Experiment fit result](../physics/parameters.md#fit-result-bank)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [points](../physics/parameters.md#fit-result-bank-n-data-points) | <code>_fit_result_bank.n_data_points</code> | — |
    | [Rp](../physics/parameters.md#fit-result-bank-prof-r-factor) | <code>_fit_result_bank.prof_r_factor</code> | % |
    | [Rwp](../physics/parameters.md#fit-result-bank-prof-wr-factor) | <code>_fit_result_bank.prof_wr_factor</code> | % |
    | [Rexp](../physics/parameters.md#fit-result-bank-prof-wr-expected) | <code>_fit_result_bank.prof_wr_expected</code> | % |
    | [cRp](../physics/parameters.md#fit-result-bank-prof-cr-factor) | <code>_fit_result_bank.prof_cr_factor</code> | % |
    | [cRwp](../physics/parameters.md#fit-result-bank-prof-cwr-factor) | <code>_fit_result_bank.prof_cwr_factor</code> | % |
    | [reduced χ²](../physics/parameters.md#fit-result-bank-chi-square) | <code>_fit_result_bank.chi_square</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-result-phase" aria-hidden="true">&#61452;</span> Structure fit result](../physics/parameters.md#fit-result-phase)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [R Bragg](../physics/parameters.md#fit-result-phase-bragg-r-factor) | <code>_fit_result_phase.bragg_r_factor</code> | % |
    | [R F](../physics/parameters.md#fit-result-phase-f-r-factor) | <code>_fit_result_phase.f_r_factor</code> | % |

    **[<span class="ed-reference-icon" data-reference-category="fit-parameter-correlation" aria-hidden="true">&#61449;</span> Correlation](../physics/parameters.md#fit-parameter-correlation)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#fit-parameter-correlation-id) | <code>_fit_parameter_correlation.id</code> | — |
    | [source](../physics/parameters.md#fit-parameter-correlation-source-kind) | <code>_fit_parameter_correlation.source_kind</code> | — |
    | [parameter 1](../physics/parameters.md#fit-parameter-correlation-parameter-unique-name-i) | <code>_fit_parameter_correlation.parameter_unique_name_i</code> | — |
    | [parameter 2](../physics/parameters.md#fit-parameter-correlation-parameter-unique-name-j) | <code>_fit_parameter_correlation.parameter_unique_name_j</code> | — |
    | [correlation](../physics/parameters.md#fit-parameter-correlation-correlation) | <code>_fit_parameter_correlation.correlation</code> | — |
    | [file](../physics/parameters.md#fit-parameter-correlation-file-path) | <code>_fit_parameter_correlation.file_path</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="pd-block" aria-hidden="true">&#61897;</span> Report block](../physics/parameters.md#pd-block)**

    | Parameter or field | Edi name | Units |
    | --- | --- | --- |
    | [block](../physics/parameters.md#pd-block-id) | <code>_pd_block.id</code> | — |

=== "Python"

    **[<span class="ed-reference-icon" data-reference-category="metadata" aria-hidden="true">&#61831;</span> Project](../physics/parameters.md#metadata)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [name](../physics/parameters.md#metadata-name) | <code>project.metadata.name</code> | — |
    | [title](../physics/parameters.md#metadata-title) | <code>project.metadata.title</code> | — |
    | [description](../physics/parameters.md#metadata-description) | <code>project.metadata.description</code> | — |
    | [authors](../physics/parameters.md#metadata-authors) | <code>project.metadata.authors</code> | — |
    | [location](../physics/parameters.md#metadata-path) | <code>project.metadata.path</code> | — |
    | [created](../physics/parameters.md#metadata-created) | <code>project.metadata.created</code> | — |
    | [last modified](../physics/parameters.md#metadata-last-modified) | <code>project.metadata.last_modified</code> | — |
    | [timestamp](../physics/parameters.md#metadata-timestamp) | <code>project.metadata.timestamp</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="su-format" aria-hidden="true">&#62030;</span> Standard uncertainties](../physics/parameters.md#su-format)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [rule](../physics/parameters.md#su-format-rule) | <code>project.su_rule</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="report" aria-hidden="true">&#61788;</span> Report](../physics/parameters.md#report)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [HTML](../physics/parameters.md#report-html) | — | — |
    | [PDF](../physics/parameters.md#report-pdf) | — | — |
    | [CIF](../physics/parameters.md#report-cif) | — | — |
    | [embed chart libraries](../physics/parameters.md#report-html-offline) | — | — |
    | [excluded](../physics/parameters.md#report-excluded) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="correlation-chart" aria-hidden="true">&#61450;</span> Correlation chart](../physics/parameters.md#correlation-chart)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [threshold](../physics/parameters.md#correlation-chart-threshold) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="pattern-chart" aria-hidden="true">&#61953;</span> Pattern chart](../physics/parameters.md#pattern-chart)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [x-axis](../physics/parameters.md#pattern-chart-x-axis) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="calculator" aria-hidden="true">&#61932;</span> Calculator](../physics/parameters.md#calculator)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [calculator](../physics/parameters.md#calculator-type) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="minimizer" aria-hidden="true">&#62398;</span> Minimizer](../physics/parameters.md#minimizer)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [minimizer](../physics/parameters.md#minimizer-type) | — | — |
    | [max iterations](../physics/parameters.md#minimizer-max-iterations) | — | — |
    | [descent](../physics/parameters.md#minimizer-descent) | <code>project.descent</code> | — |
    | [tolerance](../physics/parameters.md#minimizer-chi-square-tolerance) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="fitting-mode" aria-hidden="true">&#61918;</span> Fitting mode](../physics/parameters.md#fitting-mode)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [mode](../physics/parameters.md#fitting-mode-type) | <code>project.fitting_mode</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="refine-ls" aria-hidden="true">&#61636;</span> Fitted reflections](../physics/parameters.md#refine-ls)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [fit reflections above (su)](../physics/parameters.md#refine-ls-threshold-sigma) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="alias" aria-hidden="true">&#61483;</span> Alias](../physics/parameters.md#alias)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [alias](../physics/parameters.md#alias-id) | — | — |
    | [parameter](../physics/parameters.md#alias-parameter-unique-name) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="constraint" aria-hidden="true">&#62764;</span> Constraint](../physics/parameters.md#constraint)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#constraint-id) | — | — |
    | [expression](../physics/parameters.md#constraint-expression) | — | — |
    | [enabled](../physics/parameters.md#constraint-enabled) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="joint-fit" aria-hidden="true">&#61633;</span> Joint-fit weights](../physics/parameters.md#joint-fit)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [weight](../physics/parameters.md#joint-fit-weight) | <code>project.experiments[0].dataset_weight</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="sequential-fit" aria-hidden="true">&#61643;</span> Sequential fit](../physics/parameters.md#sequential-fit)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [data directory](../physics/parameters.md#sequential-fit-data-dir) | — | — |
    | [files](../physics/parameters.md#sequential-fit-file-pattern) | — | — |
    | [reverse](../physics/parameters.md#sequential-fit-reverse) | — | — |
    | [template](../physics/parameters.md#sequential-fit-template-file) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="sequential-fit-extract" aria-hidden="true">&#61616;</span> Scan extraction rule](../physics/parameters.md#sequential-fit-extract)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#sequential-fit-extract-id) | — | — |
    | [target](../physics/parameters.md#sequential-fit-extract-target) | — | — |
    | [pattern](../physics/parameters.md#sequential-fit-extract-pattern) | — | — |
    | [required](../physics/parameters.md#sequential-fit-extract-required) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="edi" aria-hidden="true">&#61897;</span> File header](../physics/parameters.md#edi)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [schema version](../physics/parameters.md#edi-schema-version) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="report-file" aria-hidden="true">&#61787;</span> Saved report](../physics/parameters.md#report-file)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [format](../physics/parameters.md#report-file-format) | — | — |
    | [file](../physics/parameters.md#report-file-name) | — | — |
    | [saved](../physics/parameters.md#report-file-saved) | — | — |
    | [project saved](../physics/parameters.md#report-file-project-last-modified) | — | — |
    | [digest](../physics/parameters.md#report-file-digest) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-parameter" aria-hidden="true">&#61914;</span> Fit start value](../physics/parameters.md#fit-parameter)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [parameter](../physics/parameters.md#fit-parameter-id) | — | — |
    | [start value](../physics/parameters.md#fit-parameter-start-value) | — | — |
    | [start error](../physics/parameters.md#fit-parameter-start-uncertainty) | — | — |
    | [start tied](../physics/parameters.md#fit-parameter-start-tied) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-result" aria-hidden="true">&#61528;</span> Fit result](../physics/parameters.md#fit-result)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [kind](../physics/parameters.md#fit-result-result-kind) | — | — |
    | [success](../physics/parameters.md#fit-result-success) | — | — |
    | [message](../physics/parameters.md#fit-result-message) | — | — |
    | [iterations](../physics/parameters.md#fit-result-iterations) | — | — |
    | [time](../physics/parameters.md#fit-result-fitting-time) | — | s |
    | [reduced χ²](../physics/parameters.md#fit-result-reduced-chi-square) | — | — |
    | [objective](../physics/parameters.md#fit-result-objective-name) | — | — |
    | [objective value](../physics/parameters.md#fit-result-objective-value) | — | — |
    | [points](../physics/parameters.md#fit-result-n-data-points) | — | — |
    | [parameters](../physics/parameters.md#fit-result-n-parameters) | — | — |
    | [free parameters](../physics/parameters.md#fit-result-n-free-parameters) | — | — |
    | [degrees of freedom](../physics/parameters.md#fit-result-degrees-of-freedom) | — | — |
    | [covariance](../physics/parameters.md#fit-result-covariance-available) | — | — |
    | [exit reason](../physics/parameters.md#fit-result-exit-reason) | — | — |
    | [Rwp](../physics/parameters.md#fit-result-prof-wr-factor) | — | % |
    | [Rp](../physics/parameters.md#fit-result-prof-r-factor) | — | % |
    | [Rexp](../physics/parameters.md#fit-result-prof-wr-expected) | — | % |
    | [cRp](../physics/parameters.md#fit-result-prof-cr-factor) | — | % |
    | [cRwp](../physics/parameters.md#fit-result-prof-cwr-factor) | — | % |
    | [profile](../physics/parameters.md#fit-result-profile-function) | — | — |
    | [background](../physics/parameters.md#fit-result-background-function) | — | — |
    | [descent](../physics/parameters.md#fit-result-descent) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-result-bank" aria-hidden="true">&#61452;</span> Experiment fit result](../physics/parameters.md#fit-result-bank)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [points](../physics/parameters.md#fit-result-bank-n-data-points) | — | — |
    | [Rp](../physics/parameters.md#fit-result-bank-prof-r-factor) | — | % |
    | [Rwp](../physics/parameters.md#fit-result-bank-prof-wr-factor) | — | % |
    | [Rexp](../physics/parameters.md#fit-result-bank-prof-wr-expected) | — | % |
    | [cRp](../physics/parameters.md#fit-result-bank-prof-cr-factor) | — | % |
    | [cRwp](../physics/parameters.md#fit-result-bank-prof-cwr-factor) | — | % |
    | [reduced χ²](../physics/parameters.md#fit-result-bank-chi-square) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-result-phase" aria-hidden="true">&#61452;</span> Structure fit result](../physics/parameters.md#fit-result-phase)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [R Bragg](../physics/parameters.md#fit-result-phase-bragg-r-factor) | — | % |
    | [R F](../physics/parameters.md#fit-result-phase-f-r-factor) | — | % |

    **[<span class="ed-reference-icon" data-reference-category="fit-parameter-correlation" aria-hidden="true">&#61449;</span> Correlation](../physics/parameters.md#fit-parameter-correlation)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#fit-parameter-correlation-id) | — | — |
    | [source](../physics/parameters.md#fit-parameter-correlation-source-kind) | — | — |
    | [parameter 1](../physics/parameters.md#fit-parameter-correlation-parameter-unique-name-i) | — | — |
    | [parameter 2](../physics/parameters.md#fit-parameter-correlation-parameter-unique-name-j) | — | — |
    | [correlation](../physics/parameters.md#fit-parameter-correlation-correlation) | — | — |
    | [file](../physics/parameters.md#fit-parameter-correlation-file-path) | — | — |

    **[<span class="ed-reference-icon" data-reference-category="pd-block" aria-hidden="true">&#61897;</span> Report block](../physics/parameters.md#pd-block)**

    | Parameter or field | Python name | Units |
    | --- | --- | --- |
    | [block](../physics/parameters.md#pd-block-id) | — | — |

=== "CIF"

    **[<span class="ed-reference-icon" data-reference-category="metadata" aria-hidden="true">&#61831;</span> Project](../physics/parameters.md#metadata)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [name](../physics/parameters.md#metadata-name) | <code>_edi_metadata.name</code> | — |
    | [title](../physics/parameters.md#metadata-title) | <code>_edi_metadata.title</code> | — |
    | [description](../physics/parameters.md#metadata-description) | <code>_edi_metadata.description</code> | — |
    | [authors](../physics/parameters.md#metadata-authors) | <code>_edi_metadata.authors</code> | — |
    | [location](../physics/parameters.md#metadata-path) | <code>_edi_metadata.path</code> | — |
    | [created](../physics/parameters.md#metadata-created) | <code>_edi_metadata.created</code> | — |
    | [last modified](../physics/parameters.md#metadata-last-modified) | <code>_edi_metadata.last_modified</code> | — |
    | [timestamp](../physics/parameters.md#metadata-timestamp) | <code>_edi_metadata.timestamp</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="su-format" aria-hidden="true">&#62030;</span> Standard uncertainties](../physics/parameters.md#su-format)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [rule](../physics/parameters.md#su-format-rule) | <code>_edi_su_format.rule</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="report" aria-hidden="true">&#61788;</span> Report](../physics/parameters.md#report)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [HTML](../physics/parameters.md#report-html) | <code>_edi_report.html</code> | — |
    | [PDF](../physics/parameters.md#report-pdf) | <code>_edi_report.pdf</code> | — |
    | [CIF](../physics/parameters.md#report-cif) | <code>_edi_report.cif</code> | — |
    | [embed chart libraries](../physics/parameters.md#report-html-offline) | <code>_edi_report.html_offline</code> | — |
    | [excluded](../physics/parameters.md#report-excluded) | <code>_edi_report.excluded</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="correlation-chart" aria-hidden="true">&#61450;</span> Correlation chart](../physics/parameters.md#correlation-chart)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [threshold](../physics/parameters.md#correlation-chart-threshold) | <code>_edi_correlation_chart.threshold</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="pattern-chart" aria-hidden="true">&#61953;</span> Pattern chart](../physics/parameters.md#pattern-chart)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [x-axis](../physics/parameters.md#pattern-chart-x-axis) | <code>_edi_pattern_chart.x_axis</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="calculator" aria-hidden="true">&#61932;</span> Calculator](../physics/parameters.md#calculator)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [calculator](../physics/parameters.md#calculator-type) | <code>_edi_calculator.type</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="minimizer" aria-hidden="true">&#62398;</span> Minimizer](../physics/parameters.md#minimizer)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [minimizer](../physics/parameters.md#minimizer-type) | <code>_edi_minimizer.type</code> | — |
    | [max iterations](../physics/parameters.md#minimizer-max-iterations) | <code>_edi_minimizer.max_iterations</code> | — |
    | [descent](../physics/parameters.md#minimizer-descent) | <code>_edi_minimizer.descent</code> | — |
    | [tolerance](../physics/parameters.md#minimizer-chi-square-tolerance) | <code>_edi_minimizer.chi_square_tolerance</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="fitting-mode" aria-hidden="true">&#61918;</span> Fitting mode](../physics/parameters.md#fitting-mode)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [mode](../physics/parameters.md#fitting-mode-type) | <code>_edi_fitting_mode.type</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="refine-ls" aria-hidden="true">&#61636;</span> Fitted reflections](../physics/parameters.md#refine-ls)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [fit reflections above (su)](../physics/parameters.md#refine-ls-threshold-sigma) | <code>_edi_refine_ls.threshold_sigma</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="alias" aria-hidden="true">&#61483;</span> Alias](../physics/parameters.md#alias)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [alias](../physics/parameters.md#alias-id) | <code>_edi_alias.id</code> | — |
    | [parameter](../physics/parameters.md#alias-parameter-unique-name) | <code>_edi_alias.parameter_unique_name</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="constraint" aria-hidden="true">&#62764;</span> Constraint](../physics/parameters.md#constraint)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#constraint-id) | <code>_edi_constraint.id</code> | — |
    | [expression](../physics/parameters.md#constraint-expression) | <code>_edi_constraint.expression</code> | — |
    | [enabled](../physics/parameters.md#constraint-enabled) | <code>_edi_constraint.enabled</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="joint-fit" aria-hidden="true">&#61633;</span> Joint-fit weights](../physics/parameters.md#joint-fit)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [weight](../physics/parameters.md#joint-fit-weight) | <code>_edi_joint_fit.weight</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="sequential-fit" aria-hidden="true">&#61643;</span> Sequential fit](../physics/parameters.md#sequential-fit)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [data directory](../physics/parameters.md#sequential-fit-data-dir) | <code>_edi_sequential_fit.data_dir</code> | — |
    | [files](../physics/parameters.md#sequential-fit-file-pattern) | <code>_edi_sequential_fit.file_pattern</code> | — |
    | [reverse](../physics/parameters.md#sequential-fit-reverse) | <code>_edi_sequential_fit.reverse</code> | — |
    | [template](../physics/parameters.md#sequential-fit-template-file) | <code>_edi_sequential_fit.template_file</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="sequential-fit-extract" aria-hidden="true">&#61616;</span> Scan extraction rule](../physics/parameters.md#sequential-fit-extract)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#sequential-fit-extract-id) | <code>_edi_sequential_fit_extract.id</code> | — |
    | [target](../physics/parameters.md#sequential-fit-extract-target) | <code>_edi_sequential_fit_extract.target</code> | — |
    | [pattern](../physics/parameters.md#sequential-fit-extract-pattern) | <code>_edi_sequential_fit_extract.pattern</code> | — |
    | [required](../physics/parameters.md#sequential-fit-extract-required) | <code>_edi_sequential_fit_extract.required</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="edi" aria-hidden="true">&#61897;</span> File header](../physics/parameters.md#edi)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [schema version](../physics/parameters.md#edi-schema-version) | <code>_edi_edi.schema_version</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="report-file" aria-hidden="true">&#61787;</span> Saved report](../physics/parameters.md#report-file)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [format](../physics/parameters.md#report-file-format) | <code>_edi_report_file.format</code> | — |
    | [file](../physics/parameters.md#report-file-name) | <code>_edi_report_file.name</code> | — |
    | [saved](../physics/parameters.md#report-file-saved) | <code>_edi_report_file.saved</code> | — |
    | [project saved](../physics/parameters.md#report-file-project-last-modified) | <code>_edi_report_file.project_last_modified</code> | — |
    | [digest](../physics/parameters.md#report-file-digest) | <code>_edi_report_file.digest</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-parameter" aria-hidden="true">&#61914;</span> Fit start value](../physics/parameters.md#fit-parameter)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [parameter](../physics/parameters.md#fit-parameter-id) | <code>_edi_fit_parameter.id</code> | — |
    | [start value](../physics/parameters.md#fit-parameter-start-value) | <code>_edi_fit_parameter.start_value</code> | — |
    | [start error](../physics/parameters.md#fit-parameter-start-uncertainty) | <code>_edi_fit_parameter.start_uncertainty</code> | — |
    | [start tied](../physics/parameters.md#fit-parameter-start-tied) | <code>_edi_fit_parameter.start_tied</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-result" aria-hidden="true">&#61528;</span> Fit result](../physics/parameters.md#fit-result)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [kind](../physics/parameters.md#fit-result-result-kind) | <code>_edi_fit_result.result_kind</code> | — |
    | [success](../physics/parameters.md#fit-result-success) | <code>_edi_fit_result.success</code> | — |
    | [message](../physics/parameters.md#fit-result-message) | <code>_edi_fit_result.message</code> | — |
    | [iterations](../physics/parameters.md#fit-result-iterations) | <code>_edi_fit_result.iterations</code> | — |
    | [time](../physics/parameters.md#fit-result-fitting-time) | <code>_edi_fit_result.fitting_time</code> | s |
    | [reduced χ²](../physics/parameters.md#fit-result-reduced-chi-square) | <code>_edi_fit_result.reduced_chi_square</code> | — |
    | [objective](../physics/parameters.md#fit-result-objective-name) | <code>_edi_fit_result.objective_name</code> | — |
    | [objective value](../physics/parameters.md#fit-result-objective-value) | <code>_edi_fit_result.objective_value</code> | — |
    | [points](../physics/parameters.md#fit-result-n-data-points) | <code>_edi_fit_result.n_data_points</code> | — |
    | [parameters](../physics/parameters.md#fit-result-n-parameters) | <code>_edi_fit_result.n_parameters</code> | — |
    | [free parameters](../physics/parameters.md#fit-result-n-free-parameters) | <code>_edi_fit_result.n_free_parameters</code> | — |
    | [degrees of freedom](../physics/parameters.md#fit-result-degrees-of-freedom) | <code>_edi_fit_result.degrees_of_freedom</code> | — |
    | [covariance](../physics/parameters.md#fit-result-covariance-available) | <code>_edi_fit_result.covariance_available</code> | — |
    | [exit reason](../physics/parameters.md#fit-result-exit-reason) | <code>_edi_fit_result.exit_reason</code> | — |
    | [Rwp](../physics/parameters.md#fit-result-prof-wr-factor) | <code>_edi_fit_result.prof_wr_factor</code> | % |
    | [Rp](../physics/parameters.md#fit-result-prof-r-factor) | <code>_edi_fit_result.prof_r_factor</code> | % |
    | [Rexp](../physics/parameters.md#fit-result-prof-wr-expected) | <code>_edi_fit_result.prof_wr_expected</code> | % |
    | [cRp](../physics/parameters.md#fit-result-prof-cr-factor) | <code>_edi_fit_result.prof_cr_factor</code> | % |
    | [cRwp](../physics/parameters.md#fit-result-prof-cwr-factor) | <code>_edi_fit_result.prof_cwr_factor</code> | % |
    | [profile](../physics/parameters.md#fit-result-profile-function) | <code>_edi_fit_result.profile_function</code> | — |
    | [background](../physics/parameters.md#fit-result-background-function) | <code>_edi_fit_result.background_function</code> | — |
    | [descent](../physics/parameters.md#fit-result-descent) | <code>_edi_fit_result.descent</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-result-bank" aria-hidden="true">&#61452;</span> Experiment fit result](../physics/parameters.md#fit-result-bank)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [points](../physics/parameters.md#fit-result-bank-n-data-points) | <code>_edi_fit_result_bank.n_data_points</code> | — |
    | [Rp](../physics/parameters.md#fit-result-bank-prof-r-factor) | <code>_pd_proc_ls.prof_R_factor</code> | % |
    | [Rwp](../physics/parameters.md#fit-result-bank-prof-wr-factor) | <code>_pd_proc_ls.prof_wR_factor</code> | % |
    | [Rexp](../physics/parameters.md#fit-result-bank-prof-wr-expected) | <code>_pd_proc_ls.prof_wR_expected</code> | % |
    | [cRp](../physics/parameters.md#fit-result-bank-prof-cr-factor) | <code>_edi_fit_result_bank.prof_cr_factor</code> | % |
    | [cRwp](../physics/parameters.md#fit-result-bank-prof-cwr-factor) | <code>_edi_fit_result_bank.prof_cwr_factor</code> | % |
    | [reduced χ²](../physics/parameters.md#fit-result-bank-chi-square) | <code>_edi_fit_result_bank.chi_square</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="fit-result-phase" aria-hidden="true">&#61452;</span> Structure fit result](../physics/parameters.md#fit-result-phase)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [R Bragg](../physics/parameters.md#fit-result-phase-bragg-r-factor) | <code>_refine_ls.R_I_factor</code> | % |
    | [R F](../physics/parameters.md#fit-result-phase-f-r-factor) | <code>_refine_ls.R_factor_all</code> | % |

    **[<span class="ed-reference-icon" data-reference-category="fit-parameter-correlation" aria-hidden="true">&#61449;</span> Correlation](../physics/parameters.md#fit-parameter-correlation)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [id](../physics/parameters.md#fit-parameter-correlation-id) | <code>_edi_fit_parameter_correlation.id</code> | — |
    | [source](../physics/parameters.md#fit-parameter-correlation-source-kind) | <code>_edi_fit_parameter_correlation.source_kind</code> | — |
    | [parameter 1](../physics/parameters.md#fit-parameter-correlation-parameter-unique-name-i) | <code>_edi_fit_parameter_correlation.parameter_unique_name_i</code> | — |
    | [parameter 2](../physics/parameters.md#fit-parameter-correlation-parameter-unique-name-j) | <code>_edi_fit_parameter_correlation.parameter_unique_name_j</code> | — |
    | [correlation](../physics/parameters.md#fit-parameter-correlation-correlation) | <code>_edi_fit_parameter_correlation.correlation</code> | — |
    | [file](../physics/parameters.md#fit-parameter-correlation-file-path) | <code>_edi_fit_parameter_correlation.file_path</code> | — |

    **[<span class="ed-reference-icon" data-reference-category="pd-block" aria-hidden="true">&#61897;</span> Report block](../physics/parameters.md#pd-block)**

    | Parameter or field | CIF name | Units |
    | --- | --- | --- |
    | [block](../physics/parameters.md#pd-block-id) | <code>_pd_block.id</code> | — |
