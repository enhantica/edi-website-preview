---
template: gui.html
---

# :material-archive: Projects and files

Use the application to open, save and export the complete analysis. The shared [Project](../user-guide/analysis-workflow/project.md) stage explains what belongs in a project; [data formats](../user-guide/data-formats.md) explains its folder and archive representations.

## Open a project

Choose **Open project…**, then **Folder** or **Zip archive**. In the desktop app you can also drop a project folder, its `project.edi`, or a zip archive onto the window.

When a project opens, the app prepares its pages in turn. The status bar shows progress and a top-bar page becomes available when it is ready.

If your current project has unsaved changes when you open another, create one or quit, the application asks whether to save them.

<!-- gui-guide:open-a-project -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-project-open.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Choose a project folder or archive"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Choose a project folder or archive"><title>Choose a project folder or archive</title><defs><clipPath id="gui-clip-guide-project-open-overview-projects-open-a-project-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-project-open.png" width="1480" height="800" clip-path="url(#gui-clip-guide-project-open-overview-projects-open-a-project-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-project-open-overview-projects-open-a-project-0-1" data-gui-parts="[[607,371,97.96562500000005,58]]" d="M605.000 369.000 L706.966 369.000 L706.966 431.000 L605.000 431.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>
<figcaption>Choose a project folder or archive.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-project-open-overview-projects-open-a-project-0-1" aria-pressed="true">1. Project source</button> Choose a folder or a zip archive.</li></ol>
</figure>
<!-- /gui-guide -->

## Save or save a copy

**Save** writes to the project's current location when that is writable. **Save project as…** lets you choose a different location or format.

On the desktop, **Save project as…** offers **Folder**, **Zip archive**, and **Save a copy**. A copy records the current state without moving the project you continue to work on.

An archive opened on the desktop is unpacked into a working copy. Save writes the archive again. If it is not writable, or it is a bundled example, the application asks where to keep your work instead.

<!-- gui-guide:save-or-save-a-copy -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-project-save.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Choose a save format or save a copy"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Choose a save format or save a copy"><title>Choose a save format or save a copy</title><defs><clipPath id="gui-clip-guide-project-save-overview-projects-save-or-save-a-copy-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-project-save.png" width="1480" height="800" clip-path="url(#gui-clip-guide-project-save-overview-projects-save-or-save-a-copy-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-project-save-overview-projects-save-or-save-a-copy-0-1" data-gui-parts="[[607,354,111.84375,93]]" d="M605.000 352.000 L720.844 352.000 L720.844 449.000 L605.000 449.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>
<figcaption>Choose a save format or save a copy.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-project-save-overview-projects-save-or-save-a-copy-0-1" aria-pressed="true">1. Save options</button> Choose the output format and whether to save a copy.</li></ol>
</figure>
<!-- /gui-guide -->

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

<!-- gui-guide:recent-projects-and-recovery -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-project-recent.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Find recent projects"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Find recent projects"><title>Find recent projects</title><defs><clipPath id="gui-clip-guide-project-recent-overview-projects-recent-projects-and-recovery-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-project-recent.png" width="1480" height="800" clip-path="url(#gui-clip-guide-project-recent-overview-projects-recent-projects-and-recovery-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-project-recent-overview-projects-recent-projects-and-recovery-0-1" data-gui-parts="[[770,203.0000000000036,710,180.00000000000003]]" d="M768.000 201.000 L1482.000 201.000 L1482.000 385.000 L768.000 385.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>
<figcaption>Find recent projects.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-project-recent-overview-projects-recent-projects-and-recovery-0-1" aria-pressed="true">1. Recent projects</button> </li></ol>
</figure>
<!-- /gui-guide -->

## What is saved

Saving writes the project state and measured data, including the selected analysis settings. Values are rounded according to the project's precision and uncertainty policy. The open project is updated to those saved values and its calculated pattern and agreement factors are recalculated from them.

A report is separate: saving a project does not create a fresh report. Use [Save report](reports.md) to update a document you intend to share.

<!-- gui-guide:what-is-saved -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-project-actions.png" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Open or save the current project"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Open or save the current project"><title>Open or save the current project</title><defs><clipPath id="gui-clip-guide-project-actions-overview-projects-what-is-saved-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-project-actions.png" width="1480" height="800" clip-path="url(#gui-clip-guide-project-actions-overview-projects-what-is-saved-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-project-actions-overview-projects-what-is-saved-0-1" data-gui-parts="[[1132,168,334,39]]" d="M1130.000 166.000 L1468.000 166.000 L1468.000 209.000 L1130.000 209.000 Z" /><path class="" data-gui-region="guide-project-actions-overview-projects-what-is-saved-0-2" data-gui-parts="[[784,221,334,39]]" d="M782.000 219.000 L1120.000 219.000 L1120.000 262.000 L782.000 262.000 Z" /><path data-gui-navigation data-gui-parts="[[595.46875,0,59.734375,77]]" d="M593.469 -2.000 L657.203 -2.000 L657.203 79.000 L593.469 79.000 Z" /></svg></a>
<figcaption>Open or save the current project.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-project-actions-overview-projects-what-is-saved-0-1" aria-pressed="true">1. Open project…</button> </li><li><button type="button" data-gui-target="guide-project-actions-overview-projects-what-is-saved-0-2" aria-pressed="false">2. Save project as…</button> </li></ol>
</figure>
<!-- /gui-guide -->

## Move to another interface

Open the saved folder, `project.edi` or archive from [Python](../python/index.md) or [the Command Line](../cli/index.md). The shared [project concepts](../user-guide/analysis-workflow/project.md) explain what those interfaces read.
