# Data formats

Keep the complete project when you want to continue an analysis. Use a structural CIF to exchange a crystal structure, measured-pattern files to bring in observations, and a report to communicate a result.

## A complete Edi project

An Edi project is a readable set of files that records the sample, experiments, analysis and reports together:

```text
project/
├── project.edi
├── structures/
├── experiments/
├── analysis/
└── reports/
```

`project.edi` carries the project-level information. The other files contain the structures, experiments and fitting settings. Reports and saved scan results stay with the project.

The folder can be packaged as a `.zip` archive. The app, Python and Command Line accept a project folder, its `project.edi`, or a project archive. The archive is useful for handing an analysis between a browser and a desktop or sending it to a collaborator.

## Edi and CIF

Edi uses CIF-like syntax: named data items, data blocks and `loop_` tables. Its keys describe EasyDiffraction's project model and include EasyDiffraction-owned categories.

CIF is the crystallographic exchange format maintained by the [International Union of Crystallography](https://www.iucr.org/resources/cif). Its dictionaries define scientific quantities and their names.

| File or document | What it is for |
| --- | --- |
| Edi project | Reopen the analysis with its structures, experiments, data and settings |
| Structural CIF | Import or exchange crystallographic structure information |
| Measured-pattern file | Supply observations to an experiment |
| CIF report | Exchange the model and fit result using scientific report names |
| HTML or PDF report | Inspect or share a readable account of the analysis |

A structure imported from CIF is a starting point. It still needs an experiment, instrument settings and measured data or a calculation range before it represents a complete analysis.

## Powder-pattern input

The app's **Load data…** action reads plain text containing columns for `x`, intensity, and optionally the standard uncertainty of intensity. The columns may be separated by spaces, tabs or commas.

- For constant-wavelength data, `x` is 2θ in degrees.
- For time-of-flight data, `x` is time of flight in microseconds.
- A supplied uncertainty is used as the observation's standard uncertainty. Check it as carefully as the intensity.

The loader reports skipped or adjusted rows in **Messages**. It skips non-numeric header lines, sorts by the independent variable, and keeps the first observation at a repeated position. Where uncertainty is absent or invalid, the loader applies the rules documented in the current input guide.

After loading, the measured data are stored in the experiment's Edi file. The project retains the source filename as context, but does not depend on that original text file to reopen the stored measurement.

!!! note "Check the imported pattern"

    Inspect the units, range, point count and Messages after importing. A readable file is not evidence that its columns or units describe the measurement you intended.

## Observations and calculation ranges

A fit-ready saved experiment declares its observations and uncertainties. A simulation experiment declares a calculation range instead. A complete-project loader refuses an ambiguous saved experiment that declares both forms or neither.

A project may contain both simulation and measured-data experiments. Calculation covers the project's experiments; fitting uses those with observations.

## Saving and handing on a project

On the desktop, choose a project folder or zip archive. In a browser, available save locations depend on the browser and how the project was opened. For portable work, **Save project as…** can export a zip copy to your computer.

A report is a separate output. Saving the project does not automatically create a fresh report. See [projects and files](../application/projects.md) and [reports](../application/reports.md) for the visual workflow.

---

Sources: [earlier data-format guide](https://github.com/easyscience/diffraction-lib/blob/master/docs/docs/user-guide/data-format.md), [edi input workflow](https://github.com/enhantica/edi/blob/main/docs/user/guides/projects-from-scratch-in-the-app.md), [complete-project contract](https://github.com/enhantica/edi/blob/main/docs/user/guides/complete-project-loading.md), [opening and saving](https://github.com/enhantica/edi/blob/main/docs/user/guides/open-save-and-export.md).
