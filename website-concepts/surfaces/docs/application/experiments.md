---
template: gui.html
---

# :material-microscope: Experiments and measured data

An experiment connects the measurement to the structural model. It holds measured data or a simulation range, instrument settings, peak and background descriptions, excluded regions, and links to the structures that contribute to its calculation.

The shared [Experiment](../user-guide/analysis-workflow/experiment.md) chapter explains the scientific model; the steps below describe this interface.

## Select or create an experiment

On **Experiment**, select the experiment you want to inspect. **Create experiment** adds an experiment linked to the project's current structures. Before loading measured data you can choose its type and simulation range.

A project can hold experiments with data and experiments without data. Calculation covers them all; fitting uses those with measured data.

<!-- gui-guide:select-or-create-an-experiment -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-create.png?v=3252c0fe1deb" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Load or create an experiment"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Load or create an experiment"><title>Load or create an experiment</title><defs><clipPath id="gui-clip-guide-experiment-create-overview-experiments-select-or-create-an-experiment-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-create.png?v=3252c0fe1deb" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-create-overview-experiments-select-or-create-an-experiment-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-create-overview-experiments-select-or-create-an-experiment-0-1" data-gui-parts="[[784,400,218,39]]" d="M782.000 398.000 L1004.000 398.000 L1004.000 441.000 L782.000 441.000 Z" /><path class="" data-gui-region="guide-experiment-create-overview-experiments-select-or-create-an-experiment-0-2" data-gui-parts="[[1016,400,218,39]]" d="M1014.000 398.000 L1236.000 398.000 L1236.000 441.000 L1014.000 441.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>
<figcaption>Load or create an experiment.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-create-overview-experiments-select-or-create-an-experiment-0-1" aria-pressed="true">1. <span class="gui-fa" aria-hidden="true">&#61587;</span>Load experiment</button> Import the experiment file, including measured intensities and instrument settings.</li><li><button type="button" data-gui-target="guide-experiment-create-overview-experiments-select-or-create-an-experiment-0-2" aria-pressed="false">2. <span class="gui-fa" aria-hidden="true">&#61525;</span>Create experiment</button> Add an experiment and choose its measurement type.</li></ol>
</figure>
<!-- /gui-guide -->

## Load a powder pattern

Choose **Load data…** in the **File** cell. Supported text input contains `x y` or `x y sigma` columns, separated by spaces, tabs or commas. The chooser offers `.xye`, `.xy`, `.dat`, `.txt` and `.csv` files.

| Axis | Meaning of x |
| --- | --- |
| Constant-wavelength powder | 2θ in degrees |
| Time-of-flight powder | Time of flight in microseconds |

The reader skips headers and other lines that do not contain the expected numeric columns. It sorts the retained rows by `x` and keeps the first row when an `x` value is repeated. It skips non-positive intensities.

