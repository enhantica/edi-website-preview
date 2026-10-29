# Command Line

Run a saved EasyDiffraction project from a terminal. The project keeps the structural model and analysis settings together, so a command names the input rather than rebuilding the scientific model.

```console
python -m edi fit path/to/project
```

## Choose a command

| Command | Purpose | Guide |
| --- | --- | --- |
| `fit` | Refine the project's model against its measured data. | [Run a refinement](fit.md) |
| `calc` | Calculate from the current model without fitting. | [Calculate a project](calculate.md) |
| `report` | Save a report or check whether saved reports are current. | [Reports](reports.md) |
| `export` | Package a saved project as a zip archive. | [Files and output](files.md) |
| `undo` | Restore the persisted state before the last fit. | [Command reference](reference.md) |

These commands are available in a configured edi environment. See [Python setup](../python/setup.md) for current source-build availability; this preview does not invent a public package-install command.

## Choose where results go

`fit` normally saves the refined folder back to its input location. `calc` normally writes its calculated data there. Both support `--dry` to do the computation without writing, or `--output DIR` to keep results in another folder.

A zip input is kept unchanged by `fit` and `calc`; use `--output DIR` to retain their results. Read [files and output](files.md) before automating a run.

## Keep your analysis reproducible

Store the project alongside your analysis. Its declared fitting mode determines whether the run fits one experiment, several experiments jointly, or a scan.

## Use the same model

The Command Line shares [projects and experiments](../learn/projects.md) with Python and the application. Use whichever interface fits the next step in your work. [Batch workflows](batch.md) shows ordinary shell automation around these commands.

---

Sources: current commands and defaults from [edi's argument parser](https://github.com/enhantica/edi/blob/main/lib/edi/__main__.py), [complete-project loading](https://github.com/enhantica/edi/blob/main/docs/user/guides/complete-project-loading.md), and [project input/output](https://github.com/enhantica/edi/blob/main/docs/user/guides/open-save-and-export.md).
