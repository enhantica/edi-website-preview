# Choose your interface

Choose the interface that fits the way you want to work. A saved project is the connection between them: structures, experiments, fitting settings and results can travel together.

## Compare the entry points

| Interface | A good starting point when… | How you interact |
| --- | --- | --- |
| Web application | You want to try an example or explore visually | Open the browser workspace and use its pages and controls |
| Desktop application | You want the visual workspace with local project files | Open folders or archives on your computer |
| Python library | Your analysis belongs in a script or notebook | Load and inspect project objects through `import edi` |
| Command line | You want to run the analysis declared by saved inputs | Use `python -m edi` with a project path |

The browser and desktop are two ways to run the graphical application. Python and the Command Line are alternative ways to work with the same project model.

## Application: direct visual exploration

Use the [application](../application/index.md) to inspect structures, compare measured and calculated patterns, edit model settings and run a fit. Its pages follow Project, Structure, Experiment, Analysis and Report.

The [web app](../application/browser.md) is the quickest way to try an example. The [desktop app](../application/desktop.md) works directly with local project folders and archives.

Browser file handling depends on the browser. Chrome and Edge can retain access to a chosen local folder or archive; Firefox and Safari keep the working project in browser storage and export a zip copy through **Save project as…**. Keep an external project copy when the work matters.

## Python: express the analysis in code

The [Python library](../python/index.md) exposes the model as `edi`. Load a project, inspect its structures and experiments, run its analysis and work with the result from code.

Use it for notebooks, repeated analyses and integration with your own processing. It requires a configured native edi environment; the Python source files alone do not supply the compiled core. See [Python setup](../python/setup.md).

## Command Line: run the saved project

The [command line](../cli/index.md) calculates or fits the project you give it. Structures, free parameters and minimizer conditions remain in the project rather than being recreated as a long command.

It is useful for repeatable terminal workflows and scripts that operate on saved projects. Start with [running a refinement](../cli/fit.md).

## Move between interfaces

Save a complete [project folder or archive](../learn/data-formats.md) to continue elsewhere. Export a [report](../application/reports.md) to share an account of the result.

Scientific concepts such as [parameters](../learn/parameters.md) and [fitting modes](../learn/fitting-modes.md) are shared; interface-specific pages explain how to reach them.

---

Sources: [edi overview](https://github.com/enhantica/edi/blob/main/README.md), [opening, saving and exporting](https://github.com/enhantica/edi/blob/main/docs/user/guides/open-save-and-export.md), [Python facade](https://github.com/enhantica/edi/blob/main/lib/edi/__init__.py), [Command Line entry point](https://github.com/enhantica/edi/blob/main/lib/edi/__main__.py).