When no uncertainty column is provided, the reader derives an uncertainty from the intensity. Very small uncertainty values are replaced according to the import rule. Read the message after loading to see what was changed; the [source guide](https://github.com/enhantica/edi/blob/main/docs/user/guides/projects-from-scratch-in-the-app.md) specifies the numeric rules.

After loading, the range fields reflect the data and the experiment type cannot be changed. The instrument, peak, background and excluded regions are retained. Clicking the file name loads replacement data, and Undo restores the preceding state.

<!-- gui-guide:load-a-powder-pattern -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-data.png?v=3252c0fe1deb" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Select an experiment or load measured data"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Select an experiment or load measured data"><title>Select an experiment or load measured data</title><defs><clipPath id="gui-clip-guide-experiment-data-overview-experiments-load-a-powder-pattern-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-data.png?v=3252c0fe1deb" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-data-overview-experiments-load-a-powder-pattern-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-data-overview-experiments-load-a-powder-pattern-0-1" data-gui-parts="[[784,168,682,78]]" d="M782.000 166.000 L1468.000 166.000 L1468.000 248.000 L782.000 248.000 Z" /><path class="" data-gui-region="guide-experiment-data-overview-experiments-load-a-powder-pattern-0-2" data-gui-parts="[[958,207,53.609375,39]]" d="M956.000 205.000 L1013.609 205.000 L1013.609 248.000 L956.000 248.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>
<figcaption>Select an experiment or load measured data.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-data-overview-experiments-load-a-powder-pattern-0-1" aria-pressed="true">1. Experiments</button> Select the measurement to inspect.</li><li><button type="button" data-gui-target="guide-experiment-data-overview-experiments-load-a-powder-pattern-0-2" aria-pressed="false">2. Measured-data file</button> Load the observed intensities for this experiment.</li></ol>
</figure>
<!-- /gui-guide -->

## Instrument and peak profile

Choose settings that match the measurement. The instrument describes quantities such as [wavelength](../physics/calibration.md#eq-cwl-calibration) or the [calibration of the time-of-flight axis](../physics/calibration.md#eq-tof-calibration). The peak profile describes the shape and broadening of the calculated reflections.

A profile that is appropriate for one measurement is not automatically appropriate for another. Start from a relevant example or the instrument's known conditions, then inspect the peak positions and widths before fitting.

<!-- gui-guide:instrument-and-peak-profile -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-instrument.png?v=d9d124ce709f" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Inspect instrument parameters"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Inspect instrument parameters"><title>Inspect instrument parameters</title><defs><clipPath id="gui-clip-guide-experiment-instrument-overview-experiments-instrument-and-peak-profile-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-instrument.png?v=d9d124ce709f" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-instrument-overview-experiments-instrument-and-peak-profile-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-instrument-overview-experiments-instrument-and-peak-profile-0-1" data-gui-parts="[[770,203,710,189]]" d="M768.000 201.000 L1482.000 201.000 L1482.000 394.000 L768.000 394.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>
<figcaption>Inspect instrument parameters.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-instrument-overview-experiments-instrument-and-peak-profile-0-1" aria-pressed="true">1. <span class="gui-fa" aria-hidden="true">&#62992;</span>Instrument</button> </li></ol>
</figure>

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-profile.png?v=a96021f6be73" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Choose and inspect a peak profile"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Choose and inspect a peak profile"><title>Choose and inspect a peak profile</title><defs><clipPath id="gui-clip-guide-experiment-profile-overview-experiments-instrument-and-peak-profile-1"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-profile.png?v=a96021f6be73" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-profile-overview-experiments-instrument-and-peak-profile-1)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-profile-overview-experiments-instrument-and-peak-profile-1-1" data-gui-parts="[[770,245,710,189]]" d="M768.000 243.000 L1482.000 243.000 L1482.000 436.000 L768.000 436.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>
<figcaption>Choose and inspect a peak profile.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-profile-overview-experiments-instrument-and-peak-profile-1-1" aria-pressed="true">1. <span class="gui-fa" aria-hidden="true">&#63007;</span>Peak profile</button> </li></ol>
</figure>
<!-- /gui-guide -->

## Background and exclusions

Use the **Background** group to set or estimate the background. Use **Excluded regions** to omit intervals that should not contribute to the fit. Record a scientific reason for excluding an interval; an exclusion changes the data the fit uses.

The [background guide](background.md) explains manual and automatic estimation.

<!-- gui-guide:background-and-exclusions -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-background.png?v=26e09d16e703" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Inspect the background representation and values"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Inspect the background representation and values"><title>Inspect the background representation and values</title><defs><clipPath id="gui-clip-guide-experiment-background-overview-experiments-background-and-exclusions-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-background.png?v=26e09d16e703" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-background-overview-experiments-background-and-exclusions-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-background-overview-experiments-background-and-exclusions-0-1" data-gui-parts="[[784,210,339.25,56]]" d="M782.000 208.000 L1125.250 208.000 L1125.250 268.000 L782.000 268.000 Z" /><path class="" data-gui-region="guide-experiment-background-overview-experiments-background-and-exclusions-0-2" data-gui-parts="[[784,210,682,337.5]]" d="M782.000 208.000 L1468.000 208.000 L1468.000 549.500 L782.000 549.500 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>
<figcaption>Inspect the background representation and values.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-background-overview-experiments-background-and-exclusions-0-1" aria-pressed="true">1. Background model</button> Choose the background representation.</li><li><button type="button" data-gui-target="guide-experiment-background-overview-experiments-background-and-exclusions-0-2" aria-pressed="false">2. Background values</button> Inspect or edit the values in the selected representation.</li></ol>
</figure>

<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-exclusions.png?v=f01745c5a547" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Inspect excluded fitting intervals"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Inspect excluded fitting intervals"><title>Inspect excluded fitting intervals</title><defs><clipPath id="gui-clip-guide-experiment-exclusions-overview-experiments-background-and-exclusions-1"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-exclusions.png?v=f01745c5a547" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-exclusions-overview-experiments-background-and-exclusions-1)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-exclusions-overview-experiments-background-and-exclusions-1-1" data-gui-parts="[[784,336,682,117]]" d="M782.000 334.000 L1468.000 334.000 L1468.000 455.000 L782.000 455.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>
<figcaption>Inspect excluded fitting intervals.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-exclusions-overview-experiments-background-and-exclusions-1-1" aria-pressed="true">1. Excluded intervals</button> Set the boundaries of regions omitted from fitting.</li></ol>
</figure>
<!-- /gui-guide -->

