# Short Course on Parametric Survival Analysis

**Course length:** 3–4 hours | **Format:** Slides (PDF) + R code + rendered examples

## Overview

This repository contains the slides, R code, and worked examples for a short
course on **parametric models for survival data**. The course is divided into
two lectures covering overall survival and relative (net) survival respectively,
with a focus on hazard-based regression models and practical implementation in R.

The material is self-contained and suitable for researchers and practitioners
with a basic background in statistics who want to apply parametric survival
models to real data.

## Course structure

### Lecture 1 — Survival Analysis: Parametric Models

**Slides:** [`Lecture1.pdf`](Lecture1.pdf) | **Additional material:** [`Hazard-Based regression models - Overview.pdf`](Hazard-Based%20regression%20models%20-%20Overview.pdf)

Topics covered:

- Aims of survival analysis (overall survival framework)
- Parametric approaches to estimating the survival function
- Proportional Hazards (PH) and Accelerated Failure Time (AFT) regression models
- Software tools and a real data example
- Overview of parametric, semiparametric, and nonparametric alternatives

**R packages:** [HazReg](https://github.com/FJRubio67/HazReg),
[survival](https://cran.r-project.org/web/packages/survival/index.html)

**Worked examples:**
- [Example: no covariates](https://rpubs.com/FJRubio/PSM) — parametric survival
  model without regression
- [Example: regression](https://rpubs.com/FJRubio/PSRM) — PH and AFT models
  with covariates

---

### Lecture 2 — Net Survival Analysis: Parametric Models

**Slides:** [`Lecture2.pdf`](Lecture2.pdf)

Topics covered:

- The relative (net) survival framework
- General hazard structures for excess hazard modelling
- Application in cancer epidemiology
- Challenges in the relative survival framework (life table stratification)

**R packages:** [HazReg](https://github.com/FJRubio67/HazReg),
[GHSurv](https://github.com/FJRubio67/GHSurv),
[GJRM / LBANS](https://github.com/FJRubio67/LBANS),
[SimLT](https://github.com/FJRubio67/SimLT)

**Worked examples:**
- [Parametric excess hazard: Proportional Hazards](https://rpubs.com/FJRubio/GHPH)
- [Parametric excess hazard: General Hazards](https://rpubs.com/FJRubio/GHGH)
- [The Cox Proportional Hazards Model](https://rpubs.com/FJRubio/CPHM)

---

## Requirements

Install the required R packages before running any of the example scripts:

```r
install.packages(c("survival", "flexsurv", "muhaz"))
devtools::install_github("FJRubio67/HazReg")
devtools::install_github("FJRubio67/GHSurv")
devtools::install_github("FJRubio67/SimLT")
```

> Verify exact dependencies against the `library()` calls at the top of each
> script, as the list above may be incomplete.

## Related resources

- [BVSSurv](https://github.com/FJRubio67/BVSSurv) — companion short course on
  Bayesian variable selection for survival data
- [HazReg](https://github.com/FJRubio67/HazReg) — R package for parametric
  hazard-based regression models (overall and relative survival)
- [HazReg](https://github.com/FJRubio67/HazReg) — R package for general hazard
  models in the overall and relative survival frameworks
- [SimLT](https://github.com/FJRubio67/SimLT) — R package for simulating
  survival times from life tables
