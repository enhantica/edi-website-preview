# :material-microscope: Experiments and measured data

An experiment connects the measurement to the structural model. It holds measured data or a simulation range, instrument settings, peak and background descriptions, excluded regions, and links to the structures that contribute to its calculation.

The shared [Experiment](../user-guide/analysis-workflow/experiment.md) chapter explains the scientific model; the steps below describe this interface.

## Select or create an experiment

On **Experiment**, select the experiment you want to inspect. **Create experiment** adds an experiment linked to the project's current structures. Before loading measured data you can choose its type and simulation range.

A project can hold experiments with data and experiments without data. Calculation covers them all; fitting uses those with measured data.

## Load a powder pattern

Choose **Load data…** in the **File** cell. Supported text input contains `x y` or `x y sigma` columns, separated by spaces, tabs or commas. The chooser offers `.xye`, `.xy`, `.dat`, `.txt` and `.csv` files.

| Axis | Meaning of x |
| --- | --- |
| Constant-wavelength powder | 2θ in degrees |
| Time-of-flight powder | Time of flight in microseconds |

The reader skips headers and other lines that do not contain the expected numeric columns. It sorts the retained rows by `x` and keeps the first row when an `x` value is repeated. It skips non-positive intensities.

When no uncertainty column is provided, the reader derives an uncertainty from the intensity. Very small uncertainty values are replaced according to the import rule. Read the message after loading to see what was changed; the [source guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/projects-from-scratch-in-the-app.md) specifies the numeric rules.

After loading, the range fields reflect the data and the experiment type cannot be changed. The instrument, peak, background and excluded regions are retained. Clicking the file name loads replacement data, and Undo restores the preceding state.

## Instrument and peak profile

Choose settings that match the measurement. The instrument describes quantities such as [wavelength](../physics/calibration.md#eq-cwl-calibration) or the [calibration of the time-of-flight axis](../physics/calibration.md#eq-tof-calibration). The peak profile describes the shape and broadening of the calculated reflections.

A profile that is appropriate for one measurement is not automatically appropriate for another. Start from a relevant example or the instrument's known conditions, then inspect the peak positions and widths before fitting.

## Background and exclusions

Use the **Background** group to set or estimate the background. Use **Excluded regions** to omit intervals that should not contribute to the fit. Record a scientific reason for excluding an interval; an exclusion changes the data the fit uses.

The [background guide](background.md) explains manual and automatic estimation.

## Linked structures

The **Linked structures** group lists the structures that contribute to the experiment and their [scale factors](../physics/diffraction.md#occupancy-and-scale). Check that the intended structure is linked and enabled.

Several structures can contribute to one experiment. The displayed [weight fractions](../physics/diffraction.md#phase-fractions) are derived from the scales; they are not an independent input field.

## Read the pattern

Compare the measured points with the total calculated curve, background and residual. Bragg marks locate the reflection positions. For a scan, the dataset selector chooses which measurement is shown; see [scan fitting](scans.md).

![Experiment controls beside the measured and calculated pattern](../assets/edi-app.png)

## Related Physics

[Peak profiles](../physics/profiles.md) · [Calibration](../physics/calibration.md) · [Absorption](../physics/corrections/absorption.md) · [Extinction](../physics/corrections/extinction.md) · [Preferred orientation](../physics/corrections/orientation.md).
