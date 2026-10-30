---
template: physics.html
---

# Parameter and category reference

Look up a GUI label, Edi key or CIF name. Each entry describes the current field; applicability depends on the experiment and selected model. [Compare the naming systems](../user-guide/parameter-reference.md).

## Project {#metadata}

<code>_metadata</code> — The project&#x27;s name, title, description and authors.

### <code>_metadata.name</code> {#metadata-name}

The project&#x27;s short name, which names its folder.

**GUI:** name. **Units:** not applicable.

**Python:** <code>project.metadata.name</code>.

**CIF names:** <code>_edi_metadata.name</code>, <code>_project.id</code>.

### <code>_metadata.title</code> {#metadata-title}

The project&#x27;s title.

**GUI:** title. **Units:** not applicable.

**Python:** <code>project.metadata.title</code>.

**CIF names:** <code>_edi_metadata.title</code>, <code>_project.title</code>.

### <code>_metadata.description</code> {#metadata-description}

What the project is about.

**GUI:** description. **Units:** not applicable.

**Python:** <code>project.metadata.description</code>.

**CIF names:** <code>_edi_metadata.description</code>, <code>_project.description</code>.

### <code>_metadata.authors</code> {#metadata-authors}

The people the project and its report credit, separated by semicolons.

**GUI:** authors. **Units:** not applicable.

**Python:** <code>project.metadata.authors</code>.

**CIF names:** <code>_edi_metadata.authors</code>.

### <code>_metadata.path</code> {#metadata-path}

The project&#x27;s folder.

**GUI:** location. **Units:** not applicable.

**Python:** <code>project.metadata.path</code>.

**CIF names:** <code>_edi_metadata.path</code>.

### <code>_metadata.created</code> {#metadata-created}

When the project was created.

**GUI:** created. **Units:** not applicable.

**Python:** <code>project.metadata.created</code>.

**CIF names:** <code>_edi_metadata.created</code>, <code>_project.created</code>.

### <code>_metadata.last_modified</code> {#metadata-last-modified}

When the project was last saved.

**GUI:** last modified. **Units:** not applicable.

**Python:** <code>project.metadata.last_modified</code>.

**CIF names:** <code>_edi_metadata.last_modified</code>, <code>_project.last_modified</code>.

### <code>_metadata.timestamp</code> {#metadata-timestamp}

A machine-readable time of the last save.

**GUI:** timestamp. **Units:** not applicable.

**Python:** <code>project.metadata.timestamp</code>.

**CIF names:** <code>_edi_metadata.timestamp</code>, <code>_easydiffraction_project.timestamp</code>, <code>_software.timestamp</code>.

## Standard uncertainties {#su-format}

<code>_su_format</code> — How values with a standard uncertainty are written and shown.

### <code>_su_format.rule</code> {#su-format-rule}

How a value with a standard uncertainty is rounded when it is written and shown.

**GUI:** rule. **Units:** not applicable.

**Python:** <code>project.su_rule</code>.

**CIF names:** <code>_edi_su_format.rule</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>iucr_19</code> | IUCr recommendation: 1 digit, or 2 from 10 to 19 | The IUCr recommendation 12: one significant digit in the uncertainty, two from 10 to 19. |
| <code>iucr_99</code> | Always 2 digits, 10 to 99 | Always two significant digits in the uncertainty, the practice the IUCr also admits. |

## Report {#report}

<code>_report</code> — Which report formats are saved, and what they leave out.

### <code>_report.html</code> {#report-html}

Whether Save report writes the HTML report.

**GUI:** HTML. **Units:** not applicable.

**CIF names:** <code>_edi_report.html</code>, <code>_report.html</code>.

### <code>_report.pdf</code> {#report-pdf}

Whether Save report writes the PDF report.

**GUI:** PDF. **Units:** not applicable.

**CIF names:** <code>_edi_report.pdf</code>, <code>_report.pdf</code>.

### <code>_report.cif</code> {#report-cif}

Whether Save report writes the CIF report.

**GUI:** CIF. **Units:** not applicable.

**CIF names:** <code>_edi_report.cif</code>, <code>_report.cif</code>.

### <code>_report.html_offline</code> {#report-html-offline}

Whether the HTML report carries its chart libraries, so it opens offline.

**GUI:** embed chart libraries. **Units:** not applicable.

**CIF names:** <code>_edi_report.html_offline</code>, <code>_report.html_offline</code>.

### <code>_report.excluded</code> {#report-excluded}

The report sections left out.

**GUI:** excluded. **Units:** not applicable.

**CIF names:** <code>_edi_report.excluded</code>.

## Correlation chart {#correlation-chart}

<code>_correlation_chart</code> — Settings of the parameter-correlation chart.

### <code>_correlation_chart.threshold</code> {#correlation-chart-threshold}

The smallest absolute correlation the chart shows.

**GUI:** threshold. **Units:** not applicable.

**CIF names:** <code>_edi_correlation_chart.threshold</code>.

## Pattern chart {#pattern-chart}

<code>_pattern_chart</code> — Settings of the diffraction pattern chart.

### <code>_pattern_chart.x_axis</code> {#pattern-chart-x-axis}

The pattern chart&#x27;s horizontal axis.

**GUI:** x-axis. **Units:** not applicable.

**CIF names:** <code>_edi_pattern_chart.x_axis</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>native</code> | Measured axis | The experiment&#x27;s own axis: 2θ or time of flight. |
| <code>d_spacing</code> | d-spacing | The d-spacing of each point. |

## Space group {#space-group}

<code>_space_group</code> — The structure&#x27;s space group.

### <code>_space_group.name_h_m</code> {#space-group-name-h-m}

The Hermann-Mauguin symbol of the space group.

**GUI:** name. **Units:** not applicable.

**Python:** <code>project.structures[0].space_group.name_h_m</code>.

**CIF names:** <code>_space_group.name_H-M_alt</code>, <code>_space_group_name_H-M_alt</code>, <code>_symmetry.space_group_name_H-M</code>, <code>_symmetry_space_group_name_H-M</code>.

### <code>_space_group.coord_system_code</code> {#space-group-coord-system-code}

The setting of the space group, such as an origin choice or axes.

**GUI:** code. **Units:** not applicable.

**Python:** <code>project.structures[0].space_group.coord_system_code</code>.

**CIF names:** <code>_space_group.IT_coordinate_system_code</code>, <code>_space_group_IT_coordinate_system_code</code>, <code>_symmetry.IT_coordinate_system_code</code>, <code>_symmetry_IT_coordinate_system_code</code>.

### <code>_space_group.it_number</code> {#space-group-it-number}

The number of the space group in International Tables, from 1 to 230.

**GUI:** number. **Units:** not applicable.

**Python:** <code>project.structures[0].space_group.it_number</code>.

**CIF names:** <code>_space_group.IT_number</code>, <code>_space_group_IT_number</code>, <code>_symmetry.Int_Tables_number</code>, <code>_symmetry_Int_Tables_number</code>.

## Cell {#cell}

<code>_cell</code> — The lengths and angles of the unit cell.

### <code>_cell.length_a</code> {#cell-length-a}

Unit-cell length a.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61874;</span> <span class="ed-reference-icon" aria-hidden="true">&#62789;</span> a. **Units:** Å.

