# Experiments and data

An experiment describes the measurement and the model used to calculate it. For powder diffraction, that includes instrument and peak-profile settings, background, exclusions and linked structures.

The shared [Experiment](../user-guide/analysis-workflow/experiment.md) chapter explains the scientific model; the steps below describe this interface.

## Inspect a project

```python
import edi

project = edi.Project.load('path/to/project')

for experiment in project.experiments:
    print(experiment.name)
```

Keep experimental settings with the measurement they describe. Structural parameters belong to a structure, while wavelength, zero shift and profile parameters belong to the experiment model.

## Read a measured powder pattern

For a loaded powder experiment, its data exposes measured intensities and their uncertainties. After a calculation it also carries the calculated intensities:

```python
project.analysis.calculate()

for experiment in project.experiments:
    pattern = experiment.data
    if pattern is not None:
        print(experiment.name, len(pattern.intensity_calc))
```

This snippet is limited to the powder-pattern data view. Single-crystal experiments carry reflections and require the corresponding reflection API.

## Construct an experiment from a data file

For a constant-wavelength neutron powder measurement:

```python
experiment = edi.ExperimentFactory.from_data_path(
    name='measurement',
    data_path='measurement.xye',
    sample_form='powder',
    beam_mode='constant wavelength',
    radiation_probe='neutron',
)
```

The powder reader accepts plain `x y` or `x y sigma` rows, separated by whitespace or commas. It skips nonnumeric lines, estimates uncertainty when omitted, drops nonpositive intensities, sorts the axis and keeps the first repeated-axis point. Review the resulting data when converting an unfamiliar file.

The factory creates the experiment and reads its data. You still need to choose its instrument/profile settings and link a structure before treating it as a complete model.

## Measured data or a simulation range

A measured pattern supports comparison and fitting. A simulation range supports a forward calculation without observations. A project can contain both kinds; fitting uses experiments with measured data.

Read [calculate a pattern](calculate.md) or [load and fit](fit.md) for the next step.

## Related Physics

[Peak profiles](../physics/profiles.md) · [Calibration](../physics/calibration.md) · [Absorption](../physics/corrections/absorption.md) · [Extinction](../physics/corrections/extinction.md) · [Preferred orientation](../physics/corrections/orientation.md).
