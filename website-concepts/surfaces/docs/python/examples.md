# Example refinement in Python

Download the [notebook](../assets/interfaces/refinement.ipynb) and [example project](../assets/interfaces/example-project.zip). Extract the project beside the notebook, then select a kernel from your [edi environment](setup.md).

## Load the project

<!-- example:python -->
```python
import edi

project = edi.Project.load('pd-neut-cwl_y2o3-spodi')
```
<!-- /example -->

## Refine and inspect

```python
result = project.analysis.fit()
print(f'Rwp: {100 * result.rwp:.2f}%')
print(f'Reduced chi-square: {result.reduced_chi_square:.2f}')
```

The notebook plots measured and calculated arrays with Plotly. Expand its plotting cell to see or change the code. [Inspect results](results.md) describes parameter values and uncertainties.

## Keep the result

```python
project.save_as('refined-project')
project.report.save_html('refinement.html', offline=True)
```

The starting files stay unchanged until you save. See [load and save](projects.md) for other input and output forms.
