# Experiment types and labels

Use these labels to recognise the same measurement in the app, example catalogue and guides. Colour helps scanning; the text identifies the meaning.

An experiment has several independent attributes. For example, the first refinement is <a class="ed-tag ed-tag--technique" href="../user-guide/experiment-types/#powder-diffraction" title="Powder diffraction">pd</a> <a class="ed-tag ed-tag--technique" href="../user-guide/experiment-types/#neutron-diffraction" title="Neutron diffraction">neut</a> <a class="ed-tag ed-tag--neutral" href="../user-guide/experiment-types/#constant-wavelength" title="Constant wavelength">cwl</a>.

Choose the measurement type before loading data. The app enables combinations it currently supports; a listed attribute does not imply every combination is available. [See the experiment controls](../application/experiments.md).

## Purpose

Simulation calculates a pattern. Fitting compares a model with measured observations.

### Fitting measured data {#fitting}

<a class="ed-tag ed-tag--fitting" href="../user-guide/experiment-types/#fitting" title="Fitting measured data">Fitting</a> Simulation calculates a pattern. Fitting compares a model with measured observations.

### Calculation without measured data {#simulation}

<a class="ed-tag ed-tag--simulation" href="../user-guide/experiment-types/#simulation" title="Calculation without measured data">Simulation</a> Simulation calculates a pattern. Fitting compares a model with measured observations.

## Fitting mode

Choose how experiments contribute to a fit. This is separate from their measurement type.

### Fit one experiment {#single-fit}

<a class="ed-tag ed-tag--mode" href="../user-guide/experiment-types/#single-fit" title="Fit one experiment">Single</a> Refine one experiment.

### Fit several experiments together {#joint-fit}

<a class="ed-tag ed-tag--mode" href="../user-guide/experiment-types/#joint-fit" title="Fit several experiments together">Joint</a> Refine several experiments together with shared model quantities.

### Fit a scan using the preceding result {#sequential-fit}

<a class="ed-tag ed-tag--mode" href="../user-guide/experiment-types/#sequential-fit" title="Fit a scan using the preceding result">Sequential</a> Fit a scan in order, using the preceding result as the next starting point.

### Fit a scan from common starting values {#independent-fit}

<a class="ed-tag ed-tag--mode" href="../user-guide/experiment-types/#independent-fit" title="Fit a scan from common starting values">Independent</a> Fit each dataset from the same starting model.

## Sample form

Powder profiles contain overlapping reflections; single-crystal data identify individual reflections.

### Powder diffraction {#powder-diffraction}

<a class="ed-tag ed-tag--technique" href="../user-guide/experiment-types/#powder-diffraction" title="Powder diffraction">pd</a> Diffraction from many crystallite orientations, usually measured as an intensity profile.

### Single-crystal diffraction {#single-crystal-diffraction}

<a class="ed-tag ed-tag--neutral" href="../user-guide/experiment-types/#single-crystal-diffraction" title="Single-crystal diffraction">sc</a> Diffraction from an oriented crystal, measured as individual reflection intensities.

## Probe

Neutrons and X-rays interact with the sample differently. Select the probe used for the measurement.

### Neutron diffraction {#neutron-diffraction}

<a class="ed-tag ed-tag--technique" href="../user-guide/experiment-types/#neutron-diffraction" title="Neutron diffraction">neut</a> Diffraction using neutrons; nuclear scattering and, where modelled, magnetic scattering contribute.

### X-ray diffraction {#x-ray-diffraction}

<a class="ed-tag ed-tag--neutral" href="../user-guide/experiment-types/#x-ray-diffraction" title="X-ray diffraction">xray</a> Diffraction using X-rays; the scattering model depends on the electron distribution.

## Beam mode

Constant-wavelength powder data use scattering angle; time-of-flight data use arrival time and an instrument calibration.

### Constant wavelength {#constant-wavelength}

<a class="ed-tag ed-tag--neutral" href="../user-guide/experiment-types/#constant-wavelength" title="Constant wavelength">cwl</a> A specified incident wavelength; powder patterns are commonly expressed against 2θ.

### Time of flight {#time-of-flight}

<a class="ed-tag ed-tag--technique" href="../user-guide/experiment-types/#time-of-flight" title="Time of flight">tof</a> Neutron wavelengths are separated by arrival time. Calibration relates flight time to diffraction geometry.

## Scattering type

Bragg diffraction describes the crystalline contribution from lattice reflections.

### Bragg diffraction {#bragg-diffraction}

<a class="ed-tag ed-tag--technique" href="../user-guide/experiment-types/#bragg-diffraction" title="Bragg diffraction">Bragg</a> Bragg diffraction describes the crystalline contribution from lattice reflections.

## Next steps

[Choose an example](examples.md) · [Fitting modes](fitting-modes.md) · [Instrument and profiles](../physics/profiles.md)
