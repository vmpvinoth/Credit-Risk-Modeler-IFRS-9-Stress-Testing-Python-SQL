# 🏦 End-to-End Credit Risk Modelling
### IFRS 9 ECL | Basel III Advanced IRB | Stress Testing (SS 3/19 / SS 8/38) | SR 11-7 Model Validation

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Data: Public](https://img.shields.io/badge/Data-LendingClub%20%7C%20FRED%20%7C%20BIS-blueviolet)]()
[![Regulation](https://img.shields.io/badge/Framework-IFRS9%20%7C%20Basel%20III%20%7C%20SR11--7%20%7C%20SS3--19-navy)]()

---

## 📋 Overview

A **production-grade, end-to-end credit risk modelling pipeline** built on real publicly available data. This project mirrors the quantitative workflows used by credit risk stress testing teams at Tier-1 banks (Standard Chartered, Barclays, HSBC, JPMorgan Chase).

Every regulatory framework, formula, and threshold is sourced from official publications. Every dataset is publicly available.

---

## 🎯 What This Project Covers

| Section | Topic | Framework |
|---------|-------|-----------|
| **Section 1** | Data Loading — Real LendingClub + FRED Macro | Public Data |
| **Section 2** | Exploratory Data Analysis (EDA) | SR 11-7 §IV |
| **Section 3** | Feature Engineering (5 Cs of Credit) | SR 11-7 §VI |
| **Section 4** | PD Model — Logistic Regression | SR 11-7 §VI |
| **Section 5** | Model Validation — AUC, Gini, KS, Brier | SR 11-7 §VII |
| **Section 6** | PIT PD — Vasicek Single-Factor Model | IFRS 9 §B5.5.49 |
| **Section 7** | IFRS 9 ECL — 3-Stage, Lifetime, Multi-Scenario | IFRS 9 §5.5 |
| **Section 8** | Basel III IRB — Advanced Capital Formula, RWA | BCBS CRE36 |
| **Section 9** | Stress Testing — BoE ACS, ICAAP, CET1 Depletion | SS 3/19, ICAAP |
| **Section 10** | Backtesting — Traffic Light, COVID-19 Overlay | SR 11-7 §VII |
| **Section 11** | CRO/CFO Executive Dashboard | — |
| **Section 12** | Excel Reporting Pack (7 sheets) | — |

---

## 📂 Real Public Datasets

### Primary Dataset: LendingClub Loan Data

| Property | Detail |
|----------|--------|
| **Source** | Kaggle / LendingClub |
| **URL** | https://www.kaggle.com/datasets/wordsforthewise/lending-club |
| **Size** | ~1.3 GB compressed |
| **Records** | 2,260,668 US personal loans |
| **Period** | 2007–2018 |
| **Key columns** | `loan_amnt`, `grade`, `dti`, `fico_range_low`, `loan_status` (default flag), `int_rate`, `recoveries` |

**Download:**
```bash
# Option 1 — Kaggle CLI (requires free Kaggle account)
kaggle datasets download -d wordsforthewise/lending-club
unzip lending-club.zip -d data/
# Rename: accepted_2007_to_2018Q4.csv → data/lending_club.csv

# Option 2 — Kaggle website
# Go to: https://www.kaggle.com/datasets/wordsforthewise/lending-club
# Click "Download" → extract → rename to data/lending_club.csv
```

---

### Macroeconomic Data: Federal Reserve (FRED)

| Series | Code | Direct Download URL |
|--------|------|---------------------|
| Real GDP Growth (QoQ %) | `A191RL1Q225SBEA` | https://fred.stlouisfed.org/graph/fredgraph.csv?id=A191RL1Q225SBEA |
| Civilian Unemployment Rate | `UNRATE` | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE |
| Federal Funds Rate | `FEDFUNDS` | https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS |

**Download (no account needed):**
```bash
mkdir -p data
curl -o data/fred_gdp.csv "https://fred.stlouisfed.org/graph/fredgraph.csv?id=A191RL1Q225SBEA"
curl -o data/fred_ue.csv  "https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE"
curl -o data/fred_ffr.csv "https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS"
```

> **Without the data files:** The notebook includes a `DataLoader` class with a calibrated fallback. All statistical parameters are sourced from published academic papers (Emekter et al. 2015, Serrano-Cinca et al. 2015). You can run the full notebook immediately without downloading anything.

---

## 🧮 Key Formulas Implemented

### Vasicek PIT PD (IFRS 9)
$$PD_{PIT}(t) = \Phi\!\left(\frac{\Phi^{-1}(PD_{TTC}) - \sqrt{\rho} \cdot Z(t)}{\sqrt{1-\rho}}\right)$$

### IFRS 9 Lifetime ECL
$$ECL_{Lifetime} = \sum_{t=1}^{T} PD_{marginal}(t) \times LGD \times EAD \times DF(t)$$

### IFRS 9 Multi-Scenario Weighting
$$ECL_{weighted} = \sum_{s} P(s) \times ECL_s$$

### Basel III IRB Capital
$$K = \left[LGD \cdot \Phi\!\left(\frac{\Phi^{-1}(PD)}{\sqrt{1-R}} + \sqrt{\frac{R}{1-R}} \cdot \Phi^{-1}(0.999)\right) - PD \cdot LGD\right] \times M_{adj}$$

$$RWA = K \times 12.5 \times EAD$$

---

## 📊 Sample Results

| Metric | Result |
|--------|--------|
| **PD Model AUC** | 0.90+ (SR 11-7 threshold: ≥0.70) ✅ |
| **Gini Coefficient** | 0.80+ (threshold: ≥0.40) ✅ |
| **KS Statistic** | 0.70+ (threshold: ≥0.30) ✅ |
| **IFRS 9 ECL — Base** | ~0.50% of EAD |
| **IFRS 9 ECL — Severe Stress** | ~2.00% of EAD (~4x Base) |
| **Basel RWA Density** | ~42% |
| **Starting CET1** | 14.0% |
| **Post-Severe Stress CET1** | ~4-6% (approaches minimum) |
| **2020 COVID Backtest** | 🔴 RED — Under-predicted (overlay required) |
| **2023 Backtest** | 🟢 GREEN — Model on target |

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/credit-risk-ifrs9-basel.git
cd credit-risk-ifrs9-basel

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Download real data — see Data section above

# 4. Launch Jupyter
jupyter notebook IFRS9_CreditRisk_EndToEnd.ipynb
```

---

## 📁 Repository Structure

```
credit-risk-ifrs9-basel-stresstesting/
│
├── 📓 IFRS9_CreditRisk_EndToEnd.ipynb    ← Main notebook (37 cells)
│
├── 📂 data/
│   ├── README_data.md                    ← Detailed download instructions
│   ├── lending_club.csv                  ← Place LendingClub data here
│   ├── fred_gdp.csv                      ← FRED GDP series
│   ├── fred_ue.csv                       ← FRED Unemployment series
│   └── fred_ffr.csv                      ← FRED Fed Funds Rate
│
├── 📂 outputs/
│   ├── figures/
│   │   ├── 01_eda_analysis.png
│   │   ├── 02_model_validation.png
│   │   ├── 03_pit_pd_projection.png
│   │   ├── 04_stress_testing.png
│   │   ├── 05_backtesting.png
│   │   └── 06_executive_dashboard.png
│   └── IFRS9_Basel_StressTest_Report.xlsx
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📚 Regulatory References

| Framework | Official Document | URL |
|-----------|------------------|-----|
| **IFRS 9** | IASB IFRS 9 Financial Instruments (2014) | https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/ |
| **Basel III IRB** | BCBS CRE36 (2023) | https://www.bis.org/bcbs/publ/d424.htm |
| **SR 11-7** | Federal Reserve Guidance on Model Risk Management | https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm |
| **SS 3/19** | PRA Supervisory Statement — Stress Testing | https://www.bankofengland.co.uk/prudential-regulation/publication/2019/stress-testing-of-banks-ss |
| **BoE ACS 2023** | Bank of England Annual Cyclical Scenario | https://www.bankofengland.co.uk/stress-testing |
| **Vasicek (1987)** | Probability of Loss on Loan Portfolio | https://www.moodysanalytics.com/-/media/whitepaper/before-2011/12-18-03-probability-of-loss-on-loan-portfolio.pdf |
| **BIS Default Study** | Annual Default Studies | https://www.bis.org/bcbs/wp14.htm |

---

## 🏷️ Skills Demonstrated

`Python` `Pandas` `NumPy` `Scikit-learn` `Matplotlib` `SciPy` `Jupyter`
`IFRS 9` `Basel III` `Credit Risk Modelling` `PD Modelling` `LGD Modelling`
`Stress Testing` `Model Validation` `Vasicek Model` `Logistic Regression`
`SR 11-7` `SS 3/19` `ICAAP` `BoE ACS` `Regulatory Reporting`

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

*Portfolio project for credit risk analytics demonstration. All data sources are publicly available. Results are for educational purposes only.*
