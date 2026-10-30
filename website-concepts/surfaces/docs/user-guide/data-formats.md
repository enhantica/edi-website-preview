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
| HTML or PDF report | Inspect or share a readable account of the analysis |

A structure imported from CIF is a starting point. It still needs an experiment, instrument settings and measured data or a calculation range before it represents a complete analysis.

## Powder-pattern input

Powder observations can be supplied as plain text columns for `x`, intensity, and optionally the standard uncertainty of intensity. The supported reader and its diagnostic rules are documented for each interface.

- For constant-wavelength data, `x` is 2θ in degrees.
- For time-of-flight data, `x` is time of flight in microseconds.
- A supplied uncertainty is used as the observation's standard uncertainty. Check it as carefully as the intensity.

Inspect any reader diagnostics about skipped or adjusted rows. Import rules for headers, repeated positions, missing uncertainties and invalid observations are part of the reader behaviour; they should not be inferred from the filename extension.

After loading, the measured data are stored in the experiment's Edi file. The project retains the source filename as context, but does not depend on that original text file to reopen the stored measurement.

!!! note "Check the imported pattern"

    Inspect the units, range, retained observations and import diagnostics. A readable file is not evidence that its columns or units describe the measurement you intended.

## Observations and calculation ranges

A fit-ready saved experiment declares its observations and uncertainties. A simulation experiment declares a calculation range instead. A complete-project loader refuses an ambiguous saved experiment that declares both forms or neither.

A project may contain both simulation and measured-data experiments. Calculation covers the project's experiments; fitting uses those with observations.

## Saving and handing on a project

Hand on the complete project folder or archive to retain its saved model, embedded observations and analysis choices. Retain any external scan inputs as well. A report is a separate output, and saving a project does not automatically create a fresh report.

File selection, import diagnostics and write-back behaviour are interface-specific:

- [Application: measured-data import](../application/experiments.md) and [saving projects](../application/projects.md).
- [Python: experiment input](../python/experiments.md) and [project loading and saving](../python/projects.md).
- [Command Line: accepted project inputs and output destinations](../cli/files.md).

See the shared [:material-clipboard-text: Report](analysis-workflow/report.md) stage for document formats and provenance.
