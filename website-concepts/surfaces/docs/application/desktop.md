# Work on your desktop

The desktop application uses the same workspace and project model as the web app. It works directly with project folders and zip archives on your computer.

## Open local work

Use **Open project…** and choose **Folder** or **Zip archive**. You can also drop a project folder, its `project.edi` file or an archive onto the window.

A zip archive is unpacked into a temporary working copy. **Save** writes the archive again when its location is writable; otherwise the app asks where to keep it.

## Save or hand on a copy

**Save project as…** offers a folder or zip archive. Select **Save a copy** to write the current state somewhere else while continuing in the original project.

Folders are convenient when you want to inspect individual structure, experiment or result files. A zip archive keeps the project together when sharing or moving it.

## Use the same workspace

The [workspace tour](workspace.md), [refinement guide](refine.md), [scan guide](scans.md) and [reports](reports.md) apply to both desktop and browser versions.

## Current desktop source

The current edi repository provides the desktop application for building from source. In an existing configured development checkout:

```console
pixi run -e app app-build
pixi run -e app app-run
```

The build uses the repository's dependencies, including access to the crysta SDK. The [contributor documentation](https://enhantica.github.io/edi/dev/) covers development setup.

To explore the current visual interface without a local build, use the [web app](browser.md). Earlier EasyDiffraction installers belong to their earlier implementation and are not interchangeable with the current edi application.

## Continue in Python or the Command Line

The project you save is also the input to [Python](../python/index.md) and [the command line](../cli/index.md). Those interfaces let you script the same project model.

---

Sources: [current desktop project-file guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/open-save-and-export.md), [current application build tasks](https://github.com/enhantica/edi/blob/main/pixi.toml).
