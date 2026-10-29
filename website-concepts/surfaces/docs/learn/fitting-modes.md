# Fitting modes

Choose a fitting mode according to how your observations should share a model. The mode is part of the project, so the app, Python and Command Line can run the same declared analysis.

## The available modes

| Mode | Use it for | How the analysis runs |
| --- | --- | --- |
| `single` | One experiment or the shown dataset of a scan | Fits that experiment's observations |
| `joint` | Several experiments describing a connected model | Fits their observations together |
| `sequential` | A scan whose neighbouring datasets should carry a starting model forward | Fits datasets in order, seeding each from the preceding result |
| `independent` | A scan whose datasets should share the same starting point | Fits every dataset from the template's starting values |

A calculation without observations is a different action: it evaluates the model over a declared range and does not optimise against measured data.

## A single fit

Start with a single fit when learning an example or checking one measured pattern. Inspect the initial calculation, choose free parameters, then fit and review the [residual and agreement factors](fit-quality.md).

When working with a scan, a single fit on the shown dataset can establish the template dataset. That template supplies the structure and experiment settings used by the scan.

## A joint fit

A joint fit brings several experiments into one optimisation. The experiments may contain complementary information about the same structural model, with their own measurement and instrument settings.

Check which parameters are shared and which belong to individual experiments. A visually good result in one experiment can hide poor agreement in another, so inspect each experiment's pattern as well as the combined result.

## Sequential and independent scans

A scan is a series of measured datasets, often recorded while temperature or another condition changes. It uses a template experiment and a declared set of files.

In **sequential** mode, each result becomes the starting model for the next dataset. This is useful when the sample evolves gradually, but an unsuitable fit can influence the next starting point.

In **independent** mode, every dataset starts from the same template values. This makes the starting conditions consistent across the scan, while each dataset still needs an adequate initial model.

Both modes fit files serially. Their distinction is the starting state, rather than parallel execution.

## Review a scan

Inspect convergence and failures for the individual datasets. The app's dataset selector lets you review a fitted pattern, and the Evolution tab shows a selected parameter across the scan with its uncertainty.

Results are written to `analysis/results.csv` as the scan runs. Stopping keeps completed fits; continuing resumes with the remaining files. A change to the template can make earlier results out of date, so check the displayed state before combining them with new fits.

For controls, dataset selection and display updates, read [sequential fitting in the app](https://github.com/enhantica/edi/blob/main/docs/user/guides/sequential-fitting-in-the-app.md).

## Run the declared mode

The current Python entry point reads the fitting mode from the project:

```python
import edi

project = edi.Project.load('path/to/project')
result = project.analysis.fit()
```

The Command Line follows the same declaration:

```console
python -m edi fit path/to/project
```

Keep the mode, free-parameter choices and minimizer conditions with the saved project when sharing a result.

---

Sources: [complete-project loading](https://github.com/enhantica/edi/blob/main/docs/user/guides/complete-project-loading.md), [scan workflow](https://github.com/enhantica/edi/blob/main/docs/user/guides/sequential-fitting-in-the-app.md).