## Linked structures

The **Linked structures** group lists the structures that contribute to the experiment and their [scale factors](../physics/diffraction.md#occupancy-and-scale). Check that the intended structure is linked and enabled.

Several structures can contribute to one experiment. The displayed [weight fractions](../physics/diffraction.md#phase-fractions) are derived from the scales; they are not an independent input field.

<!-- gui-guide:linked-structures -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/guide-experiment-links.png?v=01cd81e73ff0" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Link structures and inspect phase scales"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Link structures and inspect phase scales"><title>Link structures and inspect phase scales</title><defs><clipPath id="gui-clip-guide-experiment-links-overview-experiments-linked-structures-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/guide-experiment-links.png?v=01cd81e73ff0" width="1480" height="800" clip-path="url(#gui-clip-guide-experiment-links-overview-experiments-linked-structures-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="guide-experiment-links-overview-experiments-linked-structures-0-1" data-gui-parts="[[784,378,682,78]]" d="M782.000 376.000 L1468.000 376.000 L1468.000 458.000 L782.000 458.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>
<figcaption>Link structures and inspect phase scales.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="guide-experiment-links-overview-experiments-linked-structures-0-1" aria-pressed="true">1. Linked structures</button> Inspect phase links, scales and derived fractions.</li></ol>
</figure>
<!-- /gui-guide -->

## Read the pattern

Compare the measured points with the total calculated curve, background and residual. Bragg marks locate the reflection positions. For a scan, the dataset selector chooses which measurement is shown; see [scan fitting](scans.md).

<!-- gui-guide:read-the-pattern -->
<figure class="gui-figure" data-gui-figure>
<a class="gui-image-link" href="../assets/gui/y2o3/10-experiment-loaded.png?v=7f83aefad735" data-gui-open aria-haspopup="dialog" aria-label="Enlarge screenshot: Compare the measured pattern with the initial calculation"><svg class="gui-capture" viewBox="0 0 1480 800" width="1480" height="800" role="img" aria-label="Compare the measured pattern with the initial calculation"><title>Compare the measured pattern with the initial calculation</title><defs><clipPath id="gui-clip-10-experiment-loaded-overview-experiments-read-the-pattern-0"><rect width="1480" height="800" rx="12" /></clipPath></defs><image href="../assets/gui/y2o3/10-experiment-loaded.png?v=7f83aefad735" width="1480" height="800" clip-path="url(#gui-clip-10-experiment-loaded-overview-experiments-read-the-pattern-0)" /><rect class="gui-image-frame" width="1480" height="800" rx="12" /><path class="is-active" data-gui-region="10-experiment-loaded-overview-experiments-read-the-pattern-0-1" data-gui-parts="[[0,77,770,681]]" d="M-2.000 75.000 L772.000 75.000 L772.000 760.000 L-2.000 760.000 Z" /><path class="" data-gui-region="10-experiment-loaded-overview-experiments-read-the-pattern-0-2" data-gui-parts="[[770,119,710,639],[770,77,43.515625,42]]" d="M768.000 117.000 L768.000 117.000 L768.000 75.000 L815.516 75.000 L815.516 117.000 L1482.000 117.000 L1482.000 760.000 L768.000 760.000 Z" /><path data-gui-navigation data-gui-parts="[[727.453125,0,84.90625,77]]" d="M725.453 -2.000 L814.359 -2.000 L814.359 79.000 L725.453 79.000 Z" /></svg></a>
<figcaption>Compare the measured pattern with the initial calculation.</figcaption>
<ol class="gui-regions"><li><button type="button" data-gui-target="10-experiment-loaded-overview-experiments-read-the-pattern-0-1" aria-pressed="true">1. Main workspace</button> Inspect the experiment view here. Its content changes with the active page and selection.</li><li><button type="button" data-gui-target="10-experiment-loaded-overview-experiments-read-the-pattern-0-2" aria-pressed="false">2. Sidebar</button> Use the enabled Main, Extra, Text and Settings tabs to inspect and edit this page.</li></ol>
</figure>
<!-- /gui-guide -->

## Related Physics

[Peak profiles](../physics/profiles.md) · [Calibration](../physics/calibration.md) · [Absorption](../physics/corrections/absorption.md) · [Extinction](../physics/corrections/extinction.md) · [Preferred orientation](../physics/corrections/orientation.md).
