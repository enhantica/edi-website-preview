# About EasyDiffraction

EasyDiffraction makes diffraction modelling and refinement available through a visual application, Python and the command line. You can calculate a signal from a structural model, compare it with observations, refine selected parameters, and keep the analysis as a project.

## One product, connected interfaces

The current product is developed in the [edi repository](https://github.com/enhantica/edi). Its Python import is `edi`, and its command-line entry point is `python -m edi`. The desktop and browser applications provide a visual workspace over the same project model.

The shared native product core handles the project and analysis, using crysta for diffraction calculation and minimisation. The interface you choose changes how you work, while structures, experiments and analysis settings remain connected.

## From earlier EasyDiffraction releases

The project has earlier application and library generations, documented on separate websites. Their useful ideas continue here: a project-centred workflow, readable scientific files, worked examples and documentation for different ways of analysing data.

The current documentation brings these entry points together:

- **Application** explains the desktop and browser workspace.
- **Python** covers scripts and notebooks using `edi`.
- **CLI** covers commands that operate on saved projects.
- **Learn** explains the shared scientific model and examples.

Earlier names, imports, release numbers and backend descriptions belong to their corresponding versions. Use [the earlier documentation](#earlier-documentation) when reproducing work done with one of those releases.

## Open scientific software

The current source code is available on GitHub. edi's source is licensed under BSD 3-Clause; the built application is distributed under GPL version 3. See [licensing](licence.md) for the authoritative files.

The source repository also holds the examples, their provenance and comparisons against reference results. [Fit quality](../learn/fit-quality.md) explains how to read that evidence and its scope.

## Participate and report your work

Use the [community and support page](community.md) to report a problem or propose an improvement. For a scientific publication or shared analysis, record the software and inputs you used; [citing and recording an analysis](citation.md) gives a practical checklist.

## Earlier documentation

| Resource | What it documents |
| --- | --- |
| [Earlier project website](https://easydiffraction.org/) | The earlier application and library releases, with their downloads and project overview |
| [Earlier library documentation](https://docs.easydiffraction.org/lib/latest/) | The earlier Python library, its API, tutorials and verification pages |
| [Earlier application documentation](https://docs.easydiffraction.org/app/) | The earlier desktop application and its workflow |
| [Archived project website](https://easydiffraction.github.io/) | An older application release and project presentation |

---

Sources: [edi overview](https://github.com/enhantica/edi/blob/main/README.md), [product architecture](https://github.com/enhantica/edi/blob/main/docs/dev/adrs/0009-cpp-product-core-thin-bindings.md), [earlier library introduction](https://github.com/easyscience/diffraction-lib/blob/master/docs/docs/introduction/index.md).
