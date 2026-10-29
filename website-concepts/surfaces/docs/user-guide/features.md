# Features and roadmap

Choose an interface for how you work. The scientific model is shared; the controls and ways to prepare a project differ. Each scientific feature below links to its definition in **Physics**.

## Reading the tables

**Edit & run** means that the interface can configure the feature and calculate or refine it. **Run project** means that it uses the feature from a prepared project; it does not provide a dedicated editor for it. **Available** describes the named action. **Partial** has a qualification below the table. **Unavailable** is not a promise of future delivery.

These are source-backed capabilities of the [reference snapshot](../physics/models.md#reference-snapshot), rather than a guarantee about every released installer. Browser storage and downloads differ from desktop file access. Planned work is listed separately, with no implied delivery date.

## Scientific coverage

| Feature and scientific definition | Web app | Desktop app | Python | Command Line |
| --- | --- | --- | --- | --- |
| [Nuclear neutron CW powder diffraction](../physics/diffraction.md#eq-nuclear-structure-factor) | Edit & run | Edit & run | Edit & run | Run project |
| [X-ray CW powder diffraction](../physics/diffraction.md#eq-xray-structure-factor) | Edit & run | Edit & run | Edit & run | Run project |
| [Neutron TOF powder diffraction](../physics/profiles/tof.md) | Edit & run | Edit & run | Edit & run | Run project |
| [Single-crystal neutron reflection calculation and fitting](../physics/corrections/extinction.md#single-crystal-intensity) | Edit & run | Edit & run | Edit & run | Run project |
| [Multiple phases, scales and mass fractions](../physics/diffraction.md#phase-fractions) | Edit & run | Edit & run | Edit & run | Run project |
| [Cell, symmetry, atom sites and occupancy](../physics/crystallography.md) | Edit & run | Edit & run | Edit & run | Run project |
| [Atomic displacement: isotropic and anisotropic conventions](../physics/displacement.md) | Edit & run | Edit & run | Edit & run | Run project |
| [Scattering-table and dispersion source selections](../physics/diffraction.md#eq-xray-structure-factor) | Run project | Run project | Edit & run | Run project |
| [CW Gaussian, Lorentzian and direct pseudo-Voigt profiles](../physics/profiles/cw.md#eq-cwl-pseudovoigt) | Edit & run | Edit & run | Edit & run | Run project |
| [CW TCH width and mixing](../physics/profiles/cw.md#eq-tch) | Edit & run | Edit & run | Edit & run | Run project |
| [Bérar–Baldinozzi and FCJ asymmetry](../physics/profiles/cw.md#eq-berar-baldinozzi) | Edit & run | Edit & run | Edit & run | Run project |
| [TOF Jorgensen, Jorgensen–Von Dreele and symmetric pseudo-Voigt](../physics/profiles/tof.md) | Edit & run | Edit & run | Edit & run | Run project |
| [Wavelength, zero offset and TOF calibration](../physics/calibration.md) | Edit & run | Edit & run | Edit & run | Run project |
| [CW displacement and transparency shifts](../physics/calibration.md#eq-line-shifts) | Edit & run | Edit & run | Edit & run | Run project |
| [CW cylindrical absorption: Hewat and Lobanov](../physics/corrections/absorption.md) | Edit & run | Edit & run | Edit & run | Run project |
| [TOF cylindrical absorption: active ABSCOR1](../physics/corrections/absorption.md#absorption-types) | Edit & run | Edit & run | Edit & run | Run project |
| [Becker–Coppens and Larson extinction](../physics/corrections/extinction.md) | Edit & run | Edit & run | Edit & run | Run project |
| [March–Dollase preferred orientation](../physics/corrections/orientation.md) | Edit & run | Edit & run | Edit & run | Run project |
| [X-ray polarization and wavelength doublet](../physics/corrections/intensity.md) | Edit & run | Edit & run | Edit & run | Run project |
| [Line-segment, polynomial and Chebyshev background](../physics/background.md) | Edit & run | Edit & run | Edit & run | Run project |
| [Automatic background estimation: arPLS, SNIP and FABC](../physics/background.md#background-estimation) | Edit & run | Edit & run | Edit & run | Run project |
| [Rietveld least-squares refinement](../physics/rietveld.md#eq-weighted-residual) | Edit & run | Edit & run | Edit & run | Run project |
| [Single and joint fitting](../physics/rietveld.md#joint-refinement) | Edit & run | Edit & run | Edit & run | Run project |
| [Sequential and independent scans](../physics/rietveld.md#scan-refinement) | Edit & run | Edit & run | Edit & run | Run project |
| [Agreement factors and uncertainties](../physics/reliability.md) | Available | Available | Available | Available |

**Scope details.** CW means constant wavelength; TOF means time of flight. Extinction here is a single-crystal correction; March–Dollase is the CW powder texture model. The [model catalogue](../physics/models.md) lists the exact admitted types. Automatic background settings in a saved project are honoured by command-line calculation and fitting, including re-estimation when needed; there is no separate command-line background editor.

**Stored fields.** The reciprocal TOF calibration coefficient and ABSCOR2 can be retained in a project but are not active calculation terms in this snapshot. They are not additional supported fitting directions. See [TOF calibration](../physics/calibration.md#eq-tof-calibration) and [TOF absorption](../physics/corrections/absorption.md#absorption-types).

## Preparing, running and sharing

| Action | Web app | Desktop app | Python | Command Line |
| --- | --- | --- | --- | --- |
| Open a complete project folder or archive | Available¹ | Available | Available | Available |
| Save or export the complete project | Available¹ | Available | Available | Available² |
| Create structures and experiments interactively | Available | Available | API | Unavailable³ |
| Import a structural CIF | Partial⁴ | Partial⁴ | Partial⁴ | Run prepared project |
| Import measured powder text data | Available | Available | Available | Run prepared project |
| Configure powder excluded regions | Available | Available | Available | Run project |
| Calculate without measured observations | Available | Available | Available | Available |
| Show fit progress and cancel | Available | Available | Callbacks | Terminal / interrupt |
| Inspect pattern and reflection charts | Available | Available | Result arrays / HTML report | Export arrays / HTML report |
| Write interactive or offline HTML reports | Available | Available | Available | Available |
| Write PDF reports | Available | Available | Unavailable | Unavailable |
| Write CIF reports | Unavailable | Unavailable | Unavailable | Unavailable |
| Check whether a saved report is current | Available | Available | Available | Available |

1. Browser support determines whether a folder can be opened directly or an archive is imported/exported. See [browser projects](../application/browser.md).
2. Fit/calculate write-back and export operate on the prepared project; see [input and output files](../cli/files.md).
3. Prepare the project in the application, Python or saved Edi files. The command line runs, reports and exports it.
4. Current structural input supports a defined subset, rather than arbitrary CIF declarations. More complete declaration handling is planned. See [data formats](data-formats.md).

For the equations behind inputs and outputs, use [crystallography](../physics/crystallography.md), [calibration](../physics/calibration.md), [background and exclusions](../physics/background.md#background-estimation), [refinement](../physics/rietveld.md) and [reliability and uncertainty](../physics/reliability.md). File operations and visual controls have their instructions under the corresponding interface tab.

## Planned scientific models {#planned-scientific-models}

The same four interfaces are shown so an engine roadmap item cannot be mistaken for a delivered interface feature. **Planned** means a recorded scientific roadmap item; interface controls and delivery remain subject to implementation. No feature below has source evidence of being in progress in this snapshot.

| Scientific feature | Web app | Desktop app | Python | Command Line | Recorded state |
| --- | --- | --- | --- | --- | --- |
| [Ikeda–Carpenter TOF pulse profile](../physics/models.md#planned-scientific-models) | Unavailable | Unavailable | Unavailable | Unavailable | Planned |
| [Magnetic diffraction](../physics/models.md#planned-scientific-models) | Unavailable | Unavailable | Unavailable | Unavailable | Planned |
| [Polarized diffraction](../physics/models.md#planned-scientific-models) | Unavailable | Unavailable | Unavailable | Unavailable | Planned |
| [Total scattering and PDF](../physics/models.md#planned-scientific-models) | Unavailable | Unavailable | Unavailable | Unavailable | Planned |
| [Le Bail / Pawley intensity extraction](../physics/models.md#planned-scientific-models) | Unavailable | Unavailable | Unavailable | Unavailable | Proposed |
| [Single-crystal reflection exclusions](../physics/reliability.md#single-crystal-factors) | Unavailable | Unavailable | Unavailable | Unavailable | Planned |

Other recorded work includes fuller CIF input and improved PDF-report production. A proposed item is a discussion candidate, rather than a committed delivery. This page will change with the [reference snapshot](../physics/models.md#reference-snapshot).
