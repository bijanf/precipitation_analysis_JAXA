import sys
from pathlib import Path

# Add the root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.data_processing import get_hourly_precipitation
from src.plot_generation import plot_precipitation
import pandas as pd
from tqdm import tqdm

def main():
    years = range(2015, 2025)
    all_years_data = pd.concat([get_hourly_precipitation(year) for year in tqdm(years, desc="Processing Years")])
    plot_precipitation(all_years_data)

if __name__ == "__main__":
    main()
