# Python quick reference

This page covers the calls demonstrated in this preview. It is a **selected reference**, not a complete generated API catalogue. The [current declared surface](https://github.com/enhantica/edi/blob/main/data/python-surface.json) lists the broader interface; signatures and behavior should be checked in the matching edi version.

## Project input and output

| Call or property | Purpose |
| --- | --- |
| `edi.Project.load(path)` | Open a complete project folder, its `project.edi`, or a zip. |
| `project.location` | Read the project's current location. |
| `project.save()` | Write the project to its current location. |
| `project.save_as(folder)` | Write a folder and continue working there. |
| `project.export_zip(path)` | Package the project's folder as last saved. |

## Model inspection

| Property | Purpose |
| --- | --- |
| `project.structures` | Inspect the project's structures. |
| `project.experiments` | Inspect its experiments. |
| `project.free_parameters` | Inspect parameters whose `free` flag is set. |
| `parameter.value` | Read or change a parameter's value. |
| `parameter.free` | Read or change whether it may vary. |

Factories used here are `StructureFactory.from_cif_path(path)` and `ExperimentFactory.from_data_path(...)`. These create model components, not automatically complete analysis projects.

## Analysis

| Call or property | Purpose |
| --- | --- |
| `project.analysis.calculate()` | Calculate from the current project; results stay on experiments. |
| `project.analysis.fit()` | Run the refinement selected by the declared mode. |
| `project.analysis.fitting_mode` | Read or set `single`, `joint`, `sequential` or `independent`. |
| `project.analysis.descent` | Read or select a registered descent strategy. |

Optional fit callbacks are `on_start`, `on_iteration`, `on_scan_start`, `on_file_complete` and `should_cancel`. Scan-specific callbacks require a scan-mode project.

## Reports

| Call | Purpose |
| --- | --- |
| `project.report.as_html(...)` | Obtain HTML text. |
| `project.report.save_html(path, ...)` | Write an HTML report. |
| `project.report.save_cif(path)` | Write a CIF report. |
| `project.report.save(...)` | Write the project's selected formats, except PDF. |
| `project.report.check()` | Read saved-report freshness states. |

See [reports](reports.md) for call-specific options and the difference between saved settings and per-call overrides.

---

Sources: layout adapted from the [earlier quick reference](https://docs.easydiffraction.org/lib/latest/quick-reference/); members checked against [edi's declared API](https://github.com/enhantica/edi/blob/main/data/python-surface.json), [Python facade](https://github.com/enhantica/edi/blob/main/lib/edi/__init__.py), and [project input/output guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/open-save-and-export.md).
