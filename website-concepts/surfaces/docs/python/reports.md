# Reports from Python

The project's report brings together structures, experiments, calculated patterns and fit information. The application, Python and Command Line use the same report model and saved settings.

## Save interactive HTML

```python
html_path = project.report.save_html('refinement.html', offline=True)
print(html_path)
```

`offline=True` embeds the chart libraries, so the report does not need to fetch them when opened. With online libraries, a smaller report loads those libraries from the web. Charts remain interactive in HTML.

## Display in a notebook

```python
project.report
```

The report's notebook representation shows the document. To obtain its HTML text explicitly:

```python
html = project.report.as_html(offline=True)
```

## Choose contents for one call

```python
project.report.save_html(
    'refinement.html',
    offline=True,
    x_axis='d_spacing',
    excluded=['data'],
)
```

`native` and `d_spacing` select the pattern axis. Optional exclusions use `charts`, `correlations`, `reflections`, `data` and `evolution`. Keyword overrides affect that call; they do not overwrite the project's saved settings.

## Save the selected report formats

```python
written = project.report.save()
states = project.report.check()
print(written)
print(states)
```

`save()` writes the formats selected by the project except PDF, which is written by the application. `check()` returns saved report names with `current`, `out of date` or `missing` states.

Saving a project is separate from saving a report. A later model or report-settings change can make an existing report out of date.

## Export a CIF report

```python
project.report.save_cif('refinement.cif')
```

The CIF report contains result, structure and experiment blocks. It is a report of the analysis; retain the complete project as the editable working record.

---

Sources: adapted from [edi's report guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/the-report.md) and verified against the [Report facade](https://github.com/enhantica/edi/blob/main/lib/edi/__init__.py). The separation between project and report follows the [earlier report workflow](https://docs.easydiffraction.org/lib/latest/user-guide/analysis-workflow/report/).
