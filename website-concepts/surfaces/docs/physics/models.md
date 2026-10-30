---
template: physics.html
---

# Model catalogue

<span id="planned-scientific-models"></span>

Use the exact model identifier to select its explanation. Planned and proposed capabilities appear beside related models with their status; they have no selectable type token in this reference snapshot. The [parameter index](parameters.md) defines individual scientific fields. [Features and roadmap](../user-guide/features.md) distinguishes editing, execution and planned work in the four interfaces.

## Peak profiles {#peak-profiles}

### Constant-wavelength peak profiles

| Type | Scope | Explanation |
| --- | --- | --- |
| `cwl-gaussian` | CW powder | [Physics](profiles/cw.md#eq-cwl-pseudovoigt) |
| `cwl-lorentzian` | CW powder | [Physics](profiles/cw.md#eq-cwl-pseudovoigt) |
| `cwl-pseudo-voigt` | CW powder | [Physics](profiles/cw.md#eq-caglioti) |
| `cwl-pseudo-voigt-berar-baldinozzi` | CW powder | [Physics](profiles/cw.md#eq-berar-baldinozzi) |
| `cwl-tch-pseudo-voigt` | CW powder | [Physics](profiles/cw.md#eq-tch) |
| `cwl-tch-pseudo-voigt-fcj` | CW powder | [Physics](profiles/cw.md#eq-fcj) |

### Time-of-flight peak profiles

| Type or model | Scope | Explanation |
| --- | --- | --- |
| `tof-jorgensen` | TOF neutron powder | [Physics](profiles/tof.md#eq-jorgensen) |
| `tof-jorgensen-von-dreele` | TOF neutron powder | [Physics](profiles/tof.md#eq-jorgensen-von-dreele) |
| `tof-pseudo-voigt` | TOF neutron powder | [Physics](profiles/tof.md#tof-pseudo-voigt) |
| Ikeda–Carpenter · **Planned** | TOF pulse profile | [Planned model](profiles/tof.md#ikeda-carpenter) |

## Absorption {#absorption}

| Type | Scope | Explanation |
| --- | --- | --- |
| `none` | CW/TOF | [Physics](corrections/absorption.md#absorption-types) |
| `cylinder-hewat` | CW; TOF input spelling cylinder | [Physics](corrections/absorption.md#eq-hewat) |
| `cylinder-lobanov` | CW | [Physics](corrections/absorption.md#eq-lobanov) |

## Extinction {#extinction}

| Type | Scope | Explanation |
| --- | --- | --- |
| `none` | single-crystal Bragg | [Physics](corrections/extinction.md#extinction-types) |
| `becker-coppens-type-1` | single-crystal Bragg | [Physics](corrections/extinction.md#extinction-types) |
| `becker-coppens-type-2` | single-crystal Bragg | [Physics](corrections/extinction.md#extinction-types) |
| `becker-coppens-mixed` | single-crystal Bragg | [Physics](corrections/extinction.md#extinction-types) |
| `larson-isotropic` | single-crystal Bragg | [Physics](corrections/extinction.md#eq-larson) |
| `larson-anisotropic` | single-crystal Bragg | [Physics](corrections/extinction.md#eq-larson) |

## Background {#background}

| Type | Scope | Explanation |
| --- | --- | --- |
| `line-segment` | powder | [Physics](background.md#eq-line-segment-background) |
| `polynomial` | powder | [Physics](background.md#eq-polynomial-background) |
| `chebyshev` | powder | [Physics](background.md#eq-chebyshev-background) |

## Atomic displacement {#adp}

| Type | Scope | Explanation |
| --- | --- | --- |
| `Biso` | structure | [Physics](displacement.md#eq-isotropic-adp) |
| `Uiso` | structure | [Physics](displacement.md#eq-isotropic-adp) |
| `Bani` | structure | [Physics](displacement.md#eq-anisotropic-adp) |
| `Uani` | structure | [Physics](displacement.md#eq-anisotropic-adp) |
| `beta` | structure | [Physics](displacement.md#eq-anisotropic-adp) |

## Background estimation {#background-estimation}

| Type | Scope | Explanation |
| --- | --- | --- |
| `auto` | powder baseline proposal | [Physics](background.md#background-estimation) |
| `arpls` | powder baseline proposal | [Physics](background.md#eq-arpls) |
| `snip` | powder baseline proposal | [Physics](background.md#eq-snip) |
| `fabc` | powder baseline proposal | [Physics](background.md#fabc) |

## Scattering models {#scattering-models}

The current [nuclear neutron](diffraction.md#eq-nuclear-structure-factor) and [X-ray](diffraction.md#eq-xray-structure-factor) models use the source selections listed above.

| Model | Status | Explanation |
| --- | --- | --- |
| Nuclear neutron Bragg | Current | [Structure factor](diffraction.md#eq-nuclear-structure-factor) |
| X-ray Bragg | Current | [Structure factor](diffraction.md#eq-xray-structure-factor) |
| Magnetic diffraction | Planned | [Scattering](diffraction.md#magnetic-diffraction) |
| Polarized diffraction | Planned | [Scattering](diffraction.md#polarized-diffraction) |
| Total scattering and PDF | Planned | [Scattering](diffraction.md#total-scattering-and-pdf) |

## X-ray form factor {#xray-form-factor}

| Type | Scope | Explanation |
| --- | --- | --- |
| `wk1995` | CW X-ray | [Physics](diffraction.md#eq-xray-structure-factor) |
| `it1992` | CW X-ray | [Physics](diffraction.md#eq-xray-structure-factor) |

## X-ray dispersion {#xray-dispersion}

| Type | Scope | Explanation |
| --- | --- | --- |
| `cromer-liberman` | CW X-ray | [Physics](diffraction.md#eq-xray-structure-factor) |
| `sasaki1989` | CW X-ray | [Physics](diffraction.md#eq-xray-structure-factor) |
| `it1992` | CW X-ray | [Physics](diffraction.md#eq-xray-structure-factor) |
| `none` | CW X-ray | [Physics](diffraction.md#eq-xray-structure-factor) |

## Neutron scattering length {#neutron-scattering-length}

| Type | Scope | Explanation |
| --- | --- | --- |
| `rauch2003ext` | neutron | [Physics](diffraction.md#eq-nuclear-structure-factor) |
| `sears1992` | neutron | [Physics](diffraction.md#eq-nuclear-structure-factor) |

## Fitting mode {#fitting-mode}

| Type | Scope | Explanation |
| --- | --- | --- |
| `single` | project analysis | [Physics](rietveld.md#joint-refinement) |
| `joint` | project analysis | [Physics](rietveld.md#joint-refinement) |
| `sequential` | project analysis | [Physics](rietveld.md#scan-refinement) |
| `independent` | project analysis | [Physics](rietveld.md#scan-refinement) |

## Intensity extraction {#intensity-extraction}

| Model | Status | Explanation |
| --- | --- | --- |
| Le Bail / Pawley | Proposed | [Analysis](rietveld.md#intensity-extraction) |

## Descent {#descent}

| Type | Scope | Explanation |
| --- | --- | --- |
| `ladder` | least-squares; selected strategies have bound restrictions | [Physics](minimization.md#eq-lm) |
| `fast_descent` | least-squares; selected strategies have bound restrictions | [Physics](minimization.md#eq-lm) |
| `fast_descent_linear_snap` | least-squares; selected strategies have bound restrictions | [Physics](minimization.md#eq-lm) |
| `fast_descent_guarded_linear_snap` | least-squares; selected strategies have bound restrictions | [Physics](minimization.md#eq-lm) |
| `multistart_prune` | least-squares; selected strategies have bound restrictions | [Physics](minimization.md#eq-lm) |

## Preferred orientation {#preferred-orientation}

| Type | Scope | Explanation |
| --- | --- | --- |
| `march-dollase` | linked phase in CW powder | [Physics](corrections/orientation.md#eq-march-dollase) |

## Reference snapshot {#reference-snapshot}

The [machine-readable catalogue](catalogue.json) records the inspected edi source and its declared crysta SDK, along with the model/parameter identifiers used for this reference. Availability is scoped to that source snapshot; a development build or installed release can differ. Use its declared model list and version when answering a build-specific question.
