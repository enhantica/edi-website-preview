# Your first refinement

Choose a measured-data example and work through one complete analysis. The scientific steps are the same in the application, Python and the command line; choose the instructions for the interface you want to use.

## Choose how to follow along

| Interface | Walkthrough | What you need |
| --- | --- | --- |
| Application | [First refinement in the app](../application/first-refinement.md) | A browser, or a configured desktop build |
| Python | [Load and fit a project](../python/fit.md) | A configured edi environment and a measured-data example project |
| Command Line | [Refine a project](../cli/fit.md) | The same environment and a saved measured-data project |

The LBCO example measured on HRPT is a useful starting point. It supplies the structure, experiment, observations and starting parameter choices together. A simulation example has a calculation range but no measured data to refine against.

## Inspect before fitting

Check the structure, experiment type, measurement units and initial calculated pattern. Decide which independent parameters may vary. For a first run, retain the example's supplied choices so you can compare your result with its documented starting conditions.

The [analysis workflow](../user-guide/analysis-workflow/index.md) explains what each part of the project contributes.

## Fit, assess and retain

Run the refinement using your chosen interface. Read how it ended, compare the observed and calculated signals, and inspect fitted values and uncertainties. [Fit quality](../user-guide/fit-quality.md) explains the assessment.

Keep a separate copy of the starting project, save the refined project, and prepare a report when you want to share the result. The interface walkthroughs explain the corresponding actions and save locations.

## Continue with your own measurement

Prepare a structural model and observations in the supported [data formats](../user-guide/data-formats.md), then follow the [Project](../user-guide/analysis-workflow/project.md), [Structure](../user-guide/analysis-workflow/structure.md) and [Experiment](../user-guide/analysis-workflow/experiment.md) stages. Return to the interface guide for the actual import steps.


---

Sources: [earlier library guide](https://github.com/easyscience/diffraction-lib/blob/master/docs/docs/user-guide/analysis-workflow/index.md), [current edi guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/complete-project-loading.md).
