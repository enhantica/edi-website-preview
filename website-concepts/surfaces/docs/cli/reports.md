# Save and check reports

The report command uses the project's structures, experiments, fit results and saved report settings. It presents the same document as Python and the application's Report page.

## Save the selected formats

```console
python -m edi report path/to/project
```

This writes the formats selected by the project into its `reports/` folder, except PDF. The application writes PDF; the command leaves an existing PDF and its record as they are.

Saving a project does not automatically save its report. A report can become out of date after changes to the model or report contents.

## Write an HTML file elsewhere

```console
python -m edi report path/to/project --output refinement.html --offline
```

`--output PATH` writes one HTML report without changing the project's saved-report list. `--offline` embeds chart libraries; `--online` makes the HTML load them from the web. Both are overrides for this run.

## Choose the contents

```console
python -m edi report path/to/project --x-axis d_spacing --exclude data
python -m edi report path/to/project --exclude reflections --exclude correlations
python -m edi report path/to/project --include-all
```

Optional group keys are `charts`, `correlations`, `reflections`, `data` and `evolution`. Repeat `--exclude` for several groups, or use `--include-all`. These two choices are mutually exclusive.

## Correlations and colours

| Option | Meaning |
| --- | --- |
| `--x-axis native` or `d_spacing` | Use the experiment's native axis or d-spacing. |
| `--correlation-threshold X` | Show parameters whose strongest correlation reaches X, from 0 to 1. |
| `--correlation-experiment NAME` | Choose the experiment for the correlation chart in a multi-experiment fit. |
| `--colour-scheme NAME` | Use `ediNatural`, `ediCoast`, `ediGarden`, `ediStudio` or `ediContrast`. |

These switches affect the generated report for that run; they do not replace the project's saved preferences.

## Check saved reports

```console
python -m edi report path/to/project --check
```

The command lists each saved report as `current`, `out of date` or `missing`, writing nothing. It exits with status `1` when a listed report is not current. It checks the saved list; it does not require that a project has already saved a report.

---

Sources: [current report guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/the-report.md) and [report parser/execution](https://github.com/enhantica/edi/blob/main/lib/edi/__main__.py). The report's role follows the [earlier report workflow](https://docs.easydiffraction.org/lib/latest/user-guide/analysis-workflow/report/).
