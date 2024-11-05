# Precipitation Analysis Over Valencia

This project analyzes cumulative precipitation data over a 200 km radius around Valencia, Spain, using the GPM GSMaP dataset via the Google Earth Engine API.

## Features
- Fetches hourly precipitation data over a specified area for multiple years
- Aggregates monthly data and calculates cumulative precipitation
- Plots cumulative precipitation over time

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/precipitation_analysis.git
   cd precipitation_analysis
   ```
2. Install Dependencies:
   
   ```bash
      pip install -r requirements.txt
   ```

3. Authenticate with Earth Engine API:
   ```bash
   earthengine authenticate
   ```

## Usage

To run the analysis:

```bash
   python scripts/run_analysis.py
```

The script fetches precipitation data and plots cumulative values across years, saving the result as `cumulative_sum_precipitation_valencia_hourly.png`.

## Project Structure

src/: Contains modular code for data fetching (data_processing.py), plotting (plot_generation.py), and configuration (config.py).
scripts/: Entry point script (run_analysis.py) to execute the analysis.
requirements.txt: Lists necessary Python packages.


## Data Source

The precipitation data is retrieved from the JAXA/GPM_L3/GSMaP.

## License

This project is licensed under the MIT License.
