# Projects and files

Use the application to open, save and export the complete analysis. The shared [Project](../user-guide/analysis-workflow/project.md) stage explains what belongs in a project; [data formats](../user-guide/data-formats.md) explains its folder and archive representations.

## Open a project

Choose **Open project…**, then **Folder** or **Zip archive**. In the desktop app you can also drop a project folder, its `project.edi`, or a zip archive onto the window.

When a project opens, the app prepares its pages in turn. The status bar shows progress and a top-bar page becomes available when it is ready.

If your current project has unsaved changes when you open another, create one or quit, the application asks whether to save them.

## Save or save a copy

**Save** writes to the project's current location when that is writable. **Save project as…** lets you choose a different location or format.

On the desktop, **Save project as…** offers **Folder**, **Zip archive**, and **Save a copy**. A copy records the current state without moving the project you continue to work on.

An archive opened on the desktop is unpacked into a working copy. Save writes the archive again. If it is not writable, or it is a bundled example, the application asks where to keep your work instead.

## Browser file handling

| Browser workflow | What Save does | How to keep a separate copy |
| --- | --- | --- |
| Chrome or Edge, project opened from a selected folder or archive | Writes back to that selected location when access is available | **Save project as…** chooses a folder or archive |
| Firefox or Safari | Saves the browser-held project | **Save project as…** downloads a zip copy |
| An example or new project in any browser | Initially keeps the project in browser storage | **Save project as…** exports a zip copy |
| A private window without persistent storage | The project may exist only in the current tab | Export with **Save project as…** before closing |

The location **In this browser only** means that browser storage is holding your project. Browsers can clear that storage; keep a copy on your computer for work you need to retain.

## Recent projects and recovery

The browser's **Recent projects** list includes projects it keeps. After a reload or closed tab it can offer **Continue where you left off**, including changes not explicitly saved before the interruption.

Recovery is useful, but it is not a substitute for keeping your own project copy.

## What is saved

Saving writes the project state and measured data, including the selected analysis settings. Values are rounded according to the project's precision and uncertainty policy. The open project is updated to those saved values and its calculated pattern and agreement factors are recalculated from them.

A report is separate: saving a project does not create a fresh report. Use [Save report](reports.md) to update a document you intend to share.

## Move to another interface

Open the saved folder, `project.edi` or archive from [Python](../python/index.md) or [the Command Line](../cli/index.md). The shared [project concepts](../user-guide/analysis-workflow/project.md) explain what those interfaces read.
