# Example projects in Python

In a configured edi source environment, the LBCO example can be loaded from its catalogue folder:

```python
import edi

project = edi.Project.load('docs/user/cli/pd-neut-cwl_lbco-hrpt/project')
print(project.metadata.title)
result = project.analysis.fit()
print(result.rwp, result.reduced_chi_square)
```

The path is relative to the edi repository. A downloaded or exported project can be loaded from its own location instead. See [Python setup](../python/setup.md) and [load and fit a project](../python/fit.md).

The tutorial sources are also available in [the repository](https://github.com/enhantica/edi/tree/main/docs/user/tutorials). Their execution status is declared separately; publishing a tutorial does not by itself establish that it is currently part of the automatic notebook-execution suite.

Choose a scientific case in the shared [example catalogue](../user-guide/examples.md).

## Related Physics

[Least-squares objective](../physics/rietveld.md#eq-weighted-residual) · [Minimization and covariance](../physics/minimization.md) · [Agreement factors](../physics/reliability.md).
