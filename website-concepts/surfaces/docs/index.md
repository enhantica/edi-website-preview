---
title: Home
hide:
  - navigation
  - toc
  - path
---

# Making diffraction data analysis and modelling easy

Explore your data, refine your model and understand what the fit is telling you. Start in the
application, a Python notebook or your terminal, and keep the same project as your work grows.

[Try the web app](https://enhantica.github.io/edi/webapp/){ .md-button .md-button--primary }
[Get started](get-started/index.md){ .md-button }

![The EasyDiffraction application showing measured and calculated patterns, residuals and experiment controls](assets/edi-app.png)

## Choose how you work

<div class="grid cards" markdown>

-   **Application**

    ---

    Explore your model and pattern in a visual workspace, on your desktop or in your browser.

    [Explore the application](application/index.md)

-   **Python library**

    ---

    Use `edi` in a script or notebook and bring diffraction analysis into your scientific workflow.

    [Work in Python](python/index.md)

-   **Command line**

    ---

    Run the analysis declared by a project and make repeated runs part of your workflow.

    [Use the command line](cli/index.md)

</div>

## Learn the shared workflow

Keep structures, experiments, analysis settings and results together in a project. Learn these
concepts once, then choose the interface that suits your work.

1. Load a structure and an experiment, or start from an example.
2. Compare the calculated pattern with your measured data and choose which parameters vary.
3. Review the result, save your project and prepare a report.

[Understand the project model](learn/projects.md) · [Follow your first refinement](get-started/first-refinement.md)

## What you can do

Start with the part of the analysis you need. A project carries the structural model, experiment
settings and results between the visual application, Python and the command line.

| Your task | Where to start |
| --- | --- |
| Calculate a pattern from a structure and experiment, without measured data | [Calculate in Python](python/calculate.md) or [use the CLI](cli/calculate.md) |
| Bring your own structure and measured pattern into the app | [Create a project](application/new-project.md) |
| Choose background points and remove regions from a fit | [Background and excluded regions](application/background.md) |
| Refine a structural model against observations | [Application refinement](application/refine.md), [Python](python/fit.md) or [CLI](cli/fit.md) |
| Fit several experiments or follow a changing sample through a scan | [Understand fitting modes](learn/fitting-modes.md) |
| Assess the residual, uncertainties and agreement factors | [Fit quality](learn/fit-quality.md) |
| Keep an analysis portable or send it to a collaborator | [Projects and files](application/projects.md) |
| Share an interactive report or a scientific record | [Reports](application/reports.md) |

## Open and reproducible

EasyDiffraction is open scientific software. Its readable project files keep the structure,
experiment, fitting choices and saved results together. The current edi implementation uses the
crysta diffraction engine; older EasyDiffraction releases have their own interfaces and backends.

[About the project](about/index.md) · [Data and file formats](learn/data-formats.md) · [Get involved](about/community.md)

---

The product introduction develops the [earlier EasyDiffraction website](https://github.com/easyscience/EasyDiffractionWww/blob/master/content/home.yaml),
with the workflow from the [library documentation](https://github.com/easyscience/diffraction-lib/blob/master/docs/docs/user-guide/analysis-workflow/index.md).
The linked guides describe the current edi generation.
