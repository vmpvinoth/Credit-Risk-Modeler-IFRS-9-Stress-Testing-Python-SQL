# Regulatory References Guide

This document lists all regulatory frameworks, standards, and publications implemented in the IFRS 9 Credit Risk notebook.

---

## 1. IFRS 9 — Financial Instruments

| Property | Detail |
|----------|--------|
| **Issued by** | International Accounting Standards Board (IASB) |
| **Published** | July 2014 (effective January 2018) |
| **Full title** | IFRS 9 Financial Instruments |
| **URL** | https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/ |

### Key Requirements Implemented
- **3-Stage Impairment Model** (§5.5): Stage 1 (12-month ECL), Stage 2 (Lifetime ECL – SICR), Stage 3 (Lifetime ECL – Defaulted)
- **Significant Increase in Credit Risk (SICR)** (§5.5.9): PD-ratio threshold triggering Stage 2 classification
- **Point-in-Time (PIT) PD** (§B5.5.52): Forward-looking PD incorporating macro conditions
- **Multi-Scenario Weighting** (§5.5.17): Probability-weighted ECL across Base, Mild, and Severe scenarios
- **Forward-Looking Information** (§5.5.15): Macro-conditional ECL using GDP, unemployment

---

## 2. Basel III — Advanced IRB Capital Framework

| Property | Detail |
|----------|--------|
| **Issued by** | Basel Committee on Banking Supervision (BCBS) |
| **Document** | CRE36 — Credit Risk: Internal Ratings-Based Approach |
| **Published** | Revised December 2023 |
| **URL** | https://www.bis.org/bcbs/publ/d424.htm |

### Key Requirements Implemented
- **IRB Capital Formula** (CRE36.76): K = LGD × N[(1-R)^(-0.5) × G(PD) + (R/(1-R))^0.5 × G(0.999)] - PD × LGD
- **Asset Correlation (R)**: 0.12 × (1 − e^(−50×PD))/(1 − e^(−50)) + 0.24 × [1 − (1 − e^(−50×PD))/(1 − e^(−50))]
- **Maturity Adjustment** (CRE36.83): b = (0.11852 − 0.05478 × ln(PD))²
- **Risk-Weighted Assets (RWA)**: RWA = K × 12.5 × EAD
- **Minimum Capital (8%)**: Capital requirement = RWA × 8%

---

## 3. SR 11-7 — Model Risk Management

| Property | Detail |
|----------|--------|
| **Issued by** | US Federal Reserve / OCC |
| **Document** | Supervisory Guidance on Model Risk Management (SR 11-7) |
| **Published** | April 2011 |
| **URL** | https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm |

### Key Requirements Implemented
- **Model Development Documentation**: All modelling choices, assumptions, and limitations documented inline
- **Discriminatory Power Validation**: AUC ≥ 0.70, Gini ≥ 0.40 minimum thresholds
- **Calibration Testing**: Brier Score, decile calibration plots
- **Backtesting Framework**: Traffic light system (Green/Amber/Red) by calendar year
- **Out-of-Sample Testing**: Separate train/test split with reported performance gap
- **Limitation Disclosure**: Mandatory SR 11-7 limitations section included

---

## 4. PRA SS 3/19 / SS 8/38 — Stress Testing

| Property | Detail |
|----------|--------|
| **Issued by** | Prudential Regulation Authority (PRA), Bank of England |
| **Document** | SS 3/19: Stress testing of banks (superseded by SS 8/38) |
| **URL** | https://www.bankofengland.co.uk/prudential-regulation/publication/2019/stress-testing-of-banks-ss |

### Key Requirements Implemented
- **Scenario Design**: Base, Mild Stress, Severe Stress (BoE ACS-equivalent)
- **Macro Variable Paths**: GDP growth, unemployment rate over 5-year horizon
- **CET1 Depletion Waterfall**: Capital consumption under each stress scenario
- **Management Action Trigger**: Breach of 7% CET1 conservation buffer floor
- **ICAAP Integration**: Results feed into Internal Capital Adequacy Assessment Process

---

## 5. Bank of England Annual Cyclical Scenario (ACS)

| Property | Detail |
|----------|--------|
| **Issued by** | Bank of England Financial Policy Committee |
| **URL** | https://www.bankofengland.co.uk/stress-testing |

### Scenario Parameters (Approximate ACS 2023)
| Variable | Base | Mild Stress | Severe Stress |
|----------|------|-------------|---------------|
| GDP Growth (Year 1) | +1.5% | −1.0% | −5.0% |
| Unemployment Rate (Peak) | 4.2% | 6.0% | 9.5% |
| CET1 Starting Ratio | 14.0% | 14.0% | 14.0% |

---

## 6. Vasicek Single-Factor Model

| Property | Detail |
|----------|--------|
| **Author** | Oldrich Vasicek |
| **Published** | 1987 (Moody's Analytics white paper) |
| **URL** | https://www.moodysanalytics.com/-/media/whitepaper/before-2011/12-18-03-probability-of-loss-on-loan-portfolio.pdf |

### Formula (PIT PD Conversion)
```
PIT_PD = N[ (N⁻¹(TTC_PD) - √ρ × N⁻¹(GDP_percentile)) / √(1-ρ) ]
```

Where:
- `N(·)` = Cumulative standard normal distribution
- `TTC_PD` = Through-the-cycle PD from logistic regression model
- `ρ` = Asset correlation (from Basel III CRE36 formula)
- `GDP_percentile` = Macro factor (systematic risk driver)

---

## 7. External References

| Source | URL | Purpose |
|--------|-----|---------|
| LendingClub Dataset | https://www.kaggle.com/datasets/wordsforthewise/lending-club | Primary portfolio data |
| FRED API | https://fred.stlouisfed.org | Macroeconomic time series |
| BIS Default Study | https://www.bis.org/bcbs/wp14.htm | Rating-grade default rate benchmarks |
| Emekter et al. (2015) | https://doi.org/10.1080/00036846.2014.962222 | LendingClub statistical benchmarks |
| BCBS Working Paper 14 | https://www.bis.org/bcbs/wp14.htm | Validation of internal models |
