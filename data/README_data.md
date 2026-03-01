# 📂 Data Download Instructions

This project uses **real, publicly available datasets**. Place downloaded files in this `data/` folder.

---

## 1. LendingClub Loan Data (Primary Dataset)

**Source:** Kaggle  
**URL:** https://www.kaggle.com/datasets/wordsforthewise/lending-club  
**Size:** ~1.3 GB compressed | ~3.5 GB uncompressed  
**Records:** 2,260,668 loans (2007–2018)

### Download Steps

#### Option A — Kaggle Website (No CLI needed)
1. Create a free account at https://www.kaggle.com
2. Go to https://www.kaggle.com/datasets/wordsforthewise/lending-club
3. Click **"Download"** (top right)
4. Extract the ZIP file
5. Find the file: `accepted_2007_to_2018Q4.csv`
6. Copy it to this folder and rename to: **`lending_club.csv`**

#### Option B — Kaggle CLI
```bash
# Install Kaggle CLI
pip install kaggle

# Set up API key (from Kaggle Account → API → Create New Token)
# Save kaggle.json to ~/.kaggle/kaggle.json

# Download
kaggle datasets download -d wordsforthewise/lending-club
unzip lending-club.zip
cp accepted_2007_to_2018Q4.csv data/lending_club.csv
```

### Key Columns Used

| Column | Type | Description |
|--------|------|-------------|
| `loan_amnt` | float | Loan amount ($) → EAD |
| `loan_status` | string | 'Fully Paid' / 'Charged Off' → Default flag |
| `grade` | string | A–G credit grade → TTC PD |
| `sub_grade` | string | A1–G5 sub-grade |
| `int_rate` | string | Interest rate (%) → EIR |
| `dti` | float | Debt-to-income ratio → DSR |
| `fico_range_low` | float | FICO credit score lower bound |
| `fico_range_high` | float | FICO credit score upper bound |
| `revol_util` | string | Revolving utilisation (%) → LTV |
| `purpose` | string | Loan purpose → product type / LGD |
| `issue_d` | string | Origination date |
| `recoveries` | float | Post-charge-off recovery amount |
| `total_rec_prncp` | float | Total principal recovered |

---

## 2. Federal Reserve FRED Macroeconomic Data

**Source:** Federal Reserve Bank of St. Louis (FRED)  
**URL:** https://fred.stlouisfed.org  
**Cost:** FREE — no account needed  

### Direct Download Links (CSV)

Copy-paste these URLs into your browser or use curl:

```bash
# GDP Growth (Real, QoQ, Seasonally Adjusted Annual Rate)
# Series: A191RL1Q225SBEA
curl -o data/fred_gdp.csv "https://fred.stlouisfed.org/graph/fredgraph.csv?id=A191RL1Q225SBEA"

# Civilian Unemployment Rate (Monthly, Seasonally Adjusted)
# Series: UNRATE
curl -o data/fred_ue.csv "https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE"

# Federal Funds Effective Rate (Monthly)
# Series: FEDFUNDS
curl -o data/fred_ffr.csv "https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS"
```

### Or Download via Browser
| File | FRED Page | Direct CSV |
|------|-----------|-----------|
| `fred_gdp.csv` | https://fred.stlouisfed.org/series/A191RL1Q225SBEA | https://fred.stlouisfed.org/graph/fredgraph.csv?id=A191RL1Q225SBEA |
| `fred_ue.csv` | https://fred.stlouisfed.org/series/UNRATE | https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE |
| `fred_ffr.csv` | https://fred.stlouisfed.org/series/FEDFUNDS | https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS |

---

## 3. Running Without Data Files

**The notebook works without any downloaded data.** The `DataLoader` class includes a calibrated fallback that generates data with statistics exactly matching the real LendingClub dataset:

- Default rate: ~14.5% (LendingClub 2008–2018 average)
- Grade A–G distribution: calibrated to LC 2018 annual report
- FICO distribution: calibrated to Emekter et al. (2015)
- LGD by purpose: calibrated to LendingClub recovery data

When you download the real data and re-run, the `DataLoader` auto-detects the files and switches to real data automatically.

---

## 4. Data Privacy & Usage

- **LendingClub data**: Publicly released under LendingClub's data sharing programme. No PII in the dataset.
- **FRED data**: US Government data, public domain (17 U.S.C. §105).
- **This project**: For educational and portfolio demonstration purposes only. Results do not constitute financial advice.
