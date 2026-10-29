# Glossary

These terms are shared by the application, Python library and command line. The interface changes how you work with them, rather than changing their scientific meaning.

## Project and model

| Term | Meaning |
| --- | --- |
| Project | The complete analysis: structures, experiments, data, analysis settings and saved results. A project can be kept as a folder or a `.zip` archive. |
| Structure | A crystallographic model of a phase, including its space group, unit cell and atom sites. |
| Experiment | The observation or simulation associated with an instrument model, profile, background and contributing structures. |
| Parameter | A model quantity such as a cell length, atom coordinate, scale or profile coefficient. A refinable parameter may be free or fixed. |
| Constraint | A declared relationship that reduces independent freedom between model quantities. A tied value is not another independently refined parameter. |

## Diffraction

**Powder diffraction** describes diffraction from a sample containing many crystallite orientations. The measured signal is commonly an intensity profile in which reflections can overlap.

**Single-crystal diffraction** measures individual reflections from an oriented crystal. Its observations and fit assessment differ from those of a powder profile.

**Constant wavelength (CWL)** describes a measurement using a specified wavelength, with a powder pattern commonly expressed against the scattering angle 2θ.

**Time of flight (TOF)** separates neutron wavelengths through arrival time. The instrument calibration relates time of flight to the diffraction geometry.

**Reflection** refers to diffraction associated with a set of lattice planes. A **Bragg-position mark** indicates where that reflection is expected in the pattern.

**Background** is the slowly varying contribution under diffraction peaks, represented by the background model chosen for the experiment.

## Analysis

| Term | Meaning |
| --- | --- |
| Calculation or simulation | Evaluation of the model with its present parameter values. A simulation may use a calculation range without measured observations. |
| Refinement or fit | Optimisation of the chosen free parameters against measured observations. |
| Residual | The difference between observed and calculated signal. Its pattern can reveal systematic disagreement that a single agreement factor hides. |
| Joint fit | One simultaneous fit using several experiments and their shared model quantities. |
| Sequential fit | Fitting a scan in order, starting each dataset from the preceding fit's parameter values. |
| Independent fit | Fitting the datasets of a scan from the same template starting values. |
| Standard uncertainty | The uncertainty reported with an estimated parameter or observation. A fitted uncertainty reflects the assumptions of the fit, rather than every possible systematic error. |

## Files and labels

**Edi (`.edi`)** is EasyDiffraction's saved project format. It uses readable CIF-like syntax with keys that describe the project model.

**CIF** means Crystallographic Information File, a scientific exchange format with dictionaries maintained by the IUCr. A structural CIF and a complete Edi project serve different purposes.

The catalogue uses `pd` for powder, `sc` for single crystal, `neut` for neutron, `xray` for X-ray, `cwl` for constant wavelength and `tof` for time of flight.

---

Sources: [earlier glossary](https://github.com/easyscience/diffraction-lib/blob/master/docs/docs/user-guide/glossary.md), [edi example catalogue](https://github.com/enhantica/edi/blob/main/docs/user/cli/index.md), [edi fitting workflow](https://github.com/enhantica/edi/blob/main/docs/user/guides/complete-project-loading.md).
