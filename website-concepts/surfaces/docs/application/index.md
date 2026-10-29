# The application

Use the EasyDiffraction application to build a crystallographic model, compare calculated and measured diffraction data, refine parameters, and prepare a report. The desktop and browser applications share the same visual workspace and project model.

[Open the web app](https://enhantica.github.io/edi/webapp/){ .md-button .md-button--primary }
[Follow your first refinement](first-refinement.md){ .md-button }

![EasyDiffraction showing measured and calculated diffraction patterns with experiment controls](../assets/edi-app.png)

## A workflow you can follow

The pages across the top follow **Project → Structure → Experiment → Analysis → Report**. You can return to an earlier page whenever your model needs attention.

| Page | What you do there |
| --- | --- |
| [Project](projects.md) | Open an example or a saved project, and decide where to keep your work. |
| [Structure](structures.md) | Load or create crystal structures, then edit symmetry, cell and atom sites. |
| [Experiment](experiments.md) | Load measured data and describe the instrument, profile, background and linked structures. |
| [Analysis](refine.md) | Choose free parameters, select the fitting mode and inspect the result. |
| [Report](reports.md) | Review and save a document containing your model and results. |

## Start with an example or your own data

An included example provides structures, experiments and starting conditions together. It is a useful first step if you want to understand the controls before preparing input files.

To use your own measurement, [create a new project](new-project.md), add a structure, create an experiment and load its data. You can also open a complete existing project.

## Desktop and browser

The scientific workflow is the same. File handling depends on where the application runs:

- [Desktop](desktop.md) works directly with project folders and zip archives on your computer.
- [Browser](browser.md) supports local file access in Chrome and Edge. Other browser workflows use browser storage and downloadable project copies.

## Use the same project elsewhere

The project also opens in [Python](../python/index.md) and through the [command line](../cli/index.md). Shared explanations belong in [User guide](../user-guide/index.md); these pages focus on the application's controls.

---

Sources: [current project creation guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/projects-from-scratch-in-the-app.md), [current open/save guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/open-save-and-export.md), [earlier workflow](https://github.com/easyscience/diffraction-lib/blob/develop/docs/docs/user-guide/analysis-workflow/index.md).