**Calculation role:** model-parameter. [Scientific explanation](crystallography.md#eq-cell-metric).

**Python:** <code>project.structures[0].cell.length_a</code>.

**CIF names:** <code>_cell.length_a</code>, <code>_cell_length_a</code>.

### <code>_cell.length_b</code> {#cell-length-b}

Unit-cell length b.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61874;</span> <span class="ed-reference-icon" aria-hidden="true">&#62789;</span> b. **Units:** Å.

**Calculation role:** model-parameter. [Scientific explanation](crystallography.md#eq-cell-metric).

**Python:** <code>project.structures[0].cell.length_b</code>.

**CIF names:** <code>_cell.length_b</code>, <code>_cell_length_b</code>.

### <code>_cell.length_c</code> {#cell-length-c}

Unit-cell length c.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61874;</span> <span class="ed-reference-icon" aria-hidden="true">&#62789;</span> c. **Units:** Å.

**Calculation role:** model-parameter. [Scientific explanation](crystallography.md#eq-cell-metric).

**Python:** <code>project.structures[0].cell.length_c</code>.

**CIF names:** <code>_cell.length_c</code>, <code>_cell_length_c</code>.

### <code>_cell.angle_alpha</code> {#cell-angle-alpha}

Unit-cell angle between b and c (degrees; engine converts to radians).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61874;</span> <span class="ed-reference-icon" aria-hidden="true">&#62789;</span> α. **Units:** deg.

**Calculation role:** model-parameter. [Scientific explanation](crystallography.md#eq-cell-metric).

**Python:** <code>project.structures[0].cell.angle_alpha</code>.

**CIF names:** <code>_cell.angle_alpha</code>, <code>_cell_angle_alpha</code>.

### <code>_cell.angle_beta</code> {#cell-angle-beta}

Unit-cell angle between a and c (degrees; engine converts to radians).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61874;</span> <span class="ed-reference-icon" aria-hidden="true">&#62789;</span> β. **Units:** deg.

**Calculation role:** model-parameter. [Scientific explanation](crystallography.md#eq-cell-metric).

**Python:** <code>project.structures[0].cell.angle_beta</code>.

**CIF names:** <code>_cell.angle_beta</code>, <code>_cell_angle_beta</code>.

### <code>_cell.angle_gamma</code> {#cell-angle-gamma}

Unit-cell angle between a and b (degrees; engine converts to radians).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61874;</span> <span class="ed-reference-icon" aria-hidden="true">&#62789;</span> γ. **Units:** deg.

**Calculation role:** model-parameter. [Scientific explanation](crystallography.md#eq-cell-metric).

**Python:** <code>project.structures[0].cell.angle_gamma</code>.

**CIF names:** <code>_cell.angle_gamma</code>, <code>_cell_angle_gamma</code>.

## Atom site {#atom-site}

<code>_atom_site</code> — The atom sites of the structure: position, occupancy and isotropic displacement.

### <code>_atom_site.id</code> {#atom-site-id}

Unique atom-site identifier.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> id. **Units:** not applicable.

**Calculation role:** descriptor. [Scientific explanation](diffraction.md#eq-nuclear-structure-factor).

**Python:** <code>project.structures[0].atom_sites[0].id</code>.

**CIF names:** <code>_atom_site.label</code>, <code>_atom_site_label</code>, <code>_atom_site.id</code>.

**Earlier Edi spellings accepted on import:** <code>_atom_site.label</code>.

### <code>_atom_site.type_symbol</code> {#atom-site-type-symbol}

Chemical symbol of the atom at this site.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> type. **Units:** not applicable.

**Calculation role:** descriptor. [Scientific explanation](diffraction.md#eq-nuclear-structure-factor).

**Python:** <code>project.structures[0].atom_sites[0].type_symbol</code>.

**CIF names:** <code>_atom_site.type_symbol</code>, <code>_atom_site_type_symbol</code>.

### <code>_atom_site.wyckoff_letter</code> {#atom-site-wyckoff-letter}

Wyckoff letter of the site in its space group.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> WP. **Units:** not applicable.

**Calculation role:** descriptor. [Scientific explanation](diffraction.md#eq-nuclear-structure-factor).

**Python:** <code>project.structures[0].atom_sites[0].wyckoff_letter</code>.

**CIF names:** <code>_atom_site.Wyckoff_symbol</code>, <code>_atom_site_Wyckoff_symbol</code>, <code>_atom_site.Wyckoff_letter</code>.

### <code>_atom_site.adp_type</code> {#atom-site-adp-type}

Atomic displacement parameter type: Biso, Uiso, Bani, Uani or beta; Biso when absent.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> ADP type. **Units:** not applicable.

**Calculation role:** descriptor. [Scientific explanation](displacement.md#eq-isotropic-adp).

**Python:** <code>project.structures[0].atom_sites[0].adp_type</code>.

**CIF names:** <code>_atom_site.ADP_type</code>, <code>_atom_site_ADP_type</code>, <code>_atom_site_thermal_displace_type</code>, <code>_atom_site.thermal_displace_type</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>Biso</code> | B iso | Isotropic, B in Å². |
| <code>Uiso</code> | U iso | Isotropic, U in Å². |
| <code>Bani</code> | B aniso | Anisotropic, the B tensor in Å². |
| <code>Uani</code> | U aniso | Anisotropic, the U tensor in Å². |
| <code>beta</code> | β | Anisotropic, the dimensionless β tensor. |

### <code>_atom_site.fract_x</code> {#atom-site-fract-x}

Fractional x-coordinate of the atom site.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> <span class="ed-reference-icon" aria-hidden="true">&#62405;</span> x. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](diffraction.md#eq-nuclear-structure-factor).

**Python:** <code>project.structures[0].atom_sites[0].fract_x</code>.

**CIF names:** <code>_atom_site.fract_x</code>, <code>_atom_site_fract_x</code>.

### <code>_atom_site.fract_y</code> {#atom-site-fract-y}

Fractional y-coordinate of the atom site.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> <span class="ed-reference-icon" aria-hidden="true">&#62405;</span> y. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](diffraction.md#eq-nuclear-structure-factor).

**Python:** <code>project.structures[0].atom_sites[0].fract_y</code>.

**CIF names:** <code>_atom_site.fract_y</code>, <code>_atom_site_fract_y</code>.

### <code>_atom_site.fract_z</code> {#atom-site-fract-z}

Fractional z-coordinate of the atom site.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> <span class="ed-reference-icon" aria-hidden="true">&#62405;</span> z. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](diffraction.md#eq-nuclear-structure-factor).

**Python:** <code>project.structures[0].atom_sites[0].fract_z</code>.

**CIF names:** <code>_atom_site.fract_z</code>, <code>_atom_site_fract_z</code>.

### <code>_atom_site.occupancy</code> {#atom-site-occupancy}

Site occupancy (raw occupancy; m/M multiplicity applied in &#124;F&#124;^2).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> <span class="ed-reference-icon" aria-hidden="true">&#62837;</span> occ. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](diffraction.md#eq-nuclear-structure-factor).

**Python:** <code>project.structures[0].atom_sites[0].occupancy</code>.

**CIF names:** <code>_atom_site.occupancy</code>, <code>_atom_site_occupancy</code>.

### <code>_atom_site.adp_iso</code> {#atom-site-adp-iso}

Isotropic atomic displacement parameter in the site&#x27;s declared type: B for Biso, U for Uiso (B = 8 pi^2 U); an anisotropic site&#x27;s equivalent isotropic value, derived.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> iso/eq. **Units:** Å².

**Calculation role:** model-parameter. [Scientific explanation](displacement.md#eq-isotropic-adp).

**Python:** <code>project.structures[0].atom_sites[0].adp_iso</code>.

**CIF names:** <code>_atom_site.B_iso_or_equiv</code>, <code>_atom_site_B_iso_or_equiv</code>, <code>_atom_site.U_iso_or_equiv</code>, <code>_atom_site_U_iso_or_equiv</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>Biso</code> | B iso | Å² | <code>_atom_site.B_iso_or_equiv</code> |
| <code>Uiso</code> | U iso | Å² | <code>_atom_site.U_iso_or_equiv</code> |
| <code>Bani</code> | B eq | Å² | <code>_atom_site.B_iso_or_equiv</code> |
| <code>Uani</code> | U eq | Å² | <code>_atom_site.U_iso_or_equiv</code> |
| <code>beta</code> | B eq | Å² | <code>_atom_site.B_iso_or_equiv</code> |

## Atomic displacement {#atom-site-aniso}

<code>_atom_site_aniso</code> — The anisotropic displacement of each anisotropic atom site.

### <code>_atom_site_aniso.id</code> {#atom-site-aniso-id}

The id of the anisotropic atom site the row belongs to.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> id. **Units:** not applicable.

**Calculation role:** descriptor. [Scientific explanation](displacement.md#eq-anisotropic-adp).

**Python:** <code>project.structures[0].atom_site_aniso[0].id</code>.

**CIF names:** <code>_atom_site_aniso.label</code>, <code>_atom_site_aniso_label</code>, <code>_atom_site_anisotrop.id</code>.

**Earlier Edi spellings accepted on import:** <code>_atom_site_aniso.label</code>.

### <code>_atom_site_aniso.adp_11</code> {#atom-site-aniso-adp-11}

Anisotropic displacement tensor component 11 (diagonal 11) in the site&#x27;s declared type: U for Uani, B for Bani (Å²), dimensionless beta for beta.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> 11. **Units:** Å².

**Calculation role:** model-parameter. [Scientific explanation](displacement.md#eq-anisotropic-adp).

**Python:** <code>project.structures[0].atom_site_aniso[0].adp_11</code>.

**CIF names:** <code>_atom_site_aniso.B_11</code>, <code>_atom_site_aniso_B_11</code>, <code>_atom_site.aniso_B[1][1]</code>, <code>_atom_site_anisotrop.B[1][1]</code>, <code>_atom_site_aniso.U_11</code>, <code>_atom_site_aniso_U_11</code>, <code>_atom_site.aniso_U[1][1]</code>, <code>_atom_site_anisotrop.U[1][1]</code>, <code>_atom_site_aniso.beta_11</code>, <code>_atom_site_aniso_beta_11</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>Uani</code> | U₁₁ | Å² | <code>_atom_site_aniso.U_11</code> |
| <code>Bani</code> | B₁₁ | Å² | <code>_atom_site_aniso.B_11</code> |
| <code>beta</code> | β₁₁ | Å² | <code>_atom_site_aniso.beta_11</code> |

### <code>_atom_site_aniso.adp_22</code> {#atom-site-aniso-adp-22}

Anisotropic displacement tensor component 22 (diagonal 22) in the site&#x27;s declared type: U for Uani, B for Bani (Å²), dimensionless beta for beta.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> 22. **Units:** Å².

**Calculation role:** model-parameter. [Scientific explanation](displacement.md#eq-anisotropic-adp).

**Python:** <code>project.structures[0].atom_site_aniso[0].adp_22</code>.

**CIF names:** <code>_atom_site_aniso.B_22</code>, <code>_atom_site_aniso_B_22</code>, <code>_atom_site.aniso_B[2][2]</code>, <code>_atom_site_anisotrop.B[2][2]</code>, <code>_atom_site_aniso.U_22</code>, <code>_atom_site_aniso_U_22</code>, <code>_atom_site.aniso_U[2][2]</code>, <code>_atom_site_anisotrop.U[2][2]</code>, <code>_atom_site_aniso.beta_22</code>, <code>_atom_site_aniso_beta_22</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>Uani</code> | U₂₂ | Å² | <code>_atom_site_aniso.U_22</code> |
| <code>Bani</code> | B₂₂ | Å² | <code>_atom_site_aniso.B_22</code> |
| <code>beta</code> | β₂₂ | Å² | <code>_atom_site_aniso.beta_22</code> |

### <code>_atom_site_aniso.adp_33</code> {#atom-site-aniso-adp-33}

Anisotropic displacement tensor component 33 (diagonal 33) in the site&#x27;s declared type: U for Uani, B for Bani (Å²), dimensionless beta for beta.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> 33. **Units:** Å².

**Calculation role:** model-parameter. [Scientific explanation](displacement.md#eq-anisotropic-adp).

**Python:** <code>project.structures[0].atom_site_aniso[0].adp_33</code>.

**CIF names:** <code>_atom_site_aniso.B_33</code>, <code>_atom_site_aniso_B_33</code>, <code>_atom_site.aniso_B[3][3]</code>, <code>_atom_site_anisotrop.B[3][3]</code>, <code>_atom_site_aniso.U_33</code>, <code>_atom_site_aniso_U_33</code>, <code>_atom_site.aniso_U[3][3]</code>, <code>_atom_site_anisotrop.U[3][3]</code>, <code>_atom_site_aniso.beta_33</code>, <code>_atom_site_aniso_beta_33</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>Uani</code> | U₃₃ | Å² | <code>_atom_site_aniso.U_33</code> |
| <code>Bani</code> | B₃₃ | Å² | <code>_atom_site_aniso.B_33</code> |
| <code>beta</code> | β₃₃ | Å² | <code>_atom_site_aniso.beta_33</code> |

### <code>_atom_site_aniso.adp_12</code> {#atom-site-aniso-adp-12}

Anisotropic displacement tensor component 12 (off-diagonal 12) in the site&#x27;s declared type: U for Uani, B for Bani (Å²), dimensionless beta for beta.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> 12. **Units:** Å².

**Calculation role:** model-parameter. [Scientific explanation](displacement.md#eq-anisotropic-adp).

**Python:** <code>project.structures[0].atom_site_aniso[0].adp_12</code>.

**CIF names:** <code>_atom_site_aniso.B_12</code>, <code>_atom_site_aniso_B_12</code>, <code>_atom_site.aniso_B[1][2]</code>, <code>_atom_site_anisotrop.B[1][2]</code>, <code>_atom_site_aniso.U_12</code>, <code>_atom_site_aniso_U_12</code>, <code>_atom_site.aniso_U[1][2]</code>, <code>_atom_site_anisotrop.U[1][2]</code>, <code>_atom_site_aniso.beta_12</code>, <code>_atom_site_aniso_beta_12</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>Uani</code> | U₁₂ | Å² | <code>_atom_site_aniso.U_12</code> |
| <code>Bani</code> | B₁₂ | Å² | <code>_atom_site_aniso.B_12</code> |
| <code>beta</code> | β₁₂ | Å² | <code>_atom_site_aniso.beta_12</code> |

### <code>_atom_site_aniso.adp_13</code> {#atom-site-aniso-adp-13}

Anisotropic displacement tensor component 13 (off-diagonal 13) in the site&#x27;s declared type: U for Uani, B for Bani (Å²), dimensionless beta for beta.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> 13. **Units:** Å².

**Calculation role:** model-parameter. [Scientific explanation](displacement.md#eq-anisotropic-adp).

**Python:** <code>project.structures[0].atom_site_aniso[0].adp_13</code>.

**CIF names:** <code>_atom_site_aniso.B_13</code>, <code>_atom_site_aniso_B_13</code>, <code>_atom_site.aniso_B[1][3]</code>, <code>_atom_site_anisotrop.B[1][3]</code>, <code>_atom_site_aniso.U_13</code>, <code>_atom_site_aniso_U_13</code>, <code>_atom_site.aniso_U[1][3]</code>, <code>_atom_site_anisotrop.U[1][3]</code>, <code>_atom_site_aniso.beta_13</code>, <code>_atom_site_aniso_beta_13</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>Uani</code> | U₁₃ | Å² | <code>_atom_site_aniso.U_13</code> |
| <code>Bani</code> | B₁₃ | Å² | <code>_atom_site_aniso.B_13</code> |
| <code>beta</code> | β₁₃ | Å² | <code>_atom_site_aniso.beta_13</code> |

### <code>_atom_site_aniso.adp_23</code> {#atom-site-aniso-adp-23}

Anisotropic displacement tensor component 23 (off-diagonal 23) in the site&#x27;s declared type: U for Uani, B for Bani (Å²), dimensionless beta for beta.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> <span class="ed-reference-icon" aria-hidden="true">&#61618;</span> 23. **Units:** Å².

**Calculation role:** model-parameter. [Scientific explanation](displacement.md#eq-anisotropic-adp).

**Python:** <code>project.structures[0].atom_site_aniso[0].adp_23</code>.

**CIF names:** <code>_atom_site_aniso.B_23</code>, <code>_atom_site_aniso_B_23</code>, <code>_atom_site.aniso_B[2][3]</code>, <code>_atom_site_anisotrop.B[2][3]</code>, <code>_atom_site_aniso.U_23</code>, <code>_atom_site_aniso_U_23</code>, <code>_atom_site.aniso_U[2][3]</code>, <code>_atom_site_anisotrop.U[2][3]</code>, <code>_atom_site_aniso.beta_23</code>, <code>_atom_site_aniso_beta_23</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>Uani</code> | U₂₃ | Å² | <code>_atom_site_aniso.U_23</code> |
| <code>Bani</code> | B₂₃ | Å² | <code>_atom_site_aniso.B_23</code> |
| <code>beta</code> | β₂₃ | Å² | <code>_atom_site_aniso.beta_23</code> |

## Scattering length {#scattering-length}

<code>_scattering_length</code> — Neutron coherent scattering lengths that replace the built-in table for an element or isotope.

### <code>_scattering_length.type_symbol</code> {#scattering-length-type-symbol}

The element or isotope the scattering length applies to.

**GUI:** type. **Units:** not applicable.

**CIF names:** <code>_edi_scattering_length.type_symbol</code>.

### <code>_scattering_length.length_fm</code> {#scattering-length-length-fm}

The coherent neutron scattering length.

**GUI:** b. **Units:** fm.

**CIF names:** <code>_edi_scattering_length.length_fm</code>.

## Bond settings {#geom}

<code>_geom</code> — How bonds between atoms are found.

### <code>_geom.min_bond_distance_cutoff</code> {#geom-min-bond-distance-cutoff}

Atoms closer than this are not bonded.

**GUI:** minimum distance. **Units:** Å.

**Python:** <code>project.structures[0].geom.min_bond_distance_cutoff</code>.

**CIF names:** <code>_geom.min_bond_distance_cutoff</code>.

### <code>_geom.bond_distance_inc</code> {#geom-bond-distance-inc}

How much longer than the sum of the covalent radii a bond may be.

**GUI:** tolerance. **Units:** Å.

**Python:** <code>project.structures[0].geom.bond_distance_inc</code>.

**CIF names:** <code>_geom.bond_distance_incr</code>.

## Appearance {#structure-view}

<code>_structure_view</code> — How the structure view draws the structure: atoms, colours, labels and what else it shows.

### <code>_structure_view.atom_view</code> {#structure-view-atom-view}

What sets the size of each atom.

**GUI:** atoms as. **Units:** not applicable.

**CIF names:** <code>_edi_structure_view.atom_view</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>covalent</code> | Covalent radius | The covalent radius. |
| <code>vdw</code> | Van der Waals radius | The van der Waals radius. |
| <code>ionic</code> | Ionic radius | The ionic radius. |
| <code>adp</code> | Displacement | The atomic displacement, at the probability set. |

### <code>_structure_view.colour_scheme</code> {#structure-view-colour-scheme}

The colours the atoms take, by element.

**GUI:** colours. **Units:** not applicable.

**CIF names:** <code>_edi_structure_view.colour_scheme</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>jmol</code> | Jmol | The Jmol colours. |
| <code>vesta</code> | VESTA | The VESTA colours. |

### <code>_structure_view.atom_scale</code> {#structure-view-atom-scale}

The atoms&#x27; drawn size as a share of their radius.

**GUI:** atom scale. **Units:** not applicable.

**CIF names:** <code>_edi_structure_view.atom_scale</code>.

### <code>_structure_view.adp_probability</code> {#structure-view-adp-probability}

The probability the displacement ellipsoids enclose.

**GUI:** probability. **Units:** not applicable.

**CIF names:** <code>_edi_structure_view.adp_probability</code>.

### <code>_structure_view.labels</code> {#structure-view-labels}

Whether each atom is labelled.

**GUI:** labels. **Units:** not applicable.

**CIF names:** <code>_edi_structure_view.labels</code>.

### <code>_structure_view.atoms</code> {#structure-view-atoms}

Which atoms are drawn.

**GUI:** atoms shown. **Units:** not applicable.

**CIF names:** <code>_edi_structure_view.atoms</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>all</code> | All | Every atom in the cell. |
| <code>asymmetric</code> | Asymmetric unit | The atoms of the asymmetric unit. |
| <code>none</code> | None | No atoms. |

### <code>_structure_view.bonds</code> {#structure-view-bonds}

Whether bonds are drawn.

**GUI:** bonds. **Units:** not applicable.

**CIF names:** <code>_edi_structure_view.bonds</code>.

### <code>_structure_view.cell</code> {#structure-view-cell}

Whether the unit cell is drawn.

**GUI:** cell. **Units:** not applicable.

**CIF names:** <code>_edi_structure_view.cell</code>.

### <code>_structure_view.axes</code> {#structure-view-axes}

Whether the cell axes are drawn.

**GUI:** axes. **Units:** not applicable.

**CIF names:** <code>_edi_structure_view.axes</code>.

## Experiment type {#experiment-type}

<code>_experiment_type</code> — What kind of experiment this is: sample form, beam mode, probe and scattering type.

### <code>_experiment_type.beam_mode</code> {#experiment-type-beam-mode}

How the pattern is measured.

**GUI:** beam mode. **Units:** not applicable.

**Python:** <code>project.experiments[0].experiment_type.beam_mode</code>.

**CIF names:** <code>_edi_experiment_type.beam_mode</code>, <code>_easydiffraction_experiment_type.beam_mode</code>, <code>_expt_type.beam_mode</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>constant wavelength</code> | Constant wavelength | One wavelength, the pattern measured against the scattering angle 2θ. |
| <code>time-of-flight</code> | Time-of-flight | A white beam, the pattern measured against the time of flight. |

### <code>_experiment_type.sample_form</code> {#experiment-type-sample-form}

The form of the sample.

**GUI:** sample form. **Units:** not applicable.

**Python:** <code>project.experiments[0].experiment_type.sample_form</code>.

**CIF names:** <code>_edi_experiment_type.sample_form</code>, <code>_easydiffraction_experiment_type.sample_form</code>, <code>_expt_type.sample_form</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>powder</code> | Powder | A polycrystalline sample. |
| <code>single crystal</code> | Single crystal | One crystal. |

### <code>_experiment_type.radiation_probe</code> {#experiment-type-radiation-probe}

The radiation scattered by the sample.

**GUI:** probe. **Units:** not applicable.

**Python:** <code>project.experiments[0].experiment_type.radiation_probe</code>.

**CIF names:** <code>_diffrn_radiation.probe</code>, <code>_diffrn_radiation_probe</code>, <code>_easydiffraction_experiment_type.radiation_probe</code>, <code>_expt_type.radiation_probe</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>neutron</code> | Neutron | Neutrons, scattered by the nuclei. |
| <code>xray</code> | X-ray | X-rays, scattered by the electrons. |

### <code>_experiment_type.scattering_type</code> {#experiment-type-scattering-type}

Which scattering the pattern is modelled with.

**GUI:** scattering type. **Units:** not applicable.

**Python:** <code>project.experiments[0].experiment_type.scattering_type</code>.

**CIF names:** <code>_edi_experiment_type.scattering_type</code>, <code>_easydiffraction_experiment_type.scattering_type</code>, <code>_expt_type.scattering_type</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>bragg</code> | Bragg | Bragg peaks from the average structure. |
| <code>total</code> | Total | Bragg and diffuse scattering together. |

### <code>_experiment_type.dimensionality</code> {#experiment-type-dimensionality}

The dimensionality of the measured pattern.

**GUI:** dimensionality. **Units:** not applicable.

**Python:** <code>project.experiments[0].experiment_type.dimensionality</code>.

**CIF names:** <code>_edi_experiment_type.dimensionality</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>1d</code> | 1D | A one-dimensional pattern. |

### <code>_experiment_type.polarisation</code> {#experiment-type-polarisation}

The polarisation of the incident beam; an X-ray experiment states the inapplicable value.

**GUI:** polarisation. **Units:** not applicable.

**Python:** <code>project.experiments[0].experiment_type.polarisation</code>.

**CIF names:** <code>_edi_experiment_type.polarisation</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>unpolarised</code> | Unpolarised | An unpolarised neutron beam. |
| <code>.</code> | Not applicable | An X-ray experiment, whose beam polarisation is not a setting here. |

## Calculation range {#data-range}

<code>_data_range</code> — The grid a pattern is calculated on when no data are measured.

### <code>_data_range.two_theta_min</code> {#data-range-two-theta-min}

The first 2θ of the calculation grid.

**GUI:** min. **Units:** deg.

**CIF names:** <code>_pd_meas.2theta_range_min</code>, <code>_pd_meas_2theta_range_min</code>.

### <code>_data_range.two_theta_max</code> {#data-range-two-theta-max}

The last 2θ of the calculation grid.

**GUI:** max. **Units:** deg.

**CIF names:** <code>_pd_meas.2theta_range_max</code>, <code>_pd_meas_2theta_range_max</code>.

### <code>_data_range.two_theta_step</code> {#data-range-two-theta-step}

The 2θ step of the calculation grid.

**GUI:** step. **Units:** deg.

**CIF names:** <code>_pd_meas.2theta_range_inc</code>, <code>_pd_meas_2theta_range_inc</code>.

### <code>_data_range.two_theta</code> {#data-range-two-theta}

The 2θ points of the calculation grid.

**GUI:** 2θ. **Units:** deg.

**CIF names:** <code>_edi_data_range.two_theta</code>.

### <code>_data_range.time_of_flight_min</code> {#data-range-time-of-flight-min}

The first time of flight of the calculation grid.

**GUI:** min. **Units:** µs.

**CIF names:** <code>_edi_data_range.time_of_flight_min</code>, <code>_pd_meas.time_of_flight_range_min</code>.

### <code>_data_range.time_of_flight_max</code> {#data-range-time-of-flight-max}

The last time of flight of the calculation grid.

**GUI:** max. **Units:** µs.

**CIF names:** <code>_edi_data_range.time_of_flight_max</code>, <code>_pd_meas.time_of_flight_range_max</code>.

### <code>_data_range.time_of_flight_step</code> {#data-range-time-of-flight-step}

The time-of-flight step of the calculation grid.

**GUI:** step. **Units:** µs.

**CIF names:** <code>_edi_data_range.time_of_flight_step</code>.

### <code>_data_range.time_of_flight</code> {#data-range-time-of-flight}

The time-of-flight points of the calculation grid.

**GUI:** TOF. **Units:** µs.

**CIF names:** <code>_edi_data_range.time_of_flight</code>.

## Background {#background}

<code>_background</code> — The background under the diffraction peaks.

### <code>_background.intensity</code> {#background-intensity}

Line-segment background intensity anchor (dimensionless in the reduced pattern; linear).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> <span class="ed-reference-icon" aria-hidden="true">&#63228;</span> intensity. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](background.md#eq-line-segment-background).

**Python:** <code>project.experiments[0].background[0].intensity</code>.

**CIF names:** <code>_pd_background.line_segment_intensity</code>, <code>_pd_background_line_segment_intensity</code>.

### <code>_background.position</code> {#background-position}

Background anchor position (TOF, us); a fixed node, not a refinable Parameter.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> position. **Units:** µs.

**Calculation role:** descriptor. [Scientific explanation](background.md#eq-line-segment-background).

**Python:** <code>project.experiments[0].background[0].position</code>.

**CIF names:** <code>_pd_background.line_segment_X</code>, <code>_pd_background_line_segment_X</code>.

### <code>_background.coef</code> {#background-coef}

Polynomial or Chebyshev background coefficient of the row&#x27;s order (dimensionless in the reduced pattern; linear).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> coefficient. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](background.md#eq-chebyshev-background).

**CIF names:** <code>_pd_background.Chebyshev_coef</code>.

### <code>_background.order</code> {#background-order}

Order m of a polynomial or Chebyshev background term (a non-negative integer; a fixed node, not a refinable Parameter).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> order. **Units:** not applicable.

**Calculation role:** descriptor. [Scientific explanation](background.md#eq-chebyshev-background).

**CIF names:** <code>_pd_background.Chebyshev_order</code>.

### <code>_background.origin</code> {#background-origin}

Origin of the polynomial background, FullProf Bkpos: the terms are powers of x/origin - 1 (in the pattern&#x27;s axis units; non-zero).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> origin. **Units:** not applicable.

**Calculation role:** descriptor. [Scientific explanation](background.md#eq-polynomial-background).

**Python:** <code>project.experiments[0].background_origin</code>.

**CIF names:** <code>_edi_background.origin</code>.

### <code>_background.x_min</code> {#background-x-min}

Lower end of the Chebyshev background&#x27;s normalisation domain (in the pattern&#x27;s axis units).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> x min. **Units:** not applicable.

**Calculation role:** descriptor. [Scientific explanation](background.md#eq-chebyshev-background).

**Python:** <code>project.experiments[0].background_x_min</code>.

**CIF names:** <code>_edi_background.x_min</code>.

### <code>_background.x_max</code> {#background-x-max}

Upper end of the Chebyshev background&#x27;s normalisation domain (in the pattern&#x27;s axis units; above x_min).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63550;</span> x max. **Units:** not applicable.

**Calculation role:** descriptor. [Scientific explanation](background.md#eq-chebyshev-background).

**Python:** <code>project.experiments[0].background_x_max</code>.

**CIF names:** <code>_edi_background.x_max</code>.

### <code>_background.type</code> {#background-type}

The background function.

**GUI:** type. **Units:** not applicable.

**Python:** <code>project.experiments[0].background_type</code>.

**CIF names:** <code>_edi_background.type</code>, <code>_easydiffraction_background.type</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>line-segment</code> | Line segment | Straight lines between background points. |
| <code>chebyshev</code> | Chebyshev | A sum of Chebyshev polynomials. |
| <code>polynomial</code> | Polynomial | A polynomial in the scattering variable. |

### <code>_background.id</code> {#background-id}

The name of a background point or term.

**GUI:** id. **Units:** not applicable.

**Python:** <code>project.experiments[0].background[0].id</code>.

**CIF names:** <code>_pd_background.id</code>.

## Background estimation {#background-estimate}

<code>_background_estimate</code> — How the background is estimated from the measured pattern.

### <code>_background_estimate.mode</code> {#background-estimate-mode}

Whether the background is edited by hand or estimated again on every change.

**GUI:** estimation mode. **Units:** not applicable.

**CIF names:** <code>_edi_background_estimate.mode</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>manual</code> | Manual | The background is edited by hand; Estimate replaces it when asked. |
| <code>auto</code> | Auto | The background is estimated again whenever the data or the settings change. |

### <code>_background_estimate.method</code> {#background-estimate-method}

The background estimation method.

**GUI:** method. **Units:** not applicable.

**CIF names:** <code>_edi_background_estimate.method</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>auto</code> | Auto | The default method, arPLS. |
| <code>snip</code> | SNIP | SNIP (Ryan et al. 1988): clips the peaks away. |
| <code>arpls</code> | arPLS | arPLS (Baek et al. 2015): asymmetrically reweighted penalized least squares. |
| <code>fabc</code> | FABC | FABC (Cobas et al. 2006): finds the baseline points by a wavelet transform. |

### <code>_background_estimate.width</code> {#background-estimate-width}

The peak width the estimation assumes, in points.

**GUI:** peak width. **Units:** not applicable.

**CIF names:** <code>_edi_background_estimate.width</code>.

### <code>_background_estimate.smoothness</code> {#background-estimate-smoothness}

How smooth the estimated background is.

**GUI:** smoothness. **Units:** not applicable.

**CIF names:** <code>_edi_background_estimate.smoothness</code>.

### <code>_background_estimate.n_points</code> {#background-estimate-n-points}

How many background points the estimation keeps.

**GUI:** points. **Units:** not applicable.

**CIF names:** <code>_edi_background_estimate.n_points</code>.

### <code>_background_estimate.tolerance</code> {#background-estimate-tolerance}

How far, in units of the noise, the thinned background may stray.

**GUI:** tolerance. **Units:** not applicable.

**CIF names:** <code>_edi_background_estimate.tolerance</code>.

### <code>_background_estimate.in_peaks</code> {#background-estimate-in-peaks}

What happens to a background point that falls in a peak.

**GUI:** points in peaks. **Units:** not applicable.

**CIF names:** <code>_edi_background_estimate.in_peaks</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>move</code> | Move | Move it to the nearest allowed point. |
| <code>drop</code> | Drop | Drop it. |

### <code>_background_estimate.use_model</code> {#background-estimate-use-model}

What the estimation does with the peaks of the calculated pattern.

**GUI:** calculated peaks. **Units:** not applicable.

**CIF names:** <code>_edi_background_estimate.use_model</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>auto</code> | Auto | Subtract them when the calculated pattern matches the data. |
| <code>subtract</code> | Subtract | Always subtract them when there is a calculated pattern. |
| <code>ignore</code> | Ignore | Never subtract them. |

### <code>_background_estimate.max_terms</code> {#background-estimate-max-terms}

The most terms a Chebyshev or polynomial background may take.

**GUI:** max terms. **Units:** not applicable.

**CIF names:** <code>_edi_background_estimate.max_terms</code>.

### <code>_background_estimate.inputs_digest</code> {#background-estimate-inputs-digest}

A checksum of what the last estimate was made from.

**GUI:** inputs digest. **Units:** not applicable.

**CIF names:** <code>_edi_background_estimate.inputs_digest</code>.

### <code>_background_estimate.points_digest</code> {#background-estimate-points-digest}

A checksum of the background the last estimate wrote.

**GUI:** points digest. **Units:** not applicable.

**CIF names:** <code>_edi_background_estimate.points_digest</code>.

## Instrument {#instrument}

<code>_instrument</code> — The instrument setup and calibration.

### <code>_instrument.calib_d_to_tof_offset</code> {#instrument-calib-d-to-tof-offset}

TOF calibration zero offset (TOF = zero + Dtt1*d + Dtt2*d^2 + recip/d).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62263;</span> TOF offset. **Units:** µs.

**Calculation role:** model-parameter. [Scientific explanation](calibration.md#eq-tof-calibration).

**Python:** <code>project.experiments[0].instrument.calib_d_to_tof_offset</code>.

**CIF names:** <code>_edi_instrument.calib_d_to_tof_offset</code>, <code>_instr.d_to_tof_offset</code>.

### <code>_instrument.calib_d_to_tof_linear</code> {#instrument-calib-d-to-tof-linear}

TOF calibration linear coefficient Dtt1 (us/A).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63417;</span> TOF linear. **Units:** µs/Å.

**Calculation role:** model-parameter. [Scientific explanation](calibration.md#eq-tof-calibration).

**Python:** <code>project.experiments[0].instrument.calib_d_to_tof_linear</code>.

**CIF names:** <code>_edi_instrument.calib_d_to_tof_linear</code>, <code>_instr.d_to_tof_linear</code>.

### <code>_instrument.calib_d_to_tof_quadratic</code> {#instrument-calib-d-to-tof-quadratic}

TOF calibration quadratic coefficient Dtt2 (us/A^2).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63417;</span> TOF quadratic. **Units:** µs/Å².

**Calculation role:** model-parameter. [Scientific explanation](calibration.md#eq-tof-calibration).

**Python:** <code>project.experiments[0].instrument.calib_d_to_tof_quadratic</code>.

**CIF names:** <code>_edi_instrument.calib_d_to_tof_quadratic</code>, <code>_instr.d_to_tof_quad</code>.

### <code>_instrument.calib_d_to_tof_reciprocal</code> {#instrument-calib-d-to-tof-reciprocal}

TOF calibration reciprocal (1/d) coefficient (us*A); round-tripped, held fixed in the free set.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63417;</span> TOF reciprocal. **Units:** µs·Å.

**Calculation role:** stored-only. [Scientific explanation](calibration.md#eq-tof-calibration).

**Python:** <code>project.experiments[0].instrument.calib_d_to_tof_reciprocal</code>.

**CIF names:** <code>_edi_instrument.calib_d_to_tof_reciprocal</code>, <code>_instr.d_to_tof_recip</code>.

### <code>_instrument.calib_twotheta_offset</code> {#instrument-calib-twotheta-offset}

CW zero-point offset in degrees 2theta, subtracted from the observed axis.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62263;</span> 2θ offset. **Units:** deg.

**Calculation role:** model-parameter. [Scientific explanation](calibration.md#eq-cwl-calibration).

**Python:** <code>project.experiments[0].instrument.calib_twotheta_offset</code>.

**CIF names:** <code>_pd_calib.2theta_offset</code>, <code>_pd_calib_2theta_offset</code>, <code>_instr.2theta_offset</code>.

### <code>_instrument.setup_wavelength</code> {#instrument-setup-wavelength}

Incident neutron wavelength in angstroms (single wavelength; the doublet tags are X-ray scope).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63417;</span> Wavelength. **Units:** Å.

**Calculation role:** model-parameter. [Scientific explanation](calibration.md#eq-cwl-calibration).

**Python:** <code>project.experiments[0].instrument.setup_wavelength</code>.

**CIF names:** <code>_diffrn_radiation_wavelength.value</code>, <code>_diffrn_radiation_wavelength</code>, <code>_diffrn_radiation_wavelength.wavelength</code>, <code>_instr.wavelength</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>doublet</code> | Wavelength 1 | Å | — |

### <code>_instrument.calib_sample_displacement</code> {#instrument-calib-sample-displacement}

CW sample-displacement line shift in degrees 2theta (FullProf SyCos): adds displacement*cos(2theta_B) to each reflection&#x27;s position.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62263;</span> Sample displacement. **Units:** deg.

**Calculation role:** model-parameter. [Scientific explanation](calibration.md#eq-line-shifts).

**Python:** <code>project.experiments[0].instrument.calib_sample_displacement</code>.

**CIF names:** <code>_edi_instrument.calib_sample_displacement</code>, <code>_instr.sample_displacement</code>.

### <code>_instrument.calib_sample_transparency</code> {#instrument-calib-sample-transparency}

CW sample-transparency line shift in degrees 2theta (FullProf SySin): adds transparency*sin(2theta_B) to each reflection&#x27;s position.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62263;</span> Sample transparency. **Units:** deg.

**Calculation role:** model-parameter. [Scientific explanation](calibration.md#eq-line-shifts).

**Python:** <code>project.experiments[0].instrument.calib_sample_transparency</code>.

**CIF names:** <code>_edi_instrument.calib_sample_transparency</code>, <code>_instr.sample_transparency</code>.

### <code>_instrument.setup_polarization_coefficient</code> {#instrument-setup-polarization-coefficient}

X-ray CW polarization coefficient K (FullProf Rpolarz): the intensity carries P = 1 - K + K cos^2(2theta_m) cos^2(2theta); 0 disables the correction.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> Polarization coefficient. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](corrections/intensity.md#eq-xray-polarization).

**Python:** <code>project.experiments[0].instrument.setup_polarization_coefficient</code>.

**CIF names:** <code>_edi_instrument.setup_polarization_coefficient</code>.

### <code>_instrument.setup_monochromator_twotheta</code> {#instrument-setup-monochromator-twotheta}

X-ray CW pre-specimen monochromator angle 2theta_m in degrees (FullProf stores Cthm = cos^2(2theta_m)); 0 means no monochromator.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> Monochromator 2θ. **Units:** deg.

**Calculation role:** model-parameter. [Scientific explanation](corrections/intensity.md#eq-xray-polarization).

**Python:** <code>project.experiments[0].instrument.setup_monochromator_twotheta</code>.

**CIF names:** <code>_edi_instrument.setup_monochromator_twotheta</code>.

### <code>_instrument.setup_wavelength_2</code> {#instrument-setup-wavelength-2}

X-ray CW second incident wavelength in angstroms (FullProf Lambda2, e.g. Cu K-alpha2); used when setup_wavelength_2_to_1_ratio is not 0.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63417;</span> Wavelength 2. **Units:** Å.

**Calculation role:** model-parameter. [Scientific explanation](corrections/intensity.md#wavelength-doublet).

**Python:** <code>project.experiments[0].instrument.setup_wavelength_2</code>.

**CIF names:** <code>_edi_instrument.setup_wavelength_2</code>.

### <code>_instrument.setup_wavelength_2_to_1_ratio</code> {#instrument-setup-wavelength-2-to-1-ratio}

X-ray CW intensity of the second wavelength relative to the first (FullProf Ratio); 0 means a single wavelength.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63417;</span> Intensity ratio 2/1. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](corrections/intensity.md#wavelength-doublet).

**Python:** <code>project.experiments[0].instrument.setup_wavelength_2_to_1_ratio</code>.

**CIF names:** <code>_edi_instrument.setup_wavelength_2_to_1_ratio</code>.

### <code>_instrument.name</code> {#instrument-name}

The instrument the pattern was measured on, or unknown.

**GUI:** instrument. **Units:** not applicable.

**Python:** <code>project.experiments[0].instrument.name</code>.

**CIF names:** <code>_diffrn_source.beamline</code>.

### <code>_instrument.facility</code> {#instrument-facility}

The facility the instrument belongs to, or unknown.

**GUI:** facility. **Units:** not applicable.

**Python:** <code>project.experiments[0].instrument.facility</code>.

**CIF names:** <code>_diffrn_source.facility</code>.

### <code>_instrument.setup_twotheta_bank</code> {#instrument-setup-twotheta-bank}

The scattering angle of the time-of-flight detector bank.

**GUI:** 2θ bank. **Units:** deg.

**Python:** <code>project.experiments[0].instrument.setup_twotheta_bank</code>.

**CIF names:** <code>_pd_meas.2theta_fixed</code>, <code>_pd_meas_2theta_fixed</code>, <code>_instr.2theta_bank</code>.

## Peak profile {#peak}

<code>_peak</code> — The shape and width of the diffraction peaks.

### <code>_peak.rise_alpha_0</code> {#peak-rise-alpha-0}

Back-to-back exponential rise-rate coefficient alpha_0 (rate, 1/us; no closed unit code).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> α₀. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-jorgensen).

**Python:** <code>project.experiments[0].peak.rise_alpha_0</code>.

**CIF names:** <code>_edi_peak.rise_alpha_0</code>, <code>_easydiffraction_peak.rise_alpha_0</code>.

### <code>_peak.rise_alpha_1</code> {#peak-rise-alpha-1}

Back-to-back exponential rise-rate coefficient alpha_1 (alpha(d)=alpha_0+alpha_1/d).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> α₁. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-jorgensen).

**Python:** <code>project.experiments[0].peak.rise_alpha_1</code>.

**CIF names:** <code>_edi_peak.rise_alpha_1</code>, <code>_easydiffraction_peak.rise_alpha_1</code>.

### <code>_peak.decay_beta_0</code> {#peak-decay-beta-0}

Back-to-back exponential decay-rate coefficient beta_0 (rate, 1/us; no closed unit code).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> β₀. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-jorgensen).

**Python:** <code>project.experiments[0].peak.decay_beta_0</code>.

**CIF names:** <code>_edi_peak.decay_beta_0</code>, <code>_easydiffraction_peak.decay_beta_0</code>.

### <code>_peak.decay_beta_1</code> {#peak-decay-beta-1}

Back-to-back exponential decay-rate coefficient beta_1 (beta(d)=beta_0+beta_1/d^4).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> β₁. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-jorgensen).

**Python:** <code>project.experiments[0].peak.decay_beta_1</code>.

**CIF names:** <code>_edi_peak.decay_beta_1</code>, <code>_easydiffraction_peak.decay_beta_1</code>.

### <code>_peak.broad_gauss_sigma_0</code> {#peak-broad-gauss-sigma-0}

Gaussian VARIANCE coefficient sigma_0^2 (variance domain; TCH consumes FWHM_G=sqrt(sigma^2)*sqrt(8 ln 2)).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> σ₀². **Units:** µs².

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-tof-widths).

**Python:** <code>project.experiments[0].peak.broad_gauss_sigma_0</code>.

**CIF names:** <code>_edi_peak.broad_gauss_sigma_0</code>, <code>_easydiffraction_peak.broad_gauss_sigma_0</code>.

### <code>_peak.broad_gauss_sigma_1</code> {#peak-broad-gauss-sigma-1}

Gaussian VARIANCE coefficient sigma_1^2 (d^2 term; variance domain).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> σ₁². **Units:** µs²/Å².

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-tof-widths).

**Python:** <code>project.experiments[0].peak.broad_gauss_sigma_1</code>.

**CIF names:** <code>_edi_peak.broad_gauss_sigma_1</code>, <code>_easydiffraction_peak.broad_gauss_sigma_1</code>.

### <code>_peak.broad_gauss_sigma_2</code> {#peak-broad-gauss-sigma-2}

Gaussian VARIANCE coefficient sigma_2^2 (d^4 term; us^2/A^4 not in closed vocab -&gt; none).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> σ₂². **Units:** µs²/Å⁴.

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-tof-widths).

**Python:** <code>project.experiments[0].peak.broad_gauss_sigma_2</code>.

**CIF names:** <code>_edi_peak.broad_gauss_sigma_2</code>, <code>_easydiffraction_peak.broad_gauss_sigma_2</code>.

### <code>_peak.broad_gauss_size</code> {#peak-broad-gauss-size}

Gaussian isotropic size broadening (variance contribution).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> size G. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-tof-widths).

**Python:** <code>project.experiments[0].peak.broad_gauss_size</code>.

**CIF names:** <code>_edi_peak.broad_gauss_size</code>.

### <code>_peak.broad_gauss_strain</code> {#peak-broad-gauss-strain}

Gaussian isotropic strain broadening (variance contribution).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> strain G. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-tof-widths).

**Python:** <code>project.experiments[0].peak.broad_gauss_strain</code>.

**CIF names:** <code>_edi_peak.broad_gauss_strain</code>.

### <code>_peak.broad_lorentz_gamma_0</code> {#peak-broad-lorentz-gamma-0}

Lorentzian FWHM coefficient gamma_0 (FWHM domain, H_L; consumed as FWHM directly, no sqrt(8 ln 2)).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> γ₀. **Units:** µs.

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-tof-widths).

**Python:** <code>project.experiments[0].peak.broad_lorentz_gamma_0</code>.

**CIF names:** <code>_edi_peak.broad_lorentz_gamma_0</code>, <code>_easydiffraction_peak.broad_lorentz_gamma_0</code>.

### <code>_peak.broad_lorentz_gamma_1</code> {#peak-broad-lorentz-gamma-1}

Lorentzian FWHM coefficient gamma_1 (d term; FWHM domain).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> γ₁. **Units:** µs/Å.

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-tof-widths).

**Python:** <code>project.experiments[0].peak.broad_lorentz_gamma_1</code>.

**CIF names:** <code>_edi_peak.broad_lorentz_gamma_1</code>, <code>_easydiffraction_peak.broad_lorentz_gamma_1</code>.

### <code>_peak.broad_lorentz_gamma_2</code> {#peak-broad-lorentz-gamma-2}

Lorentzian FWHM coefficient gamma_2 (d^2 term; FWHM domain).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> γ₂. **Units:** µs/Å².

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-tof-widths).

**Python:** <code>project.experiments[0].peak.broad_lorentz_gamma_2</code>.

**CIF names:** <code>_edi_peak.broad_lorentz_gamma_2</code>, <code>_easydiffraction_peak.broad_lorentz_gamma_2</code>.

### <code>_peak.broad_lorentz_size</code> {#peak-broad-lorentz-size}

Lorentzian isotropic size broadening (FWHM).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> size L. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-tof-widths).

**Python:** <code>project.experiments[0].peak.broad_lorentz_size</code>.

**CIF names:** <code>_edi_peak.broad_lorentz_size</code>.

### <code>_peak.broad_lorentz_strain</code> {#peak-broad-lorentz-strain}

Lorentzian isotropic strain broadening (FWHM).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> strain L. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/tof.md#eq-tof-widths).

**Python:** <code>project.experiments[0].peak.broad_lorentz_strain</code>.

**CIF names:** <code>_edi_peak.broad_lorentz_strain</code>.

### <code>_peak.broad_gauss_u</code> {#peak-broad-gauss-u}

Caglioti Gaussian FWHM coefficient U (tan^2(theta) term; H_G^2 in deg^2).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> U. **Units:** deg².

**Calculation role:** model-parameter. [Scientific explanation](profiles/cw.md#eq-tch).

**Python:** <code>project.experiments[0].peak.broad_gauss_u</code>.

**CIF names:** <code>_edi_peak.broad_gauss_u</code>, <code>_easydiffraction_peak.broad_gauss_u</code>.

### <code>_peak.broad_gauss_v</code> {#peak-broad-gauss-v}

Caglioti Gaussian FWHM coefficient V (tan(theta) term; H_G^2 in deg^2).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> V. **Units:** deg².

**Calculation role:** model-parameter. [Scientific explanation](profiles/cw.md#eq-tch).

**Python:** <code>project.experiments[0].peak.broad_gauss_v</code>.

**CIF names:** <code>_edi_peak.broad_gauss_v</code>, <code>_easydiffraction_peak.broad_gauss_v</code>.

### <code>_peak.broad_gauss_w</code> {#peak-broad-gauss-w}

Caglioti Gaussian FWHM coefficient W (constant term; H_G^2 in deg^2).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> W. **Units:** deg².

**Calculation role:** model-parameter. [Scientific explanation](profiles/cw.md#eq-tch).

**Python:** <code>project.experiments[0].peak.broad_gauss_w</code>.

**CIF names:** <code>_edi_peak.broad_gauss_w</code>, <code>_easydiffraction_peak.broad_gauss_w</code>.

### <code>_peak.broad_lorentz_x</code> {#peak-broad-lorentz-x}

Lorentzian FWHM coefficient X, strain-like (tan(theta) term; H_L in deg).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> X. **Units:** deg.

**Calculation role:** model-parameter. [Scientific explanation](profiles/cw.md#eq-tch).

**Python:** <code>project.experiments[0].peak.broad_lorentz_x</code>.

**CIF names:** <code>_edi_peak.broad_lorentz_x</code>, <code>_easydiffraction_peak.broad_lorentz_x</code>.

### <code>_peak.broad_lorentz_y</code> {#peak-broad-lorentz-y}

Lorentzian FWHM coefficient Y, size-like (1/cos(theta) term; H_L in deg).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> Y. **Units:** deg.

**Calculation role:** model-parameter. [Scientific explanation](profiles/cw.md#eq-tch).

**Python:** <code>project.experiments[0].peak.broad_lorentz_y</code>.

**CIF names:** <code>_edi_peak.broad_lorentz_y</code>, <code>_easydiffraction_peak.broad_lorentz_y</code>.

### <code>_peak.mixing_eta_0</code> {#peak-mixing-eta-0}

Pseudo-Voigt mixing at 2theta = 0: eta = eta_0 + eta_1 2theta (FullProf Eta0).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> Eta0. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/cw.md#eq-caglioti).

**Python:** <code>project.experiments[0].peak.mixing_eta_0</code>.

**CIF names:** <code>_edi_peak.mixing_eta_0</code>, <code>_easydiffraction_peak.mixing_eta_0</code>.

### <code>_peak.mixing_eta_1</code> {#peak-mixing-eta-1}

Pseudo-Voigt mixing slope per degree 2theta: eta = eta_0 + eta_1 2theta (FullProf X of Npr 5).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> Eta1. **Units:** 1/deg.

**Calculation role:** model-parameter. [Scientific explanation](profiles/cw.md#eq-caglioti).

**Python:** <code>project.experiments[0].peak.mixing_eta_1</code>.

**CIF names:** <code>_edi_peak.mixing_eta_1</code>, <code>_easydiffraction_peak.mixing_eta_1</code>.

### <code>_peak.asym_fcj_1</code> {#peak-asym-fcj-1}

Finger-Cox-Jephcoat asymmetry parameter 1: S/L, half the sample height over the diffractometer radius.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> S/L. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/cw.md#eq-fcj).

**Python:** <code>project.experiments[0].peak.asym_fcj_1</code>.

**CIF names:** <code>_edi_peak.asym_fcj_1</code>, <code>_easydiffraction_peak.asym_fcj_1</code>.

### <code>_peak.asym_fcj_2</code> {#peak-asym-fcj-2}

Finger-Cox-Jephcoat asymmetry parameter 2: D/L, half the detector height over the diffractometer radius.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> D/L. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/cw.md#eq-fcj).

**Python:** <code>project.experiments[0].peak.asym_fcj_2</code>.

**CIF names:** <code>_edi_peak.asym_fcj_2</code>, <code>_easydiffraction_peak.asym_fcj_2</code>.

### <code>_peak.asym_beba_a0</code> {#peak-asym-beba-a0}

Berar-Baldinozzi asymmetry coefficient A0 (Fa/tan theta).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> A₀. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/cw.md#eq-berar-baldinozzi).

**Python:** <code>project.experiments[0].peak.asym_beba_a0</code>.

**CIF names:** <code>_edi_peak.asym_beba_a0</code>, <code>_easydiffraction_peak.asym_beba_a0</code>.

### <code>_peak.asym_beba_b0</code> {#peak-asym-beba-b0}

Berar-Baldinozzi asymmetry coefficient B0 (Fb/tan theta).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> B₀. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/cw.md#eq-berar-baldinozzi).

**Python:** <code>project.experiments[0].peak.asym_beba_b0</code>.

**CIF names:** <code>_edi_peak.asym_beba_b0</code>, <code>_easydiffraction_peak.asym_beba_b0</code>.

### <code>_peak.asym_beba_a1</code> {#peak-asym-beba-a1}

Berar-Baldinozzi asymmetry coefficient A1 (Fa/tan 2theta).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> A₁. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/cw.md#eq-berar-baldinozzi).

**Python:** <code>project.experiments[0].peak.asym_beba_a1</code>.

**CIF names:** <code>_edi_peak.asym_beba_a1</code>, <code>_easydiffraction_peak.asym_beba_a1</code>.

### <code>_peak.asym_beba_b1</code> {#peak-asym-beba-b1}

Berar-Baldinozzi asymmetry coefficient B1 (Fb/tan 2theta).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> B₁. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](profiles/cw.md#eq-berar-baldinozzi).

**Python:** <code>project.experiments[0].peak.asym_beba_b1</code>.

**CIF names:** <code>_edi_peak.asym_beba_b1</code>, <code>_easydiffraction_peak.asym_beba_b1</code>.

### <code>_peak.asym_beba_limit</code> {#peak-asym-beba-limit}

Berar-Baldinozzi limit angle (deg 2theta): reflections at or above it get no asymmetry correction (FullProf AsyLim); default 180.

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#63007;</span> <span class="ed-reference-icon" aria-hidden="true">&#62741;</span> AsyLim. **Units:** deg.

**Calculation role:** fixed. [Scientific explanation](profiles/cw.md#eq-berar-baldinozzi).

**Python:** <code>project.experiments[0].peak.asym_beba_limit</code>.

**CIF names:** <code>_edi_peak.asym_beba_limit</code>, <code>_easydiffraction_peak.asym_beba_limit</code>.

### <code>_peak.type</code> {#peak-type}

The peak-profile function.

**GUI:** profile. **Units:** not applicable.

**Python:** <code>project.experiments[0].peak.type</code>.

**CIF names:** <code>_edi_peak.type</code>, <code>_easydiffraction_peak.type</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>cwl-gaussian</code> | Gaussian | A Gaussian peak with the Caglioti width. |
| <code>cwl-lorentzian</code> | Lorentzian | A Lorentzian peak. |
| <code>cwl-pseudo-voigt</code> | Pseudo-Voigt | A pseudo-Voigt peak with a refinable mixing. |
| <code>cwl-pseudo-voigt-berar-baldinozzi</code> | Pseudo-Voigt + Bérar-Baldinozzi asymmetry | A pseudo-Voigt peak with the Bérar-Baldinozzi asymmetry correction. |
| <code>cwl-tch-pseudo-voigt</code> | Thompson-Cox-Hastings pseudo-Voigt (TCH) | The Thompson-Cox-Hastings pseudo-Voigt peak. |
| <code>cwl-tch-pseudo-voigt-fcj</code> | Thompson-Cox-Hastings pseudo-Voigt (TCH) + Finger-Cox-Jephcoat asymmetry (FCJ) | The TCH peak with the Finger-Cox-Jephcoat axial-divergence asymmetry. |
| <code>tof-jorgensen</code> | Jorgensen | The back-to-back exponentials convolved with a Gaussian. |
| <code>tof-jorgensen-von-dreele</code> | Jorgensen-Von Dreele | The back-to-back exponentials convolved with a pseudo-Voigt. |
| <code>tof-pseudo-voigt</code> | Pseudo-Voigt | A time-of-flight pseudo-Voigt peak. |

### <code>_peak.cutoff_fwhm</code> {#peak-cutoff-fwhm}

How far from its centre a peak is calculated, in units of its width.

**GUI:** cutoff (FWHM). **Units:** not applicable.

**Python:** <code>project.experiments[0].peak.cutoff_fwhm</code>.

**CIF names:** <code>_edi_peak.cutoff_fwhm</code>, <code>_easydiffraction_peak.cutoff_fwhm</code>.

## Excluded region {#excluded-region}

<code>_excluded_region</code> — Ranges of the pattern left out of the fit.

### <code>_excluded_region.id</code> {#excluded-region-id}

The name of the excluded region.

**GUI:** id. **Units:** not applicable.

**CIF names:** <code>_edi_excluded_region.id</code>, <code>_easydiffraction_excluded_region.id</code>.

### <code>_excluded_region.start</code> {#excluded-region-start}

Where the excluded region starts.

**GUI:** start. **Units:** deg.

**CIF names:** <code>_edi_excluded_region.start</code>, <code>_easydiffraction_excluded_region.start</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>constant wavelength</code> | start | deg | — |
| <code>time-of-flight</code> | start | µs | — |

### <code>_excluded_region.end</code> {#excluded-region-end}

Where the excluded region ends.

**GUI:** end. **Units:** deg.

**CIF names:** <code>_edi_excluded_region.end</code>, <code>_easydiffraction_excluded_region.end</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>constant wavelength</code> | end | deg | — |
| <code>time-of-flight</code> | end | µs | — |

## Extinction {#extinction}

<code>_extinction</code> — A single crystal&#x27;s extinction correction: its type, mosaic distribution and parameters.

### <code>_extinction.domain_radius</code> {#extinction-domain-radius}

Becker-Coppens domain (mosaic block) radius r (micrometres; extinction types II and mixed; single crystal; a fit parameter).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> Domain radius. **Units:** μm.

**Calculation role:** model-parameter. [Scientific explanation](corrections/extinction.md#extinction-units).

**CIF names:** <code>_edi_extinction.domain_radius</code>.

### <code>_extinction.mosaic_spread</code> {#extinction-mosaic-spread}

Becker-Coppens mosaic spread g of the crystal, the inverse width of its mosaic distribution (larger is narrower; radians to the minus one; extinction types I and mixed; single crystal; a fit parameter).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> Mosaic spread. **Units:** rad⁻¹.

**Calculation role:** model-parameter. [Scientific explanation](corrections/extinction.md#extinction-units).

**CIF names:** <code>_edi_extinction.mosaic_spread</code>.

### <code>_extinction.crystal_radius</code> {#extinction-crystal-radius}

Radius of the crystal taken as a sphere, which sets each reflection&#x27;s mean path length through it for the Becker-Coppens secondary extinction (millimetres, as _exptl_crystal.size_rad; every Becker-Coppens type; single crystal; a descriptor, never fitted).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> Crystal radius. **Units:** mm.

**Calculation role:** descriptor. [Scientific explanation](corrections/extinction.md#extinction-units).

**CIF names:** <code>_exptl_crystal.size_rad</code>, <code>_exptl_crystal_size_rad</code>.

### <code>_extinction.coefficient</code> {#extinction-coefficient}

Larson&#x27;s empirical extinction coefficient x, as SHELXL&#x27;s EXTI: F2calc is multiplied by [1 + 0.001 x F2calc lambda^3 / sin 2theta]^(-1/2) (extinction type larson-isotropic; single crystal; a fit parameter).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> Extinction coefficient. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](corrections/extinction.md#eq-larson).

**CIF names:** <code>_edi_extinction.coefficient</code>.

### <code>_extinction.coefficient_11</code> {#extinction-coefficient-11}

The term of h² in Larson&#x27;s anisotropic extinction tensor x_aniso = x11 h^2 + x22 k^2 + x33 l^2 + x12 hk + x13 hl + x23 kl, which takes the place of 4 x (sin theta/lambda)^2 (FullProf&#x27;s Ext1; extinction type larson-anisotropic; single crystal; a fit parameter).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> x11. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](corrections/extinction.md#eq-larson).

**CIF names:** <code>_edi_extinction.coefficient_11</code>.

### <code>_extinction.coefficient_22</code> {#extinction-coefficient-22}

The term of k² in Larson&#x27;s anisotropic extinction tensor x_aniso = x11 h^2 + x22 k^2 + x33 l^2 + x12 hk + x13 hl + x23 kl, which takes the place of 4 x (sin theta/lambda)^2 (FullProf&#x27;s Ext2; extinction type larson-anisotropic; single crystal; a fit parameter).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> x22. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](corrections/extinction.md#eq-larson).

**CIF names:** <code>_edi_extinction.coefficient_22</code>.

### <code>_extinction.coefficient_33</code> {#extinction-coefficient-33}

The term of l² in Larson&#x27;s anisotropic extinction tensor x_aniso = x11 h^2 + x22 k^2 + x33 l^2 + x12 hk + x13 hl + x23 kl, which takes the place of 4 x (sin theta/lambda)^2 (FullProf&#x27;s Ext3; extinction type larson-anisotropic; single crystal; a fit parameter).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> x33. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](corrections/extinction.md#eq-larson).

**CIF names:** <code>_edi_extinction.coefficient_33</code>.

### <code>_extinction.coefficient_12</code> {#extinction-coefficient-12}

The term of hk in Larson&#x27;s anisotropic extinction tensor x_aniso = x11 h^2 + x22 k^2 + x33 l^2 + x12 hk + x13 hl + x23 kl, which takes the place of 4 x (sin theta/lambda)^2 (FullProf&#x27;s Ext4; extinction type larson-anisotropic; single crystal; a fit parameter).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> x12. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](corrections/extinction.md#eq-larson).

**CIF names:** <code>_edi_extinction.coefficient_12</code>.

### <code>_extinction.coefficient_13</code> {#extinction-coefficient-13}

The term of hl in Larson&#x27;s anisotropic extinction tensor x_aniso = x11 h^2 + x22 k^2 + x33 l^2 + x12 hk + x13 hl + x23 kl, which takes the place of 4 x (sin theta/lambda)^2 (FullProf&#x27;s Ext5; extinction type larson-anisotropic; single crystal; a fit parameter).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> x13. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](corrections/extinction.md#eq-larson).

**CIF names:** <code>_edi_extinction.coefficient_13</code>.

### <code>_extinction.coefficient_23</code> {#extinction-coefficient-23}

The term of kl in Larson&#x27;s anisotropic extinction tensor x_aniso = x11 h^2 + x22 k^2 + x33 l^2 + x12 hk + x13 hl + x23 kl, which takes the place of 4 x (sin theta/lambda)^2 (FullProf&#x27;s Ext6; extinction type larson-anisotropic; single crystal; a fit parameter).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62373;</span> x23. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](corrections/extinction.md#eq-larson).

**CIF names:** <code>_edi_extinction.coefficient_23</code>.

### <code>_extinction.type</code> {#extinction-type}

The extinction correction of a single crystal.

**GUI:** type. **Units:** not applicable.

**CIF names:** <code>_edi_extinction.type</code>, <code>_easydiffraction_extinction.type</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>none</code> | None | No extinction correction. |
| <code>becker-coppens-type-1</code> | Isotropic Becker-Coppens type I | Becker-Coppens secondary extinction set by the mosaic spread. |
| <code>becker-coppens-type-2</code> | Isotropic Becker-Coppens type II | Becker-Coppens secondary extinction set by the domain radius. |
| <code>becker-coppens-mixed</code> | Isotropic Becker-Coppens mixed | Becker-Coppens secondary extinction set by both the mosaic spread and the domain radius. |
| <code>larson-isotropic</code> | Isotropic Larson | Larson&#x27;s empirical coefficient, as SHELXL&#x27;s EXTI. |
| <code>larson-anisotropic</code> | Anisotropic Larson | Larson&#x27;s anisotropic extinction tensor. |

### <code>_extinction.mosaic_distribution</code> {#extinction-mosaic-distribution}

The shape of a Becker-Coppens crystal&#x27;s mosaic distribution.

**GUI:** mosaic distribution. **Units:** not applicable.

**CIF names:** <code>_edi_extinction.mosaic_distribution</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>gaussian</code> | Gaussian | A Gaussian mosaic distribution. |
| <code>lorentzian</code> | Lorentzian | A Lorentzian mosaic distribution. |

## Linked structure {#linked-structure}

<code>_linked_structure</code> — The structures that contribute to the pattern, each with its scale.

### <code>_linked_structure.scale</code> {#linked-structure-scale}

Scale factor of one linked structure&#x27;s (phase&#x27;s) pattern, the overall pattern scale when there is one structure (dimensionless; linear).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#62973;</span> <span class="ed-reference-icon" aria-hidden="true">&#62614;</span> scale. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](diffraction.md#phase-fractions).

**Python:** <code>project.experiments[0].linked_structures[0].scale</code>.

**CIF names:** <code>_edi_linked_structure.scale</code>, <code>_pd_phase_block.scale</code>, <code>_easydiffraction_sc_crystal_block.scale</code>, <code>_sc_crystal_block.scale</code>.

**Earlier Edi spellings accepted on import:** <code>_scale.value</code>.

### <code>_linked_structure.structure_id</code> {#linked-structure-structure-id}

The structure that contributes to the pattern.

**GUI:** structure. **Units:** not applicable.

**Python:** <code>project.experiments[0].linked_structures[0].structure_id</code>.

**CIF names:** <code>_pd_phase_block.id</code>, <code>_pd_phase_block_id</code>, <code>_easydiffraction_sc_crystal_block.id</code>, <code>_sc_crystal_block.id</code>.

### <code>_linked_structure.enabled</code> {#linked-structure-enabled}

Whether the structure contributes to the pattern.

**GUI:** enabled. **Units:** not applicable.

**Python:** <code>project.experiments[0].linked_structures[0].enabled</code>.

**CIF names:** <code>_edi_linked_structure.enabled</code>.

### <code>_linked_structure.weight_fraction</code> {#linked-structure-weight-fraction}

The structure&#x27;s weight fraction in the sample, from the scales (Hill and Howard); computed, never edited.

**GUI:** weight fraction. **Units:** not applicable.

**CIF names:** <code>_edi_linked_structure.weight_fraction</code>.

## Absorption {#absorption}

<code>_absorption</code> — The absorption correction.

### <code>_absorption.abscor1</code> {#absorption-abscor1}

TOF sample absorption coefficient ABSCOR1 (muR = ABSCOR1 * lambda; refinable).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#61507;</span> ABSCOR1. **Units:** Å⁻¹.

**Calculation role:** model-parameter. [Scientific explanation](corrections/absorption.md#eq-hewat).

**Python:** <code>project.experiments[0].absorption.abscor1</code>.

**CIF names:** <code>_edi_absorption.abscor1</code>.

### <code>_absorption.abscor2</code> {#absorption-abscor2}

TOF sample absorption lambda-power ABSCOR2 (round-tripped, held fixed; freeing it is a hard error).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#61507;</span> ABSCOR2. **Units:** not applicable.

**Calculation role:** stored-only. [Scientific explanation](corrections/absorption.md#eq-hewat).

**Python:** <code>project.experiments[0].absorption.abscor2</code>.

**CIF names:** <code>_edi_absorption.abscor2</code>.

### <code>_absorption.mu_r</code> {#absorption-mu-r}

CW cylinder sample absorption mu*R (mu the linear absorption coefficient, R the cylinder RADIUS; evaluated at each reflection&#x27;s Bragg theta; refinable; C13-T5).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#61507;</span> μR. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](corrections/absorption.md#eq-hewat).

**Python:** <code>project.experiments[0].absorption.mu_r</code>.

**CIF names:** <code>_edi_absorption.mu_r</code>, <code>_easydiffraction_absorption.mu_r</code>.

### <code>_absorption.type</code> {#absorption-type}

The absorption correction.

**GUI:** type. **Units:** not applicable.

**Python:** <code>project.experiments[0].absorption.type</code>.

**CIF names:** <code>_edi_absorption.type</code>, <code>_easydiffraction_absorption.type</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>none</code> | None | No absorption correction. |
| <code>cylinder-hewat</code> | Cylinder (Hewat) | The Hewat (1979) polynomial for a cylindrical sample. |
| <code>cylinder-lobanov</code> | Cylinder (Lobanov) | The Lobanov and Alte da Veiga (1998) fit for a cylindrical sample. |

## Preferred orientation {#preferred-orientation}

<code>_preferred_orientation</code> — The March-Dollase preferred-orientation correction per structure.

### <code>_preferred_orientation.march_r</code> {#preferred-orientation-march-r}

March-Dollase coefficient r (FullProf Pref1, IUCr _pd_pref_orient_March_Dollase.r; 1 = no texture, &lt;1 platy, &gt;1 needle; must be &gt; 0; a fit parameter; C13-T4).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#61774;</span> r. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](corrections/orientation.md#eq-march-dollase).

**CIF names:** <code>_pd_pref_orient_March_Dollase.r</code>, <code>_pref_orient.march_r</code>.

### <code>_preferred_orientation.march_random_fract</code> {#preferred-orientation-march-random-fract}

Random (untextured) fraction mixed with the March-Dollase term (FullProf Pref2; a fit parameter; C13-T4).

**GUI:** <span class="ed-reference-icon" aria-hidden="true">&#62992;</span> <span class="ed-reference-icon" aria-hidden="true">&#61774;</span> f rand. **Units:** not applicable.

**Calculation role:** model-parameter. [Scientific explanation](corrections/orientation.md#eq-march-dollase).

**CIF names:** <code>_edi_preferred_orientation.march_random_fract</code>, <code>_easydiffraction_pref_orient.march_random_fract</code>, <code>_pref_orient.march_random_fract</code>.

### <code>_preferred_orientation.structure_id</code> {#preferred-orientation-structure-id}

The structure the correction applies to.

**GUI:** structure. **Units:** not applicable.

**CIF names:** <code>_pd_pref_orient_March_Dollase.phase_id</code>, <code>_pref_orient.phase_id</code>.

### <code>_preferred_orientation.index_h</code> {#preferred-orientation-index-h}

The h index of the preferred-orientation direction.

**GUI:** h. **Units:** not applicable.

**CIF names:** <code>_pd_pref_orient_March_Dollase.index_h</code>, <code>_pref_orient.index_h</code>.

### <code>_preferred_orientation.index_k</code> {#preferred-orientation-index-k}

The k index of the preferred-orientation direction.

**GUI:** k. **Units:** not applicable.

**CIF names:** <code>_pd_pref_orient_March_Dollase.index_k</code>, <code>_pref_orient.index_k</code>.

### <code>_preferred_orientation.index_l</code> {#preferred-orientation-index-l}

The l index of the preferred-orientation direction.

**GUI:** l. **Units:** not applicable.

**CIF names:** <code>_pd_pref_orient_March_Dollase.index_l</code>, <code>_pref_orient.index_l</code>.

## Observed reflections {#reflns}

<code>_reflns</code> — Which of a single crystal&#x27;s reflections count as observed, for its counts and R factors.

### <code>_reflns.threshold_sigma</code> {#reflns-threshold-sigma}

The multiple n of its su above which a single crystal&#x27;s reflection counts as observed; 2 when absent.

**GUI:** observed above (su). **Units:** not applicable.

**CIF names:** <code>_edi_reflns.threshold_sigma</code>.

### <code>_reflns.threshold_basis</code> {#reflns-threshold-basis}

Whether the observed threshold is on the intensity or the amplitude; the intensity when absent.

**GUI:** on. **Units:** not applicable.

**CIF names:** <code>_edi_reflns.threshold_basis</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>intensity</code> | I | The intensity: I &gt; n u(I). |
| <code>amplitude</code> | F | The amplitude: F &gt; n u(F). |

### <code>_reflns.threshold_expression</code> {#reflns-threshold-expression}

The observed threshold as CIF writes it, such as I&gt;2u(I); a save writes it beside the counts and R factors it gives.

**GUI:** threshold. **Units:** not applicable.

**CIF names:** <code>_reflns.threshold_expression</code>, <code>_reflns_threshold_expression</code>, <code>_reflns_observed_criterion</code>, <code>_reflns.observed_criterion</code>.

## Scattering source {#scattering-source}

<code>_scattering_source</code> — The published tables the scattering factors and lengths come from.

### <code>_scattering_source.xray_form_factor</code> {#scattering-source-xray-form-factor}

The published table the X-ray atomic form factors come from.

**GUI:** X-ray form factors. **Units:** not applicable.

**CIF names:** <code>_edi_scattering_source.xray_form_factor</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>wk1995</code> | Waasmaier &amp; Kirfel (1995) | Waasmaier and Kirfel, Acta Cryst. A51 (1995) 416. |
| <code>it1992</code> | International Tables C (1992) | International Tables for Crystallography, Vol. C (1992). |

### <code>_scattering_source.xray_dispersion</code> {#scattering-source-xray-dispersion}

The published table the anomalous dispersion corrections come from.

**GUI:** X-ray dispersion. **Units:** not applicable.

**CIF names:** <code>_edi_scattering_source.xray_dispersion</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>cromer-liberman</code> | Cromer &amp; Liberman | Cromer and Liberman, calculated for the wavelength. |
| <code>sasaki1989</code> | Sasaki (1989) | Sasaki, KEK Report 88-14 (1989). |
| <code>it1992</code> | International Tables C (1992) | International Tables for Crystallography, Vol. C (1992). |
| <code>none</code> | None | No anomalous dispersion correction. |

### <code>_scattering_source.neutron_scattering_length</code> {#scattering-source-neutron-scattering-length}

The published table the neutron scattering lengths come from.

**GUI:** neutron scattering lengths. **Units:** not applicable.

**CIF names:** <code>_edi_scattering_source.neutron_scattering_length</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>rauch2003ext</code> | Rauch &amp; Waschkowski (2003) | Rauch and Waschkowski (2003), extended with the isotopes it lacks. |
| <code>sears1992</code> | Sears (1992) | Sears, Neutron News 3 (1992) 26. |

## Calculator {#calculator}

<code>_calculator</code> — The calculation engine an experiment names.

### <code>_calculator.type</code> {#calculator-type}

The calculation engine.

**GUI:** calculator. **Units:** not applicable.

**CIF names:** <code>_edi_calculator.type</code>, <code>_easydiffraction_calculator.type</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>crysta</code> | crysta | The crysta engine. |

## Minimizer {#minimizer}

<code>_minimizer</code> — The minimizer and its settings.

### <code>_minimizer.type</code> {#minimizer-type}

The minimizer.

**GUI:** minimizer. **Units:** not applicable.

**CIF names:** <code>_edi_minimizer.type</code>, <code>_easydiffraction_minimizer.type</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>crysta</code> | crysta | crysta&#x27;s own least-squares minimizer. |

### <code>_minimizer.max_iterations</code> {#minimizer-max-iterations}

The most iterations a fit may take.

**GUI:** max iterations. **Units:** not applicable.

**CIF names:** <code>_edi_minimizer.max_iterations</code>, <code>_easydiffraction_minimizer.max_iterations</code>.

### <code>_minimizer.descent</code> {#minimizer-descent}

The descent strategy of the minimizer.

**GUI:** descent. **Units:** not applicable.

**Python:** <code>project.descent</code>.

**CIF names:** <code>_edi_minimizer.descent</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>ladder</code> | Ladder | The default descent. |
| <code>fast_descent</code> | Fast descent | A faster descent that takes fewer steps. |
| <code>fast_descent_linear_snap</code> | Fast descent with linear snap | The fast descent, solving the linear parameters exactly at each step. |
| <code>fast_descent_guarded_linear_snap</code> | Fast descent with guarded linear snap | The fast descent, keeping a linear snap only when it lowers χ². |
| <code>multistart_prune</code> | Multi-start with pruning | Several starts, the worse ones dropped as the fit goes on. |

### <code>_minimizer.chi_square_tolerance</code> {#minimizer-chi-square-tolerance}

The relative change of χ² at which a fit stops.

**GUI:** tolerance. **Units:** not applicable.

**CIF names:** <code>_edi_minimizer.chi_square_tolerance</code>.

## Fitting mode {#fitting-mode}

<code>_fitting_mode</code> — How the experiments of a project are fitted.

### <code>_fitting_mode.type</code> {#fitting-mode-type}

How the experiments of the project are fitted.

**GUI:** mode. **Units:** not applicable.

**Python:** <code>project.fitting_mode</code>.

**CIF names:** <code>_edi_fitting_mode.type</code>, <code>_easydiffraction_fitting_mode.type</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>single</code> | Single experiment | The one experiment is fitted on its own. |
| <code>joint</code> | Joint: all experiments at once | All experiments are fitted together. |
| <code>sequential</code> | Sequential: each from the previous | Each data file is fitted, starting from the previous result. |
| <code>independent</code> | Independent: each from the same start | Each data file is fitted from the same start. |

## Fitted reflections {#refine-ls}

<code>_refine_ls</code> — Which of a single crystal&#x27;s reflections a fit uses.

### <code>_refine_ls.threshold_sigma</code> {#refine-ls-threshold-sigma}

The multiple n of its su above which a single crystal&#x27;s reflection is fitted; every reflection when absent.

**GUI:** fit reflections above (su). **Units:** not applicable.

**CIF names:** <code>_edi_refine_ls.threshold_sigma</code>.

## Alias {#alias}

<code>_alias</code> — Short names for parameters, used in constraints.

### <code>_alias.id</code> {#alias-id}

The short name.

**GUI:** alias. **Units:** not applicable.

**CIF names:** <code>_edi_alias.id</code>, <code>_easydiffraction_alias.id</code>, <code>_alias.label</code>.

### <code>_alias.parameter_unique_name</code> {#alias-parameter-unique-name}

The parameter the short name stands for.

**GUI:** parameter. **Units:** not applicable.

**CIF names:** <code>_edi_alias.parameter_unique_name</code>, <code>_easydiffraction_alias.parameter_unique_name</code>, <code>_alias.param_unique_name</code>.

## Constraint {#constraint}

<code>_constraint</code> — Expressions that compute a parameter from others.

### <code>_constraint.id</code> {#constraint-id}

The name of the constraint.

**GUI:** id. **Units:** not applicable.

**CIF names:** <code>_edi_constraint.id</code>, <code>_easydiffraction_constraint.id</code>.

### <code>_constraint.expression</code> {#constraint-expression}

The expression, such as occ_Ba = 1 - occ_La.

**GUI:** expression. **Units:** not applicable.

**CIF names:** <code>_edi_constraint.expression</code>, <code>_easydiffraction_constraint.expression</code>.

### <code>_constraint.enabled</code> {#constraint-enabled}

Whether the constraint applies.

**GUI:** enabled. **Units:** not applicable.

**CIF names:** <code>_edi_constraint.enabled</code>.

## Joint-fit weights {#joint-fit}

<code>_joint_fit</code> — Each experiment&#x27;s weight in a joint fit.

### <code>_joint_fit.weight</code> {#joint-fit-weight}

The experiment&#x27;s weight in a joint fit.

**GUI:** weight. **Units:** not applicable.

**Python:** <code>project.experiments[0].dataset_weight</code>.

**CIF names:** <code>_edi_joint_fit.weight</code>, <code>_easydiffraction_joint_fit.weight</code>.

## Sequential fit {#sequential-fit}

<code>_sequential_fit</code> — Which data files a sequential fit runs over.

### <code>_sequential_fit.data_dir</code> {#sequential-fit-data-dir}

The folder of the data files.

**GUI:** data directory. **Units:** not applicable.

**CIF names:** <code>_edi_sequential_fit.data_dir</code>, <code>_easydiffraction_sequential_fit.data_dir</code>.

### <code>_sequential_fit.file_pattern</code> {#sequential-fit-file-pattern}

Which files of the folder are fitted.

**GUI:** files. **Units:** not applicable.

**CIF names:** <code>_edi_sequential_fit.file_pattern</code>, <code>_easydiffraction_sequential_fit.file_pattern</code>.

### <code>_sequential_fit.reverse</code> {#sequential-fit-reverse}

Whether the files are fitted in reverse order.

**GUI:** reverse. **Units:** not applicable.

**CIF names:** <code>_edi_sequential_fit.reverse</code>, <code>_easydiffraction_sequential_fit.reverse</code>.

### <code>_sequential_fit.template_file</code> {#sequential-fit-template-file}

The experiment every file is fitted with.

**GUI:** template. **Units:** not applicable.

**CIF names:** <code>_edi_sequential_fit.template_file</code>.

## Scan extraction rule {#sequential-fit-extract}

<code>_sequential_fit_extract</code> — Rules that read a value, such as a temperature, from each data file name.

### <code>_sequential_fit_extract.id</code> {#sequential-fit-extract-id}

The name of the value read from each file name.

**GUI:** id. **Units:** not applicable.

**CIF names:** <code>_edi_sequential_fit_extract.id</code>, <code>_easydiffraction_sequential_fit_extract.id</code>.

### <code>_sequential_fit_extract.target</code> {#sequential-fit-extract-target}

What the value is stored as.

**GUI:** target. **Units:** not applicable.

**CIF names:** <code>_edi_sequential_fit_extract.target</code>, <code>_easydiffraction_sequential_fit_extract.target</code>.

### <code>_sequential_fit_extract.pattern</code> {#sequential-fit-extract-pattern}

The pattern that finds the value in the file name.

**GUI:** pattern. **Units:** not applicable.

**CIF names:** <code>_edi_sequential_fit_extract.pattern</code>, <code>_easydiffraction_sequential_fit_extract.pattern</code>.

### <code>_sequential_fit_extract.required</code> {#sequential-fit-extract-required}

Whether a file whose name does not match fails.

**GUI:** required. **Units:** not applicable.

**CIF names:** <code>_edi_sequential_fit_extract.required</code>, <code>_easydiffraction_sequential_fit_extract.required</code>.

## File header {#edi}

<code>_edi</code> — The header every .edi file starts with.

### <code>_edi.schema_version</code> {#edi-schema-version}

The version of the .edi format the file follows.

**GUI:** schema version. **Units:** not applicable.

**CIF names:** <code>_edi_edi.schema_version</code>.

## Saved report {#report-file}

<code>_report_file</code> — The report files saved from this project.

### <code>_report_file.format</code> {#report-file-format}

The format of a saved report file.

**GUI:** format. **Units:** not applicable.

**CIF names:** <code>_edi_report_file.format</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>html</code> | HTML | An HTML page with interactive charts. |
| <code>pdf</code> | PDF | A PDF document on A4 pages. |
| <code>cif</code> | CIF | A CIF file with the official CIF names. |

### <code>_report_file.name</code> {#report-file-name}

The saved report file, in the reports folder.

**GUI:** file. **Units:** not applicable.

**CIF names:** <code>_edi_report_file.name</code>.

### <code>_report_file.saved</code> {#report-file-saved}

When the report file was saved.

**GUI:** saved. **Units:** not applicable.

**CIF names:** <code>_edi_report_file.saved</code>.

### <code>_report_file.project_last_modified</code> {#report-file-project-last-modified}

When the project was last saved before the report was.

**GUI:** project saved. **Units:** not applicable.

**CIF names:** <code>_edi_report_file.project_last_modified</code>.

### <code>_report_file.digest</code> {#report-file-digest}

A checksum of the saved report file.

**GUI:** digest. **Units:** not applicable.

**CIF names:** <code>_edi_report_file.digest</code>.

## Symmetry operator {#space-group-symop}

<code>_space_group_symop</code> — The space group&#x27;s symmetry operators, in the order a symmetry code refers to them.

### <code>_space_group_symop.operation_xyz</code> {#space-group-symop-operation-xyz}

A symmetry operator as x, y, z expressions.

**GUI:** operation. **Units:** not applicable.

**CIF names:** <code>_space_group_symop.operation_xyz</code>, <code>_space_group_symop_operation_xyz</code>, <code>_symmetry_equiv.pos_as_xyz</code>, <code>_symmetry_equiv_pos_as_xyz</code>.

## Atom in the cell {#expanded-atom-site}

<code>_expanded_atom_site</code> — Every atom of the unit cell, generated from the atom sites by symmetry.

### <code>_expanded_atom_site.atom_site_id</code> {#expanded-atom-site-atom-site-id}

The atom site this atom is generated from.

**GUI:** site. **Units:** not applicable.

**CIF names:** <code>_edi_expanded_atom_site.atom_site_id</code>.

### <code>_expanded_atom_site.site_symmetry</code> {#expanded-atom-site-site-symmetry}

The symmetry code that generates this atom from its site.

**GUI:** symmetry. **Units:** not applicable.

**CIF names:** <code>_edi_expanded_atom_site.site_symmetry</code>.

### <code>_expanded_atom_site.fract_x</code> {#expanded-atom-site-fract-x}

Fractional x-coordinate.

**GUI:** x. **Units:** not applicable.

**CIF names:** <code>_edi_expanded_atom_site.fract_x</code>.

### <code>_expanded_atom_site.fract_y</code> {#expanded-atom-site-fract-y}

Fractional y-coordinate.

**GUI:** y. **Units:** not applicable.

**CIF names:** <code>_edi_expanded_atom_site.fract_y</code>.

### <code>_expanded_atom_site.fract_z</code> {#expanded-atom-site-fract-z}

Fractional z-coordinate.

**GUI:** z. **Units:** not applicable.

**CIF names:** <code>_edi_expanded_atom_site.fract_z</code>.

### <code>_expanded_atom_site.cartn_x</code> {#expanded-atom-site-cartn-x}

Cartesian X-coordinate.

**GUI:** X. **Units:** Å.

**CIF names:** <code>_edi_expanded_atom_site.cartn_x</code>.

### <code>_expanded_atom_site.cartn_y</code> {#expanded-atom-site-cartn-y}

Cartesian Y-coordinate.

**GUI:** Y. **Units:** Å.

**CIF names:** <code>_edi_expanded_atom_site.cartn_y</code>.

### <code>_expanded_atom_site.cartn_z</code> {#expanded-atom-site-cartn-z}

Cartesian Z-coordinate.

**GUI:** Z. **Units:** Å.

**CIF names:** <code>_edi_expanded_atom_site.cartn_z</code>.

### <code>_expanded_atom_site.occupancy</code> {#expanded-atom-site-occupancy}

Occupancy of the atom.

**GUI:** occ. **Units:** not applicable.

**CIF names:** <code>_edi_expanded_atom_site.occupancy</code>.

### <code>_expanded_atom_site.u_iso</code> {#expanded-atom-site-u-iso}

Isotropic displacement of the atom, as U.

**GUI:** U iso. **Units:** Å².

**CIF names:** <code>_edi_expanded_atom_site.u_iso</code>.

### <code>_expanded_atom_site.cluster_id</code> {#expanded-atom-site-cluster-id}

Atoms within one shared position carry the same cluster number.

**GUI:** cluster. **Units:** not applicable.

**CIF names:** <code>_edi_expanded_atom_site.cluster_id</code>.

## Bond {#geom-bond}

<code>_geom_bond</code> — The bonds between the atoms of the cell.

### <code>_geom_bond.expanded_atom_site_id_1</code> {#geom-bond-expanded-atom-site-id-1}

The first atom of the bond, in the atoms of the cell.

**GUI:** atom 1. **Units:** not applicable.

**CIF names:** <code>_edi_geom_bond.expanded_atom_site_id_1</code>.

### <code>_geom_bond.expanded_atom_site_id_2</code> {#geom-bond-expanded-atom-site-id-2}

The second atom of the bond, in the atoms of the cell.

**GUI:** atom 2. **Units:** not applicable.

**CIF names:** <code>_edi_geom_bond.expanded_atom_site_id_2</code>.

### <code>_geom_bond.atom_site_label_1</code> {#geom-bond-atom-site-label-1}

The atom site of the first atom.

**GUI:** site 1. **Units:** not applicable.

**CIF names:** <code>_geom_bond.atom_site_label_1</code>, <code>_geom_bond_atom_site_label_1</code>, <code>_geom_bond.atom_site_id_1</code>.

### <code>_geom_bond.atom_site_label_2</code> {#geom-bond-atom-site-label-2}

The atom site of the second atom.

**GUI:** site 2. **Units:** not applicable.

**CIF names:** <code>_geom_bond.atom_site_label_2</code>, <code>_geom_bond_atom_site_label_2</code>, <code>_geom_bond.atom_site_id_2</code>.

### <code>_geom_bond.site_symmetry_1</code> {#geom-bond-site-symmetry-1}

The symmetry code of the first atom.

**GUI:** symmetry 1. **Units:** not applicable.

**CIF names:** <code>_geom_bond.site_symmetry_1</code>, <code>_geom_bond_site_symmetry_1</code>.

### <code>_geom_bond.site_symmetry_2</code> {#geom-bond-site-symmetry-2}

The symmetry code of the second atom.

**GUI:** symmetry 2. **Units:** not applicable.

**CIF names:** <code>_geom_bond.site_symmetry_2</code>, <code>_geom_bond_site_symmetry_2</code>.

### <code>_geom_bond.distance</code> {#geom-bond-distance}

The length of the bond.

**GUI:** distance. **Units:** Å.

**CIF names:** <code>_geom_bond.distance</code>, <code>_geom_bond_distance</code>, <code>_geom_bond.dist</code>.

## Cartesian frame {#atom-sites-cartn-transform}

<code>_atom_sites_cartn_transform</code> — The matrix from fractional to Cartesian coordinates.

### <code>_atom_sites_cartn_transform.mat_11</code> {#atom-sites-cartn-transform-mat-11}

Element 11 of the fractional-to-Cartesian matrix.

**GUI:** M₁₁. **Units:** Å.

**CIF names:** <code>_atom_sites_Cartn_transform.mat_11</code>, <code>_atom_sites_Cartn_tran_matrix_11</code>, <code>_atom_sites.Cartn_transf_matrix[1][1]</code>.

### <code>_atom_sites_cartn_transform.mat_12</code> {#atom-sites-cartn-transform-mat-12}

Element 12 of the fractional-to-Cartesian matrix.

**GUI:** M₁₂. **Units:** Å.

**CIF names:** <code>_atom_sites_Cartn_transform.mat_12</code>, <code>_atom_sites_Cartn_tran_matrix_12</code>, <code>_atom_sites.Cartn_transf_matrix[1][2]</code>.

### <code>_atom_sites_cartn_transform.mat_13</code> {#atom-sites-cartn-transform-mat-13}

Element 13 of the fractional-to-Cartesian matrix.

**GUI:** M₁₃. **Units:** Å.

**CIF names:** <code>_atom_sites_Cartn_transform.mat_13</code>, <code>_atom_sites_Cartn_tran_matrix_13</code>, <code>_atom_sites.Cartn_transf_matrix[1][3]</code>.

### <code>_atom_sites_cartn_transform.mat_21</code> {#atom-sites-cartn-transform-mat-21}

Element 21 of the fractional-to-Cartesian matrix.

**GUI:** M₂₁. **Units:** Å.

**CIF names:** <code>_atom_sites_Cartn_transform.mat_21</code>, <code>_atom_sites_Cartn_tran_matrix_21</code>, <code>_atom_sites.Cartn_transf_matrix[2][1]</code>.

### <code>_atom_sites_cartn_transform.mat_22</code> {#atom-sites-cartn-transform-mat-22}

Element 22 of the fractional-to-Cartesian matrix.

**GUI:** M₂₂. **Units:** Å.

**CIF names:** <code>_atom_sites_Cartn_transform.mat_22</code>, <code>_atom_sites_Cartn_tran_matrix_22</code>, <code>_atom_sites.Cartn_transf_matrix[2][2]</code>.

### <code>_atom_sites_cartn_transform.mat_23</code> {#atom-sites-cartn-transform-mat-23}

Element 23 of the fractional-to-Cartesian matrix.

**GUI:** M₂₃. **Units:** Å.

**CIF names:** <code>_atom_sites_Cartn_transform.mat_23</code>, <code>_atom_sites_Cartn_tran_matrix_23</code>, <code>_atom_sites.Cartn_transf_matrix[2][3]</code>.

### <code>_atom_sites_cartn_transform.mat_31</code> {#atom-sites-cartn-transform-mat-31}

Element 31 of the fractional-to-Cartesian matrix.

**GUI:** M₃₁. **Units:** Å.

**CIF names:** <code>_atom_sites_Cartn_transform.mat_31</code>, <code>_atom_sites_Cartn_tran_matrix_31</code>, <code>_atom_sites.Cartn_transf_matrix[3][1]</code>.

### <code>_atom_sites_cartn_transform.mat_32</code> {#atom-sites-cartn-transform-mat-32}

Element 32 of the fractional-to-Cartesian matrix.

**GUI:** M₃₂. **Units:** Å.

**CIF names:** <code>_atom_sites_Cartn_transform.mat_32</code>, <code>_atom_sites_Cartn_tran_matrix_32</code>, <code>_atom_sites.Cartn_transf_matrix[3][2]</code>.

### <code>_atom_sites_cartn_transform.mat_33</code> {#atom-sites-cartn-transform-mat-33}

Element 33 of the fractional-to-Cartesian matrix.

**GUI:** M₃₃. **Units:** Å.

**CIF names:** <code>_atom_sites_Cartn_transform.mat_33</code>, <code>_atom_sites_Cartn_tran_matrix_33</code>, <code>_atom_sites.Cartn_transf_matrix[3][3]</code>.

### <code>_atom_sites_cartn_transform.axes</code> {#atom-sites-cartn-transform-axes}

How the Cartesian axes are placed in the cell.

**GUI:** axes. **Units:** not applicable.

**CIF names:** <code>_atom_sites_Cartn_transform.axes</code>, <code>_atom_sites_Cartn_transform_axes</code>, <code>_atom_sites.Cartn_transform_axes</code>.

## Data source {#data-source}

<code>_data_source</code> — The file the measured data were read from.

### <code>_data_source.file_name</code> {#data-source-file-name}

The file the measured data were read from.

**GUI:** data file. **Units:** not applicable.

**CIF names:** <code>_edi_data_source.file_name</code>.

## Measured data point {#data}

<code>_data</code> — The measured pattern and the values calculated at each of its points.

### <code>_data.two_theta</code> {#data-two-theta}

The scattering angle of each point.

**GUI:** 2θ. **Units:** deg.

**CIF names:** <code>_pd_meas.2theta_scan</code>, <code>_pd_meas_2theta_scan</code>, <code>_pd_meas_angle_2theta</code>, <code>_pd_proc.2theta_scan</code>.

### <code>_data.time_of_flight</code> {#data-time-of-flight}

The time of flight of each point.

**GUI:** TOF. **Units:** µs.

**CIF names:** <code>_pd_meas.time_of_flight</code>, <code>_pd_meas_time_of_flight</code>.

### <code>_data.intensity_meas</code> {#data-intensity-meas}

The measured intensity.

**GUI:** meas. **Units:** not applicable.

**CIF names:** <code>_pd_meas.intensity_total</code>, <code>_pd_meas_intensity_total</code>, <code>_pd_proc.intensity_norm</code>.

### <code>_data.intensity_meas_su</code> {#data-intensity-meas-su}

The standard uncertainty of the measured intensity.

**GUI:** s.u.. **Units:** not applicable.

**CIF names:** <code>_pd_meas.intensity_total_su</code>, <code>_pd_proc.intensity_norm_su</code>.

### <code>_data.d_spacing</code> {#data-d-spacing}

The d-spacing of each point.

**GUI:** d. **Units:** Å.

**CIF names:** <code>_pd_proc.d_spacing</code>, <code>_pd_proc_d_spacing</code>.

### <code>_data.intensity_calc</code> {#data-intensity-calc}

The calculated intensity, the background included.

**GUI:** calc. **Units:** not applicable.

**CIF names:** <code>_pd_calc.intensity_total</code>, <code>_pd_calc_intensity_total</code>.

### <code>_data.intensity_bkg</code> {#data-intensity-bkg}

The background at each point.

**GUI:** bkg. **Units:** not applicable.

**CIF names:** <code>_pd_calc.intensity_bkg</code>.

### <code>_data.calc_status</code> {#data-calc-status}

Whether the point takes part in the calculation and the fit.

**GUI:** status. **Units:** not applicable.

**CIF names:** <code>_edi_data.calc_status</code>, <code>_pd_data.refinement_status</code>.

| Stored value | GUI option | Meaning |
| --- | --- | --- |
| <code>incl</code> | Included | The point is calculated and fitted. |
| <code>excl</code> | Excluded | The point lies in an excluded region and is not calculated. |

## Calculated point {#data-calc}

<code>_data_calc</code> — The calculated pattern the command line writes.

### <code>_data_calc.point_id</code> {#data-calc-point-id}

The index of the point in the calculated pattern.

**GUI:** point. **Units:** not applicable.

**CIF names:** <code>_pd_data.point_id</code>, <code>_pd_data_point_id</code>.

## Structure curves {#pd-calc-overall}

<code>_pd_calc_overall</code> — The structures the per-point curves follow.

### <code>_pd_calc_overall.component_presentation_order</code> {#pd-calc-overall-component-presentation-order}

The structures whose curves the per-point lists hold, in their order.

**GUI:** structure order. **Units:** not applicable.

**CIF names:** <code>_edi_pd_calc_overall.component_presentation_order</code>.

## Structure curve {#pd-calc}

<code>_pd_calc</code> — Each structure&#x27;s calculated curve, one value per structure at every point of the pattern.

### <code>_pd_calc.component_intensities_net</code> {#pd-calc-component-intensities-net}

Each structure&#x27;s calculated intensity at the point, the background excluded, in the order _pd_calc_overall.component_presentation_order gives.

**GUI:** structure calc. **Units:** not applicable.

**CIF names:** <code>_pd_calc.component_intensities_net</code>.

## Reflection {#refln}

<code>_refln</code> — The Bragg reflections of each linked structure.

### <code>_refln.structure_id</code> {#refln-structure-id}

The structure the reflection belongs to.

**GUI:** structure. **Units:** not applicable.

**CIF names:** <code>_pd_refln.phase_id</code>, <code>_pd_refln_phase_id</code>, <code>_refln.phase_id</code>.

### <code>_refln.d_spacing</code> {#refln-d-spacing}

The d-spacing of the reflection.

**GUI:** d. **Units:** Å.

**CIF names:** <code>_refln.d_spacing</code>, <code>_refln_d_spacing</code>.

### <code>_refln.sin_theta_over_lambda</code> {#refln-sin-theta-over-lambda}

sin θ over λ of the reflection.

**GUI:** sin θ/λ. **Units:** 1/Å.

**CIF names:** <code>_refln.sin_theta_over_lambda</code>, <code>_refln_sint/lambda</code>, <code>_refln_sin_theta_over_lambda</code>, <code>_refln.sint_over_lambda</code>.

### <code>_refln.index_h</code> {#refln-index-h}

The h index of the reflection.

**GUI:** h. **Units:** not applicable.

**CIF names:** <code>_refln.index_h</code>, <code>_refln_index_h</code>.

### <code>_refln.index_k</code> {#refln-index-k}

The k index of the reflection.

**GUI:** k. **Units:** not applicable.

**CIF names:** <code>_refln.index_k</code>, <code>_refln_index_k</code>.

### <code>_refln.index_l</code> {#refln-index-l}

The l index of the reflection.

**GUI:** l. **Units:** not applicable.

**CIF names:** <code>_refln.index_l</code>, <code>_refln_index_l</code>.

### <code>_refln.f_calc</code> {#refln-f-calc}

The calculated structure-factor amplitude.

**GUI:** F calc. **Units:** not applicable.

**CIF names:** <code>_refln.F_calc</code>, <code>_refln_F_calc</code>, <code>_refln.f_calc</code>.

### <code>_refln.f_meas</code> {#refln-f-meas}

The measured structure-factor amplitude, the square root of a single crystal&#x27;s measured F², as its chart plots it in F.

**GUI:** F meas. **Units:** not applicable.

**CIF names:** <code>_refln.F_meas</code>, <code>_refln_F_meas</code>.

### <code>_refln.f_squared_calc</code> {#refln-f-squared-calc}

The calculated squared structure factor.

**GUI:** F² calc. **Units:** not applicable.

**CIF names:** <code>_refln.F_squared_calc</code>, <code>_refln_F_squared_calc</code>, <code>_refln.f_squared_calc</code>.

### <code>_refln.intensity_meas</code> {#refln-intensity-meas}

The measured squared structure factor of a single crystal&#x27;s reflection.

**GUI:** F² meas. **Units:** not applicable.

**CIF names:** <code>_refln.intensity_meas</code>, <code>_refln_intensity_meas</code>.

### <code>_refln.intensity_meas_su</code> {#refln-intensity-meas-su}

The standard uncertainty of the measured squared structure factor.

**GUI:** s.u.. **Units:** not applicable.

**CIF names:** <code>_refln.intensity_meas_su</code>, <code>_refln_intensity_meas_su</code>, <code>_refln.intensity_sigma</code>, <code>_refln_intensity_sigma</code>.

### <code>_refln.intensity_calc</code> {#refln-intensity-calc}

The calculated squared structure factor of a single crystal&#x27;s reflection.

**GUI:** F² calc. **Units:** not applicable.

**CIF names:** <code>_refln.intensity_calc</code>, <code>_refln_intensity_calc</code>.

### <code>_refln.wavelength</code> {#refln-wavelength}

The wavelength a time-of-flight single crystal&#x27;s reflection was measured at.

**GUI:** λ. **Units:** Å.

**CIF names:** <code>_refln.wavelength</code>, <code>_refln_wavelength</code>.

### <code>_refln.two_theta</code> {#refln-two-theta}

The Bragg angle of the reflection.

**GUI:** 2θ. **Units:** deg.

**CIF names:** <code>_edi_refln.two_theta</code>, <code>_refln.two_theta</code>.

### <code>_refln.time_of_flight</code> {#refln-time-of-flight}

The time of flight of the reflection.

**GUI:** TOF. **Units:** µs.

**CIF names:** <code>_edi_refln.time_of_flight</code>, <code>_refln.time_of_flight</code>.

## Fit start value {#fit-parameter}

<code>_fit_parameter</code> — The values the last fit started from, kept so the fit can be undone.

### <code>_fit_parameter.id</code> {#fit-parameter-id}

The parameter the start value belongs to.

**GUI:** parameter. **Units:** not applicable.

**CIF names:** <code>_edi_fit_parameter.id</code>.

### <code>_fit_parameter.start_value</code> {#fit-parameter-start-value}

The value the last fit started from.

**GUI:** start value. **Units:** not applicable.

**CIF names:** <code>_edi_fit_parameter.start_value</code>, <code>_fit_parameter.start_value</code>.

### <code>_fit_parameter.start_uncertainty</code> {#fit-parameter-start-uncertainty}

The uncertainty the parameter had when the last fit started.

**GUI:** start error. **Units:** not applicable.

**CIF names:** <code>_edi_fit_parameter.start_uncertainty</code>, <code>_fit_parameter.start_uncertainty</code>.

### <code>_fit_parameter.start_tied</code> {#fit-parameter-start-tied}

Whether the parameter was tied when the last fit started.

**GUI:** start tied. **Units:** not applicable.

**CIF names:** <code>_edi_fit_parameter.start_tied</code>.

## Fit result {#fit-result}

<code>_fit_result</code> — The outcome of the last fit.

### <code>_fit_result.result_kind</code> {#fit-result-result-kind}

What kind of fit gave the result.

**GUI:** kind. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.result_kind</code>, <code>_fit_result.result_kind</code>.

### <code>_fit_result.success</code> {#fit-result-success}

Whether the fit converged.

**GUI:** success. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.success</code>, <code>_fit_result.success</code>.

### <code>_fit_result.message</code> {#fit-result-message}

The minimizer&#x27;s message.

**GUI:** message. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.message</code>, <code>_fit_result.message</code>.

### <code>_fit_result.iterations</code> {#fit-result-iterations}

How many iterations the fit took.

**GUI:** iterations. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.iterations</code>, <code>_fit_result.iterations</code>.

### <code>_fit_result.fitting_time</code> {#fit-result-fitting-time}

How long the fit took.

**GUI:** time. **Units:** s.

**CIF names:** <code>_edi_fit_result.fitting_time</code>, <code>_fit_result.fitting_time</code>.

### <code>_fit_result.reduced_chi_square</code> {#fit-result-reduced-chi-square}

χ² divided by the degrees of freedom.

**GUI:** reduced χ². **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.reduced_chi_square</code>, <code>_fit_result.reduced_chi_square</code>.

### <code>_fit_result.objective_name</code> {#fit-result-objective-name}

The quantity the fit minimized.

**GUI:** objective. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.objective_name</code>, <code>_fit_result.objective_name</code>.

### <code>_fit_result.objective_value</code> {#fit-result-objective-value}

The value of the objective at the end of the fit.

**GUI:** objective value. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.objective_value</code>, <code>_fit_result.objective_value</code>.

### <code>_fit_result.n_data_points</code> {#fit-result-n-data-points}

How many data points the fit used.

**GUI:** points. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.n_data_points</code>, <code>_fit_result.n_data_points</code>.

### <code>_fit_result.n_parameters</code> {#fit-result-n-parameters}

How many parameters the project has.

**GUI:** parameters. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.n_parameters</code>, <code>_fit_result.n_parameters</code>.

### <code>_fit_result.n_free_parameters</code> {#fit-result-n-free-parameters}

How many parameters the fit refined.

**GUI:** free parameters. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.n_free_parameters</code>, <code>_fit_result.n_free_parameters</code>.

### <code>_fit_result.degrees_of_freedom</code> {#fit-result-degrees-of-freedom}

The points minus the free parameters.

**GUI:** degrees of freedom. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.degrees_of_freedom</code>, <code>_fit_result.degrees_of_freedom</code>.

### <code>_fit_result.covariance_available</code> {#fit-result-covariance-available}

Whether the fit gave a covariance matrix.

**GUI:** covariance. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.covariance_available</code>, <code>_fit_result.covariance_available</code>.

### <code>_fit_result.exit_reason</code> {#fit-result-exit-reason}

Why the fit stopped.

**GUI:** exit reason. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.exit_reason</code>, <code>_fit_result.exit_reason</code>.

### <code>_fit_result.prof_wr_factor</code> {#fit-result-prof-wr-factor}

The weighted profile R factor.

**GUI:** Rwp. **Units:** %.

**CIF names:** <code>_edi_fit_result.prof_wr_factor</code>, <code>_fit_result.prof_wR_factor</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>single crystal</code> | wR(F²) | % | — |

### <code>_fit_result.prof_r_factor</code> {#fit-result-prof-r-factor}

The profile R factor.

**GUI:** Rp. **Units:** %.

**CIF names:** <code>_edi_fit_result.prof_r_factor</code>, <code>_fit_result.prof_R_factor</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>single crystal</code> | R(F²) | % | — |

### <code>_fit_result.prof_wr_expected</code> {#fit-result-prof-wr-expected}

The expected weighted profile R factor.

**GUI:** Rexp. **Units:** %.

**CIF names:** <code>_edi_fit_result.prof_wr_expected</code>, <code>_fit_result.prof_wR_expected</code>.

### <code>_fit_result.prof_cr_factor</code> {#fit-result-prof-cr-factor}

The background-corrected profile R factor.

**GUI:** cRp. **Units:** %.

**CIF names:** <code>_edi_fit_result.prof_cr_factor</code>.

### <code>_fit_result.prof_cwr_factor</code> {#fit-result-prof-cwr-factor}

The background-corrected weighted profile R factor.

**GUI:** cRwp. **Units:** %.

**CIF names:** <code>_edi_fit_result.prof_cwr_factor</code>.

### <code>_fit_result.profile_function</code> {#fit-result-profile-function}

The peak profile the fit used.

**GUI:** profile. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.profile_function</code>, <code>_fit_result.profile_function</code>.

### <code>_fit_result.background_function</code> {#fit-result-background-function}

The background the fit used.

**GUI:** background. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.background_function</code>, <code>_fit_result.background_function</code>.

### <code>_fit_result.descent</code> {#fit-result-descent}

The descent strategy the fit used.

**GUI:** descent. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result.descent</code>.

## Experiment fit result {#fit-result-bank}

<code>_fit_result_bank</code> — The agreement factors of each experiment in the last fit.

### <code>_fit_result_bank.n_data_points</code> {#fit-result-bank-n-data-points}

How many data points of the experiment the fit used.

**GUI:** points. **Units:** not applicable.

**CIF names:** <code>_edi_fit_result_bank.n_data_points</code>.

### <code>_fit_result_bank.prof_r_factor</code> {#fit-result-bank-prof-r-factor}

The experiment&#x27;s profile R factor.

**GUI:** Rp. **Units:** %.

**CIF names:** <code>_pd_proc_ls.prof_R_factor</code>, <code>_pd_proc_ls_prof_R_factor</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>single crystal</code> | R(F²) | % | — |

### <code>_fit_result_bank.prof_wr_factor</code> {#fit-result-bank-prof-wr-factor}

The experiment&#x27;s weighted profile R factor.

**GUI:** Rwp. **Units:** %.

**CIF names:** <code>_pd_proc_ls.prof_wR_factor</code>, <code>_pd_proc_ls_prof_wR_factor</code>.

| Form | GUI label | Units | CIF name |
| --- | --- | --- | --- |
| <code>single crystal</code> | wR(F²) | % | — |

### <code>_fit_result_bank.prof_wr_expected</code> {#fit-result-bank-prof-wr-expected}

The experiment&#x27;s expected weighted profile R factor.

**GUI:** Rexp. **Units:** %.

**CIF names:** <code>_pd_proc_ls.prof_wR_expected</code>, <code>_pd_proc_ls_prof_wR_expected</code>.

### <code>_fit_result_bank.prof_cr_factor</code> {#fit-result-bank-prof-cr-factor}

The experiment&#x27;s background-corrected profile R factor.

**GUI:** cRp. **Units:** %.

**CIF names:** <code>_edi_fit_result_bank.prof_cr_factor</code>.

### <code>_fit_result_bank.prof_cwr_factor</code> {#fit-result-bank-prof-cwr-factor}

The experiment&#x27;s background-corrected weighted profile R factor.

**GUI:** cRwp. **Units:** %.

**CIF names:** <code>_edi_fit_result_bank.prof_cwr_factor</code>.

### <code>_fit_result_bank.chi_square</code> {#fit-result-bank-chi-square}

The experiment&#x27;s reduced χ².

**GUI:** reduced χ². **Units:** not applicable.

**CIF names:** <code>_edi_fit_result_bank.chi_square</code>.

## Structure fit result {#fit-result-phase}

<code>_fit_result_phase</code> — The agreement factors of each structure in each experiment.

### <code>_fit_result_phase.bragg_r_factor</code> {#fit-result-phase-bragg-r-factor}

The structure&#x27;s Bragg R factor in the experiment.

**GUI:** R Bragg. **Units:** %.

**CIF names:** <code>_refine_ls.R_I_factor</code>, <code>_refine_ls_R_I_factor</code>, <code>_refine.ls_R_I_factor_obs</code>.

### <code>_fit_result_phase.f_r_factor</code> {#fit-result-phase-f-r-factor}

The structure&#x27;s structure-factor R factor in the experiment.

**GUI:** R F. **Units:** %.

**CIF names:** <code>_refine_ls.R_factor_all</code>, <code>_refine_ls_R_factor_all</code>, <code>_refine.ls_R_factor_all</code>.

## Correlation {#fit-parameter-correlation}

<code>_fit_parameter_correlation</code> — The correlations between the fitted parameters.

### <code>_fit_parameter_correlation.id</code> {#fit-parameter-correlation-id}

The name of the correlation.

**GUI:** id. **Units:** not applicable.

**CIF names:** <code>_edi_fit_parameter_correlation.id</code>, <code>_fit_parameter_correlation.id</code>.

### <code>_fit_parameter_correlation.source_kind</code> {#fit-parameter-correlation-source-kind}

What kind of fit the correlation comes from.

**GUI:** source. **Units:** not applicable.

**CIF names:** <code>_edi_fit_parameter_correlation.source_kind</code>, <code>_fit_parameter_correlation.source_kind</code>.

### <code>_fit_parameter_correlation.parameter_unique_name_i</code> {#fit-parameter-correlation-parameter-unique-name-i}

The first parameter.

**GUI:** parameter 1. **Units:** not applicable.

**CIF names:** <code>_edi_fit_parameter_correlation.parameter_unique_name_i</code>, <code>_fit_parameter_correlation.param_unique_name_i</code>.

### <code>_fit_parameter_correlation.parameter_unique_name_j</code> {#fit-parameter-correlation-parameter-unique-name-j}

The second parameter.

**GUI:** parameter 2. **Units:** not applicable.

**CIF names:** <code>_edi_fit_parameter_correlation.parameter_unique_name_j</code>, <code>_fit_parameter_correlation.param_unique_name_j</code>.

### <code>_fit_parameter_correlation.correlation</code> {#fit-parameter-correlation-correlation}

The correlation coefficient between the two parameters.

**GUI:** correlation. **Units:** not applicable.

**CIF names:** <code>_edi_fit_parameter_correlation.correlation</code>, <code>_fit_parameter_correlation.correlation</code>.

### <code>_fit_parameter_correlation.file_path</code> {#fit-parameter-correlation-file-path}

The data file of a sequential fit the correlation belongs to.

**GUI:** file. **Units:** not applicable.

**CIF names:** <code>_edi_fit_parameter_correlation.file_path</code>.

## Report block {#pd-block}

<code>_pd_block</code> — The name each data block of the CIF report gives itself.

### <code>_pd_block.id</code> {#pd-block-id}

The name of a data block of the CIF report, which a phase link refers to.

**GUI:** block. **Units:** not applicable.

**CIF names:** <code>_pd_block.id</code>, <code>_pd_block_id</code>.
