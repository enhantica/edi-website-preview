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




## Follow the example in your interface

- [Application: open an included example](../application/examples.md).
- [Python: load and fit an example project](../python/examples.md).
- [Command Line: run an example project](../cli/examples.md).

## Understand the reference

An example may compare a calculated curve or fitted values with FullProf or another reference. Read what is being compared: identical model settings, a program-specific model, or a labelled regression result answer different questions.

Use [fit quality](fit-quality.md) to interpret agreement factors. The references validate the paths and cases they cover; they do not establish every possible model or interface operation.

---

Sources: [edi catalogue](https://github.com/enhantica/edi/blob/main/docs/user/cli/index.md), [LBCO example](https://github.com/enhantica/edi/blob/main/docs/user/cli/pd-neut-cwl_lbco-hrpt/index.md), [LBCO tutorial](https://github.com/enhantica/edi/blob/main/docs/user/tutorials/pd-neut-cwl_lbco-hrpt.py), [tutorial execution declaration](https://github.com/enhantica/edi/blob/main/docs/user/tutorials/execution-exclusions.yml).
