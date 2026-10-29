# Learn diffraction analysis

A visual refinement, a Python notebook and a command-line run can describe the same analysis. The shared ideas are the project, its structures and experiments, the parameters allowed to vary, and the evidence used to judge the result.

Start here when you want to understand the analysis itself. The [Application](../application/index.md), [Python](../python/index.md) and [Command Line](../cli/index.md) sections explain the controls and commands particular to each interface.

## Understand the model

- [From measurement to analysis](concepts.md) explains what EasyDiffraction takes as input and what the model represents.
- [Projects and experiments](projects.md) describes the common project model and the workflow from structure to report.
- [Parameters](parameters.md) explains values, uncertainties, free parameters and relationships between them.
- [Glossary](glossary.md) defines the terms used across the documentation.

## Prepare the inputs

Use [data formats](data-formats.md) to distinguish a saved Edi project from a structural CIF, a measured pattern and an exported report. Keep the complete project when moving an analysis between interfaces.

## Choose the analysis

The [fitting modes](fitting-modes.md) determine whether the analysis fits one experiment, several experiments together, or the successive datasets of a scan. A calculation without measured data is useful for exploring a structural model before fitting.

## Interpret the result

[Fit quality](fit-quality.md) connects the pattern, residual, agreement factors and parameter uncertainties. A small agreement factor is one part of the assessment; the scientific model and the structure of the residual matter too.

## Work through an example

The [example projects](examples.md) combine structures, experiments, data and starting conditions. Open one in the app, load the same project in Python, or pass it to the command line.

---

Sources: [earlier library guide](https://github.com/easyscience/diffraction-lib/tree/master/docs/docs/user-guide), [edi user guides](https://github.com/enhantica/edi/tree/main/docs/user/guides).
