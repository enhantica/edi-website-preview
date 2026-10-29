# Find your way around

The application separates the analysis into pages, each with a main working view and related controls in the sidebar. The top bar moves between **Project**, **Structure**, **Experiment**, **Analysis** and **Report**.

## Project

Start with **Create a new project**, **Open project…**, or an example. Project information describes the work you are doing, while the project itself keeps structures, experiments and analysis settings together.

An example opens as a temporary working copy. Save a copy to keep changes you make to it.

## Structure

Select a structure from the **Structures** table, then edit its space group, cell and atom sites. A project can contain several structures. The selected structure determines which values the page displays.

The current page is called **Structure**; earlier application documentation called this page **Model**. See [work with structures](structures.md).

## Experiment

Select an experiment or scan dataset. The main view compares measured and calculated intensities; the sidebar contains the instrument, profile, background and other experiment settings.

The residual shows the difference between measured and calculated intensity. Reflection marks locate the calculated Bragg positions.

![Measured pattern, calculated pattern, reflection marks and residual in the application](../assets/edi-app.png)

## Analysis

The parameter table controls which parameters are free to vary. The fitting-mode control selects the analysis that applies to the project; **Start fitting** runs it.

For scan projects, additional controls let you follow the current dataset, inspect fitted-parameter evolution, stop and continue a run. See [fitting modes](fitting-modes.md) and [scans](scans.md).

## Report

The report combines structures, experiments, fit information and selected figures. Its sidebar controls the saved formats and which sections appear. A report is a document you can share; the project is the state you continue working on.

## Messages, selection and undo

The status bar reports messages and the state of the project. Read a message after importing data or when an operation is refused: it can explain a changed value or an unavailable action.

Changing the selected structure, experiment or dataset changes the values shown on the relevant pages. Undo returns project changes to their earlier state.

---

Sources: [earlier analysis workflow](https://github.com/easyscience/diffraction-lib/blob/develop/docs/docs/user-guide/analysis-workflow/index.md), [current fitting controls](https://github.com/enhantica/edi/blob/main/app/qml/Pages/Analysis/FittingGroup.qml), [current project controls](https://github.com/enhantica/edi/blob/main/app/qml/Pages/Project/GetStartedGroup.qml).
