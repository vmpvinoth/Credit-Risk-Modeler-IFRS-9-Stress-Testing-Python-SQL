"""
download_data.py
----------------
Downloads FRED macroeconomic data required by the IFRS 9 Credit Risk notebook.

Usage:
    python scripts/download_data.py

Datasets downloaded:
    - fred_gdp.csv       : US Real GDP Growth Rate (Quarterly, 1947–present)
    - fred_unrate.csv    : US Unemployment Rate (Monthly, 1948–present)
    - fred_fedfunds.csv  : US Federal Funds Rate (Monthly, 1954–present)

Note: LendingClub data must be downloaded manually from Kaggle.
      See README.md for instructions.
"""

import os
import sys
import requests
from pathlib import Path

# ── Output directory
DATA_DIR = Path(__file__).parent.parent / "data" / "raw"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# ── FRED series to download (no API key required for direct CSV)
FRED_SERIES = {
    "fred_gdp.csv": {
        "url": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=A191RL1Q225SBEA",
        "description": "Real GDP Growth Rate (Quarterly, %)",
    },
    "fred_unrate.csv": {
        "url": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE",
        "description": "US Unemployment Rate (Monthly, %)",
    },
    "fred_fedfunds.csv": {
        "url": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS",
        "description": "Federal Funds Effective Rate (Monthly, %)",
    },
}


def download_file(url: str, dest: Path, description: str) -> bool:
    """Download a single file from URL to destination path."""
    print(f"  Downloading: {description}")
    print(f"    URL  : {url}")
    print(f"    Dest : {dest}")
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        dest.write_bytes(response.content)
        size_kb = dest.stat().st_size / 1024
        print(f"    ✅  Saved ({size_kb:.1f} KB)\n")
        return True
    except requests.RequestException as e:
        print(f"    ❌  Failed: {e}\n")
        return False


def main():
    print("=" * 60)
    print("IFRS 9 Credit Risk — FRED Data Downloader")
    print("=" * 60)
    print(f"Saving to: {DATA_DIR.resolve()}\n")

    results = {}
    for filename, meta in FRED_SERIES.items():
        dest = DATA_DIR / filename
        if dest.exists():
            print(f"  ⏭️  Already exists: {filename} — skipping\n")
            results[filename] = True
            continue
        results[filename] = download_file(meta["url"], dest, meta["description"])

    print("=" * 60)
    success = sum(results.values())
    total = len(results)
    print(f"Download complete: {success}/{total} files successful")

    if success == total:
        print("\n✅  All FRED data ready.")
        print("\n📌 Next step: Download LendingClub data from Kaggle.")
        print("   See README.md for instructions.")
    else:
        failed = [k for k, v in results.items() if not v]
        print(f"\n⚠️  Failed files: {', '.join(failed)}")
        print("   Please download manually from https://fred.stlouisfed.org")
        sys.exit(1)


if __name__ == "__main__":
    main()
