---
template: physics.html
---

# Reliability factors

Reliability factors summarise agreement under a defined observation model. They supplement the pattern, residual, physical model and parameter uncertainties.

## Included observations and weights {#factor-observations}

For powder factors, sums run over included points outside excluded intervals with positive standard uncertainty and available finite calculated intensity. Let $w_i=1/\sigma_i^2$, $b_i$ be background, $N$ the included point count and $P$ the independent free-parameter count.

## Powder profile factors {#eq-profile-factors}

$$R_p=\frac{\sum_i|y_{o,i}-y_{c,i}|}{\sum_i|y_{o,i}|},\qquad
R_{wp}=\sqrt{\frac{\sum_iw_i(y_{o,i}-y_{c,i})^2}{\sum_iw_i y_{o,i}^2}},$$

$$R_{\exp}=\sqrt{\frac{N-P}{\sum_iw_i y_{o,i}^2}},\qquad
\chi^2_{\rm red}=\frac{\sum_iw_i(y_{o,i}-y_{c,i})^2}{N-P}.$$

The engine's factor values are fractions; a displayed percentage is 100 times that fraction. $R_{wp}/R_{\exp}$ is the square root of reduced χ² under matching sums and degrees of freedom. The name “goodness of fit” is used for both conventions in the literature, so state which is meant.

A fit needs positive degrees of freedom to interpret reduced χ². Nonpositive degrees of freedom or a zero denominator are degenerate cases; the report's numerical guard result is not a statistically meaningful factor.

## Background-subtracted factors {#eq-background-subtracted-factors}

The conventional background-subtracted factors retain the same residual numerator but replace the normalising observations by net intensity:

$$cR_p=\frac{\sum_i|y_{o,i}-y_{c,i}|}{\sum_i|y_{o,i}-b_i|},\qquad
cR_{wp}=\sqrt{\frac{\sum_iw_i(y_{o,i}-y_{c,i})^2}{\sum_iw_i(y_{o,i}-b_i)^2}},$$

$$cR_{\exp}=\sqrt{\frac{N-P}{\sum_iw_i(y_{o,i}-b_i)^2}}.$$

Removing background from the denominator can change the apparent factor substantially. Do not compare a conventional profile Rwp directly with a background-subtracted value while calling them the same definition.

## Bragg and F factors {#eq-bragg-factors}

Powder phase factors use reflection intensities apportioned from the observed profile according to the calculated contributions:

$$I_{o,h}=\sum_i I_{c,h}(i)\frac{y_{o,i}-b_i}{y_{c,i}-b_i},\qquad
R_B=\frac{\sum_h|I_{o,h}-I_{c,h}|}{\sum_h|I_{o,h}|}.$$

$$|F_{c,h}|=\sqrt{m_h|F_h|^2},\qquad |F_{o,h}|=|F_{c,h}|\sqrt{\max(I_{o,h},0)/I_{c,h}},\qquad
R_F=\frac{\sum_h\big||F_{o,h}|-|F_{c,h}|\big|}{\sum_h|F_{o,h}|}.$$

The reflection partition is model-dependent, particularly where peaks overlap. These phase factors are not independent directly measured integrated intensities for every powder reflection.

## Single-crystal and pooled results {#pooled-factors}

For a single-crystal reflection list, the same absolute and weighted formulas operate on observed and calculated $F^2$ values, giving $R(F^2)$ and $wR(F^2)$. There is no powder background partition; the background-subtracted denominators equal the un-subtracted ones. Do not label this intensity-based factor as the amplitude-based $R(F)$.

Per-experiment factors use that experiment's included observations. Pooled factors combine the underlying sums across experiments; they are not an arithmetic average of each experiment's R factor. Keep the objective weighting and factor definition explicit when interpreting joint fits.

## Interpretation and references

There is no universal threshold that proves structural correctness. Changing the data range, uncertainty estimates, background, excluded observations or free set changes the statistic. See [assessing a fit](../user-guide/fit-quality.md).

McCusker et al. (1999), *Rietveld refinement guidelines*, J. Appl. Cryst. 32, 36–50; Toby (2006), *R factors in Rietveld analysis: How good is good enough?*, Powder Diffraction 21, 67–70. Definitions here also follow the [documented EasyDiffraction fit-quality convention](https://github.com/enhantica/edi/blob/main/docs/user/guides/fit-quality.md), extended with the background-subtracted and phase factors described above.
