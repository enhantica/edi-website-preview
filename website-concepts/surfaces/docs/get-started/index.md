# Get started

Start with an example in the browser. You can explore the project, compare a measured pattern with its calculation, and run a refinement without installing a programming environment.

[Open the web app](https://enhantica.github.io/edi/webapp/){ .md-button .md-button--primary }
[Your first refinement](first-refinement.md){ .md-button }

## Try a complete analysis

1. Open the web application and go to **Project**.
2. Choose a measured-data project from **Examples**.
3. Inspect its structure and experiment before fitting.
4. Review the free parameters on **Analysis**, then run the fit.
5. Inspect the result and save your own project copy.

[Your first refinement](first-refinement.md) walks through these steps. The [workspace tour](../application/workspace.md) explains the pages and their controls.

## Choose how you work

| You want to… | Start here |
| --- | --- |
| Explore interactively with no local installation | [Browser application](../application/browser.md) |
| Work with projects on your computer | [Desktop application](../application/desktop.md) |
| Express an analysis in a script or notebook | [Python library](../python/index.md) |
| Run saved projects from a terminal | [Command-line interface](../cli/index.md) |

The interfaces share the scientific model. Their setup, controls and file handling differ. [Choose your interface](interfaces.md) compares them.

## Bring your own work

Once the example workflow is familiar, [create a project](../application/new-project.md) and import a structure and measured data. Check the [data formats](../learn/data-formats.md) before preparing files.

You can also reopen a complete project folder or zip archive. A structural CIF on its own supplies the structure, rather than all the settings of an analysis.

## Learn the common ideas

The [Learn](../learn/index.md) section covers projects, parameters, fitting modes and fit quality once for every interface. Use the [glossary](../learn/glossary.md) whenever an unfamiliar term appears.

## Set up a local environment

Current local builds use the edi source environment and its native dependencies. The [setup overview](setup.md) links the appropriate desktop, Python and Command Line instructions and explains the current availability.

---

Sources: [current example catalogue](https://github.com/enhantica/edi/blob/main/docs/user/cli/index.md), [app project controls](https://github.com/enhantica/edi/blob/main/app/qml/Pages/Project/ProjectPage.qml), [current project workflow](https://github.com/enhantica/edi/blob/main/docs/user/guides/projects-from-scratch-in-the-app.md).
