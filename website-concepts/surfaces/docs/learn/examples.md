# Example projects

Examples combine a structure model, experiment settings, data and starting conditions. Use them to learn an analysis before preparing your own files.

The example catalogue connects the interfaces: an example opens in the app, has project files the Command Line can run, and has a Python tutorial using those files. Read the example's description and provenance to understand its starting point and reference result.

## Choose an example

| Interest | Examples to explore | What to learn |
| --- | --- | --- |
| A calculation without measured data | LBCO at constant wavelength; silicon in time of flight; NaCl with laboratory X-rays | Structure, experiment and calculation range |
| A first powder refinement | LBCO on HRPT; Co₂SiO₄ on D20 | Free parameters, profile, background and residual |
| Time-of-flight refinement | Silicon on SEPD; NCAF on WISH | TOF calibration, profiles and multiple banks |
| Several phases or experiments | LBCO with silicon; PbSO₄ neutron and X-ray data | Structural links, scales and joint information |
| A scan | Co₂SiO₄ temperature series; LATP on BM01 | Template, fitting order and parameter evolution |

The [current catalogue](https://github.com/enhantica/edi/blob/main/docs/user/cli/index.md) lists the available projects and links each project page to its tutorial. Example-specific pages carry the reference and any limitations; support should be read from those pages rather than inferred from an example name alone.

## Open one in the app

Open the [web app](https://enhantica.github.io/edi/webapp/), go to **Project**, and expand **Examples**. Choose a measured-data example for [your first refinement](../get-started/first-refinement.md), or choose a simulation to inspect a calculated pattern without fitting.

Examples open as working copies. Use **Save project as…** to keep your changes in your own project.

## Use the same project in Python

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

## Run it from the command line

From the same configured checkout:

```console
python -m edi fit docs/user/cli/pd-neut-cwl_lbco-hrpt/project --dry
```

For a real fit, follow the [Command Line refinement guide](../cli/fit.md). Keep a copy of the starting project so the original inputs remain available.

## Understand the reference

An example may compare a calculated curve or fitted values with FullProf or another reference. Read what is being compared: identical model settings, a program-specific model, or a labelled regression result answer different questions.

Use [fit quality](fit-quality.md) to interpret agreement factors. The references validate the paths and cases they cover; they do not establish every possible model or interface operation.

---

Sources: [edi catalogue](https://github.com/enhantica/edi/blob/main/docs/user/cli/index.md), [LBCO example](https://github.com/enhantica/edi/blob/main/docs/user/cli/pd-neut-cwl_lbco-hrpt/index.md), [LBCO tutorial](https://github.com/enhantica/edi/blob/main/docs/user/tutorials/pd-neut-cwl_lbco-hrpt.py), [tutorial execution declaration](https://github.com/enhantica/edi/blob/main/docs/user/tutorials/execution-exclusions.yml).
