---
template: physics.html
---

# Scientific parameter index

Look up an exact stored parameter name, its units and the scientific section that defines it. The family and selected model determine applicability; this index is not a claim that every parameter is visible or free in every interface. Model-admissibility limits are distinct from optimiser bounds.

A **stored-only** item is retained but does not affect the calculation. A **descriptor** or **fixed** item can configure a model without being an independent fitting direction. Numerical parameters remain subject to symmetry, constraints and observation sensitivity. Dictionary refinability metadata is not the complete fitting contract: selected model, free-set admission and derived values can impose additional restrictions. For an anisotropic site, `adp_iso` is derived from its tensor. `extinction.crystal_radius` is a fixed crystal descriptor, although the dictionary carries numeric parameter metadata for it.

## Cell {#cell}

### `cell.length_a` {#cell-length-a}

Unit-cell length a.

**Units:** Å. **Family:** shared. **Role:** model-parameter. [Equation and explanation](crystallography.md#eq-cell-metric).

### `cell.length_b` {#cell-length-b}

Unit-cell length b.

**Units:** Å. **Family:** shared. **Role:** model-parameter. [Equation and explanation](crystallography.md#eq-cell-metric).

### `cell.length_c` {#cell-length-c}

Unit-cell length c.

**Units:** Å. **Family:** shared. **Role:** model-parameter. [Equation and explanation](crystallography.md#eq-cell-metric).

### `cell.angle_alpha` {#cell-angle-alpha}

Unit-cell angle between b and c (degrees; engine converts to radians).

**Units:** deg. **Family:** shared. **Role:** model-parameter. [Equation and explanation](crystallography.md#eq-cell-metric).

### `cell.angle_beta` {#cell-angle-beta}

Unit-cell angle between a and c (degrees; engine converts to radians).

**Units:** deg. **Family:** shared. **Role:** model-parameter. [Equation and explanation](crystallography.md#eq-cell-metric).

### `cell.angle_gamma` {#cell-angle-gamma}

Unit-cell angle between a and b (degrees; engine converts to radians).

**Units:** deg. **Family:** shared. **Role:** model-parameter. [Equation and explanation](crystallography.md#eq-cell-metric).

## Atom site {#atom-site}

### `atom_site.id` {#atom-site-id}

Unique atom-site identifier.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** shared. **Role:** descriptor. [Equation and explanation](diffraction.md#eq-nuclear-structure-factor).

### `atom_site.type_symbol` {#atom-site-type-symbol}

Chemical symbol of the atom at this site.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** shared. **Role:** descriptor. [Equation and explanation](diffraction.md#eq-nuclear-structure-factor).

### `atom_site.wyckoff_letter` {#atom-site-wyckoff-letter}

Wyckoff letter of the site in its space group.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** shared. **Role:** descriptor. [Equation and explanation](diffraction.md#eq-nuclear-structure-factor).

### `atom_site.adp_type` {#atom-site-adp-type}

Atomic displacement parameter type: Biso, Uiso, Bani, Uani or beta; Biso when absent.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** shared. **Role:** descriptor. [Equation and explanation](displacement.md#eq-isotropic-adp).

### `atom_site.fract_x` {#atom-site-fract-x}

Fractional x-coordinate of the atom site.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** shared. **Role:** model-parameter. [Equation and explanation](diffraction.md#eq-nuclear-structure-factor).

### `atom_site.fract_y` {#atom-site-fract-y}

Fractional y-coordinate of the atom site.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** shared. **Role:** model-parameter. [Equation and explanation](diffraction.md#eq-nuclear-structure-factor).

### `atom_site.fract_z` {#atom-site-fract-z}

Fractional z-coordinate of the atom site.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** shared. **Role:** model-parameter. [Equation and explanation](diffraction.md#eq-nuclear-structure-factor).

### `atom_site.occupancy` {#atom-site-occupancy}

Site occupancy (raw occupancy; m/M multiplicity applied in |F|^2).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** shared. **Role:** model-parameter. [Equation and explanation](diffraction.md#eq-nuclear-structure-factor).

### `atom_site.adp_iso` {#atom-site-adp-iso}

Isotropic atomic displacement parameter in the site's declared type: B for Biso, U for Uiso (B = 8 pi^2 U); an anisotropic site's equivalent isotropic value, derived.

**Units:** Å². **Family:** shared. **Role:** model-parameter. [Equation and explanation](displacement.md#eq-isotropic-adp).

## Atom site aniso {#atom-site-aniso}

### `atom_site_aniso.id` {#atom-site-aniso-id}

The id of the anisotropic atom site the row belongs to.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** shared. **Role:** descriptor. [Equation and explanation](displacement.md#eq-anisotropic-adp).

### `atom_site_aniso.adp_11` {#atom-site-aniso-adp-11}

Anisotropic displacement tensor component 11 (diagonal 11) in the site's declared type: U for Uani, B for Bani (Å²), dimensionless beta for beta.

**Units:** Å² for Uani/Bani; dimensionless for beta. **Family:** shared. **Role:** model-parameter. [Equation and explanation](displacement.md#eq-anisotropic-adp).

### `atom_site_aniso.adp_22` {#atom-site-aniso-adp-22}

Anisotropic displacement tensor component 22 (diagonal 22) in the site's declared type: U for Uani, B for Bani (Å²), dimensionless beta for beta.

**Units:** Å² for Uani/Bani; dimensionless for beta. **Family:** shared. **Role:** model-parameter. [Equation and explanation](displacement.md#eq-anisotropic-adp).

### `atom_site_aniso.adp_33` {#atom-site-aniso-adp-33}

Anisotropic displacement tensor component 33 (diagonal 33) in the site's declared type: U for Uani, B for Bani (Å²), dimensionless beta for beta.

**Units:** Å² for Uani/Bani; dimensionless for beta. **Family:** shared. **Role:** model-parameter. [Equation and explanation](displacement.md#eq-anisotropic-adp).

### `atom_site_aniso.adp_12` {#atom-site-aniso-adp-12}

Anisotropic displacement tensor component 12 (off-diagonal 12) in the site's declared type: U for Uani, B for Bani (Å²), dimensionless beta for beta.

**Units:** Å² for Uani/Bani; dimensionless for beta. **Family:** shared. **Role:** model-parameter. [Equation and explanation](displacement.md#eq-anisotropic-adp).

### `atom_site_aniso.adp_13` {#atom-site-aniso-adp-13}

Anisotropic displacement tensor component 13 (off-diagonal 13) in the site's declared type: U for Uani, B for Bani (Å²), dimensionless beta for beta.

**Units:** Å² for Uani/Bani; dimensionless for beta. **Family:** shared. **Role:** model-parameter. [Equation and explanation](displacement.md#eq-anisotropic-adp).

### `atom_site_aniso.adp_23` {#atom-site-aniso-adp-23}

Anisotropic displacement tensor component 23 (off-diagonal 23) in the site's declared type: U for Uani, B for Bani (Å²), dimensionless beta for beta.

**Units:** Å² for Uani/Bani; dimensionless for beta. **Family:** shared. **Role:** model-parameter. [Equation and explanation](displacement.md#eq-anisotropic-adp).

## Peak {#peak}

### `peak.rise_alpha_0` {#peak-rise-alpha-0}

Back-to-back exponential rise-rate coefficient alpha_0 (rate, 1/us; no closed unit code).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-jorgensen).

### `peak.rise_alpha_1` {#peak-rise-alpha-1}

Back-to-back exponential rise-rate coefficient alpha_1 (alpha(d)=alpha_0+alpha_1/d).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-jorgensen).

### `peak.decay_beta_0` {#peak-decay-beta-0}

Back-to-back exponential decay-rate coefficient beta_0 (rate, 1/us; no closed unit code).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-jorgensen).

### `peak.decay_beta_1` {#peak-decay-beta-1}

Back-to-back exponential decay-rate coefficient beta_1 (beta(d)=beta_0+beta_1/d^4).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-jorgensen).

### `peak.broad_gauss_sigma_0` {#peak-broad-gauss-sigma-0}

Gaussian VARIANCE coefficient sigma_0^2 (variance domain; TCH consumes FWHM_G=sqrt(sigma^2)*sqrt(8 ln 2)).

**Units:** µs². **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-tof-widths).

### `peak.broad_gauss_sigma_1` {#peak-broad-gauss-sigma-1}

Gaussian VARIANCE coefficient sigma_1^2 (d^2 term; variance domain).

**Units:** µs²/Å². **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-tof-widths).

### `peak.broad_gauss_sigma_2` {#peak-broad-gauss-sigma-2}

Gaussian VARIANCE coefficient sigma_2^2 (d^4 term; us^2/A^4 not in closed vocab -> none).

**Units:** µs²/Å⁴. **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-tof-widths).

### `peak.broad_gauss_size` {#peak-broad-gauss-size}

Gaussian isotropic size broadening (variance contribution).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-tof-widths).

### `peak.broad_gauss_strain` {#peak-broad-gauss-strain}

Gaussian isotropic strain broadening (variance contribution).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-tof-widths).

### `peak.broad_lorentz_gamma_0` {#peak-broad-lorentz-gamma-0}

Lorentzian FWHM coefficient gamma_0 (FWHM domain, H_L; consumed as FWHM directly, no sqrt(8 ln 2)).

**Units:** µs. **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-tof-widths).

### `peak.broad_lorentz_gamma_1` {#peak-broad-lorentz-gamma-1}

Lorentzian FWHM coefficient gamma_1 (d term; FWHM domain).

**Units:** µs/Å. **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-tof-widths).

### `peak.broad_lorentz_gamma_2` {#peak-broad-lorentz-gamma-2}

Lorentzian FWHM coefficient gamma_2 (d^2 term; FWHM domain).

**Units:** µs/Å². **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-tof-widths).

### `peak.broad_lorentz_size` {#peak-broad-lorentz-size}

Lorentzian isotropic size broadening (FWHM).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-tof-widths).

### `peak.broad_lorentz_strain` {#peak-broad-lorentz-strain}

Lorentzian isotropic strain broadening (FWHM).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** tof. **Role:** model-parameter. [Equation and explanation](profiles/tof.md#eq-tof-widths).

### `peak.broad_gauss_u` {#peak-broad-gauss-u}

Caglioti Gaussian FWHM coefficient U (tan^2(theta) term; H_G^2 in deg^2).

**Units:** deg². **Family:** cwl. **Role:** model-parameter. [Equation and explanation](profiles/cw.md#eq-tch).

### `peak.broad_gauss_v` {#peak-broad-gauss-v}

Caglioti Gaussian FWHM coefficient V (tan(theta) term; H_G^2 in deg^2).

**Units:** deg². **Family:** cwl. **Role:** model-parameter. [Equation and explanation](profiles/cw.md#eq-tch).

### `peak.broad_gauss_w` {#peak-broad-gauss-w}

Caglioti Gaussian FWHM coefficient W (constant term; H_G^2 in deg^2).

**Units:** deg². **Family:** cwl. **Role:** model-parameter. [Equation and explanation](profiles/cw.md#eq-tch).

### `peak.broad_lorentz_x` {#peak-broad-lorentz-x}

Lorentzian FWHM coefficient X, strain-like (tan(theta) term; H_L in deg).

**Units:** deg. **Family:** cwl. **Role:** model-parameter. [Equation and explanation](profiles/cw.md#eq-tch).

### `peak.broad_lorentz_y` {#peak-broad-lorentz-y}

Lorentzian FWHM coefficient Y, size-like (1/cos(theta) term; H_L in deg).

**Units:** deg. **Family:** cwl. **Role:** model-parameter. [Equation and explanation](profiles/cw.md#eq-tch).

### `peak.mixing_eta_0` {#peak-mixing-eta-0}

Pseudo-Voigt mixing at 2theta = 0: eta = eta_0 + eta_1 2theta (FullProf Eta0).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** cwl. **Role:** model-parameter. [Equation and explanation](profiles/cw.md#eq-caglioti).

### `peak.mixing_eta_1` {#peak-mixing-eta-1}

Pseudo-Voigt mixing slope per degree 2theta: eta = eta_0 + eta_1 2theta (FullProf X of Npr 5).

**Units:** 1/deg. **Family:** cwl. **Role:** model-parameter. [Equation and explanation](profiles/cw.md#eq-caglioti).

### `peak.asym_fcj_1` {#peak-asym-fcj-1}

Finger-Cox-Jephcoat asymmetry parameter 1: S/L, half the sample height over the diffractometer radius.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** cwl. **Role:** model-parameter. [Equation and explanation](profiles/cw.md#eq-fcj).

### `peak.asym_fcj_2` {#peak-asym-fcj-2}

Finger-Cox-Jephcoat asymmetry parameter 2: D/L, half the detector height over the diffractometer radius.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** cwl. **Role:** model-parameter. [Equation and explanation](profiles/cw.md#eq-fcj).

### `peak.asym_beba_a0` {#peak-asym-beba-a0}

Berar-Baldinozzi asymmetry coefficient A0 (Fa/tan theta).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** cwl. **Role:** model-parameter. [Equation and explanation](profiles/cw.md#eq-berar-baldinozzi).

### `peak.asym_beba_b0` {#peak-asym-beba-b0}

Berar-Baldinozzi asymmetry coefficient B0 (Fb/tan theta).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** cwl. **Role:** model-parameter. [Equation and explanation](profiles/cw.md#eq-berar-baldinozzi).

### `peak.asym_beba_a1` {#peak-asym-beba-a1}

Berar-Baldinozzi asymmetry coefficient A1 (Fa/tan 2theta).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** cwl. **Role:** model-parameter. [Equation and explanation](profiles/cw.md#eq-berar-baldinozzi).

### `peak.asym_beba_b1` {#peak-asym-beba-b1}

Berar-Baldinozzi asymmetry coefficient B1 (Fb/tan 2theta).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** cwl. **Role:** model-parameter. [Equation and explanation](profiles/cw.md#eq-berar-baldinozzi).

### `peak.asym_beba_limit` {#peak-asym-beba-limit}

Berar-Baldinozzi limit angle (deg 2theta): reflections at or above it get no asymmetry correction (FullProf AsyLim); default 180.

**Units:** deg. **Family:** cwl. **Role:** fixed. [Equation and explanation](profiles/cw.md#eq-berar-baldinozzi).

## Instrument {#instrument}

### `instrument.calib_d_to_tof_offset` {#instrument-calib-d-to-tof-offset}

TOF calibration zero offset in the active quadratic calibration; the reciprocal field is retained but not applied.

**Units:** µs. **Family:** tof. **Role:** model-parameter. [Equation and explanation](calibration.md#eq-tof-calibration).

### `instrument.calib_d_to_tof_linear` {#instrument-calib-d-to-tof-linear}

TOF calibration linear coefficient Dtt1 (us/A).

**Units:** µs/Å. **Family:** tof. **Role:** model-parameter. [Equation and explanation](calibration.md#eq-tof-calibration).

### `instrument.calib_d_to_tof_quadratic` {#instrument-calib-d-to-tof-quadratic}

TOF calibration quadratic coefficient Dtt2 (us/A^2).

**Units:** µs/Å². **Family:** tof. **Role:** model-parameter. [Equation and explanation](calibration.md#eq-tof-calibration).

### `instrument.calib_d_to_tof_reciprocal` {#instrument-calib-d-to-tof-reciprocal}

TOF calibration reciprocal (1/d) coefficient (us*A); round-tripped, held fixed in the free set.

**Units:** µs·Å. **Family:** tof. **Role:** stored-only. [Equation and explanation](calibration.md#eq-tof-calibration).

### `instrument.calib_twotheta_offset` {#instrument-calib-twotheta-offset}

CW zero-point offset in degrees 2theta, subtracted from the observed axis.

**Units:** deg. **Family:** cwl. **Role:** model-parameter. [Equation and explanation](calibration.md#eq-cwl-calibration).

### `instrument.setup_wavelength` {#instrument-setup-wavelength}

Incident neutron wavelength in angstroms (single wavelength; the doublet tags are X-ray scope).

**Units:** Å. **Family:** cwl. **Role:** model-parameter. [Equation and explanation](calibration.md#eq-cwl-calibration).

### `instrument.calib_sample_displacement` {#instrument-calib-sample-displacement}

CW sample-displacement line shift in degrees 2theta (FullProf SyCos): adds displacement*cos(2theta_B) to each reflection's position.

**Units:** deg. **Family:** cwl. **Role:** model-parameter. [Equation and explanation](calibration.md#eq-line-shifts).

### `instrument.calib_sample_transparency` {#instrument-calib-sample-transparency}

CW sample-transparency line shift in degrees 2theta (FullProf SySin): adds transparency*sin(2theta_B) to each reflection's position.

**Units:** deg. **Family:** cwl. **Role:** model-parameter. [Equation and explanation](calibration.md#eq-line-shifts).

### `instrument.setup_polarization_coefficient` {#instrument-setup-polarization-coefficient}

X-ray CW polarization coefficient K (FullProf Rpolarz): the intensity carries P = 1 - K + K cos^2(2theta_m) cos^2(2theta); 0 disables the correction.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** cwl-xray. **Role:** model-parameter. [Equation and explanation](corrections/intensity.md#eq-xray-polarization).

### `instrument.setup_monochromator_twotheta` {#instrument-setup-monochromator-twotheta}

X-ray CW pre-specimen monochromator angle 2theta_m in degrees (FullProf stores Cthm = cos^2(2theta_m)); 0 means no monochromator.

**Units:** deg. **Family:** cwl-xray. **Role:** model-parameter. [Equation and explanation](corrections/intensity.md#eq-xray-polarization).

### `instrument.setup_wavelength_2` {#instrument-setup-wavelength-2}

X-ray CW second incident wavelength in angstroms (FullProf Lambda2, e.g. Cu K-alpha2); used when setup_wavelength_2_to_1_ratio is not 0.

**Units:** Å. **Family:** cwl-xray. **Role:** model-parameter. [Equation and explanation](corrections/intensity.md#wavelength-doublet).

### `instrument.setup_wavelength_2_to_1_ratio` {#instrument-setup-wavelength-2-to-1-ratio}

X-ray CW intensity of the second wavelength relative to the first (FullProf Ratio); 0 means a single wavelength.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** cwl-xray. **Role:** model-parameter. [Equation and explanation](corrections/intensity.md#wavelength-doublet).

## Absorption {#absorption}

### `absorption.abscor1` {#absorption-abscor1}

TOF sample absorption coefficient ABSCOR1 (muR = ABSCOR1 * lambda; refinable).

**Units:** Å⁻¹. **Family:** tof. **Role:** model-parameter. [Equation and explanation](corrections/absorption.md#eq-hewat).

### `absorption.abscor2` {#absorption-abscor2}

TOF sample absorption lambda-power ABSCOR2 (round-tripped, held fixed; freeing it is a hard error).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** tof. **Role:** stored-only. [Equation and explanation](corrections/absorption.md#eq-hewat).

### `absorption.mu_r` {#absorption-mu-r}

CW cylinder sample absorption mu*R.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** cwl. **Role:** model-parameter. [Equation and explanation](corrections/absorption.md#eq-hewat).

## Extinction {#extinction}

### `extinction.domain_radius` {#extinction-domain-radius}

Becker-Coppens domain (mosaic block) radius r (micrometres; extinction types II and mixed; single crystal; a fit parameter).

**Units:** μm. **Family:** sc. **Role:** model-parameter. [Equation and explanation](corrections/extinction.md#extinction-units).

### `extinction.mosaic_spread` {#extinction-mosaic-spread}

Becker-Coppens mosaic spread g of the crystal, the inverse width of its mosaic distribution (larger is narrower; radians to the minus one; extinction types I and mixed; single crystal; a fit parameter).

**Units:** rad⁻¹. **Family:** sc. **Role:** model-parameter. [Equation and explanation](corrections/extinction.md#extinction-units).

### `extinction.crystal_radius` {#extinction-crystal-radius}

Radius of the crystal taken as a sphere, which sets each reflection's mean path length through it for the Becker-Coppens secondary extinction (millimetres, as _exptl_crystal.size_rad; every Becker-Coppens type; single crystal; a descriptor, never fitted).

**Units:** mm. **Family:** sc. **Role:** descriptor. [Equation and explanation](corrections/extinction.md#extinction-units).

### `extinction.coefficient` {#extinction-coefficient}

Larson's empirical extinction coefficient x, as SHELXL's EXTI: F2calc is multiplied by [1 + 0.001 x F2calc lambda^3 / sin 2theta]^(-1/2) (extinction type larson-isotropic; single crystal; a fit parameter).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** sc. **Role:** model-parameter. [Equation and explanation](corrections/extinction.md#eq-larson).

### `extinction.coefficient_11` {#extinction-coefficient-11}

The term of h² in Larson's anisotropic extinction tensor x_aniso = x11 h^2 + x22 k^2 + x33 l^2 + x12 hk + x13 hl + x23 kl, which takes the place of 4 x (sin theta/lambda)^2 (FullProf's Ext1; extinction type larson-anisotropic; single crystal; a fit parameter).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** sc. **Role:** model-parameter. [Equation and explanation](corrections/extinction.md#eq-larson).

### `extinction.coefficient_22` {#extinction-coefficient-22}

The term of k² in Larson's anisotropic extinction tensor x_aniso = x11 h^2 + x22 k^2 + x33 l^2 + x12 hk + x13 hl + x23 kl, which takes the place of 4 x (sin theta/lambda)^2 (FullProf's Ext2; extinction type larson-anisotropic; single crystal; a fit parameter).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** sc. **Role:** model-parameter. [Equation and explanation](corrections/extinction.md#eq-larson).

### `extinction.coefficient_33` {#extinction-coefficient-33}

The term of l² in Larson's anisotropic extinction tensor x_aniso = x11 h^2 + x22 k^2 + x33 l^2 + x12 hk + x13 hl + x23 kl, which takes the place of 4 x (sin theta/lambda)^2 (FullProf's Ext3; extinction type larson-anisotropic; single crystal; a fit parameter).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** sc. **Role:** model-parameter. [Equation and explanation](corrections/extinction.md#eq-larson).

### `extinction.coefficient_12` {#extinction-coefficient-12}

The term of hk in Larson's anisotropic extinction tensor x_aniso = x11 h^2 + x22 k^2 + x33 l^2 + x12 hk + x13 hl + x23 kl, which takes the place of 4 x (sin theta/lambda)^2 (FullProf's Ext4; extinction type larson-anisotropic; single crystal; a fit parameter).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** sc. **Role:** model-parameter. [Equation and explanation](corrections/extinction.md#eq-larson).

### `extinction.coefficient_13` {#extinction-coefficient-13}

The term of hl in Larson's anisotropic extinction tensor x_aniso = x11 h^2 + x22 k^2 + x33 l^2 + x12 hk + x13 hl + x23 kl, which takes the place of 4 x (sin theta/lambda)^2 (FullProf's Ext5; extinction type larson-anisotropic; single crystal; a fit parameter).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** sc. **Role:** model-parameter. [Equation and explanation](corrections/extinction.md#eq-larson).

### `extinction.coefficient_23` {#extinction-coefficient-23}

The term of kl in Larson's anisotropic extinction tensor x_aniso = x11 h^2 + x22 k^2 + x33 l^2 + x12 hk + x13 hl + x23 kl, which takes the place of 4 x (sin theta/lambda)^2 (FullProf's Ext6; extinction type larson-anisotropic; single crystal; a fit parameter).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** sc. **Role:** model-parameter. [Equation and explanation](corrections/extinction.md#eq-larson).

## Preferred orientation {#preferred-orientation}

### `preferred_orientation.march_r` {#preferred-orientation-march-r}

March-Dollase coefficient r.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** cwl. **Role:** model-parameter. [Equation and explanation](corrections/orientation.md#eq-march-dollase).

### `preferred_orientation.march_random_fract` {#preferred-orientation-march-random-fract}

Random (untextured) fraction mixed with the March-Dollase term.

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** cwl. **Role:** model-parameter. [Equation and explanation](corrections/orientation.md#eq-march-dollase).

## Linked structure {#linked-structure}

### `linked_structure.scale` {#linked-structure-scale}

Scale factor of one linked structure's (phase's) pattern, the overall pattern scale when there is one structure (dimensionless; linear).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** shared. **Role:** model-parameter. [Equation and explanation](diffraction.md#phase-fractions).

## Background {#background}

### `background.intensity` {#background-intensity}

Line-segment background intensity anchor (dimensionless in the reduced pattern; linear).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** pd. **Role:** model-parameter. [Equation and explanation](background.md#eq-line-segment-background).

### `background.position` {#background-position}

Background anchor position on the native pattern axis; a fixed node, not a refinable parameter.

**Units:** degrees 2θ for CW or µs for TOF. **Family:** pd. **Role:** descriptor. [Equation and explanation](background.md#eq-line-segment-background).

### `background.coef` {#background-coef}

Polynomial or Chebyshev background coefficient of the row's order (dimensionless in the reduced pattern; linear).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** pd. **Role:** model-parameter. [Equation and explanation](background.md#eq-chebyshev-background).

### `background.order` {#background-order}

Order m of a polynomial or Chebyshev background term (a non-negative integer; a fixed node, not a refinable Parameter).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** pd. **Role:** descriptor. [Equation and explanation](background.md#eq-chebyshev-background).

### `background.origin` {#background-origin}

Origin of the polynomial background, FullProf Bkpos: the terms are powers of x/origin - 1 (in the pattern's axis units; non-zero).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** pd. **Role:** descriptor. [Equation and explanation](background.md#eq-polynomial-background).

### `background.x_min` {#background-x-min}

Lower end of the Chebyshev background's normalisation domain (in the pattern's axis units).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** pd. **Role:** descriptor. [Equation and explanation](background.md#eq-chebyshev-background).

### `background.x_max` {#background-x-max}

Upper end of the Chebyshev background's normalisation domain (in the pattern's axis units; above x_min).

**Units:** see the quantity and selected model above (no unit supplied by the dictionary). **Family:** pd. **Role:** descriptor. [Equation and explanation](background.md#eq-chebyshev-background).
