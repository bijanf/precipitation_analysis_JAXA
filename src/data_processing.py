import ee
import pandas as pd
from datetime import datetime, timedelta
from tqdm import tqdm
from .config import VALENCIA_COORDS

def get_hourly_precipitation(year):
    """Fetches and processes hourly precipitation data for a given year."""
    monthly_dataframes = []
    cumulative_start = 0  # Initialize cumulative starting value

    for month in tqdm(range(1, 13), desc=f"Processing {year} Monthly Data"):
        start_date, end_date = get_date_range(year, month)
        
        dataset = ee.ImageCollection('JAXA/GPM_L3/GSMaP/v6/operational') \
                    .filterDate(start_date, end_date) \
                    .select('hourlyPrecipRate')
        
        if dataset.size().getInfo() == 0:
            print(f"No data available for {year}-{month:02d}. Skipping this month.")
            continue
        
        try:
            reduced_collection = dataset.map(reduce_to_region)
            df = process_monthly_data(reduced_collection, year, month, cumulative_start)
            cumulative_start = df['cumulative_precip'].iloc[-1]
            monthly_dataframes.append(df)
        
        except Exception as e:
            print(f"An error occurred for {year}-{month:02d}: {e}")
            continue

    return pd.concat(monthly_dataframes, ignore_index=True)

def get_date_range(year, month):
    """Calculate the start and end date for a given year and month."""
    start_date = f'{year}-{month:02d}-01'
    end_date = (datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=32)).replace(day=1).strftime('%Y-%m-%d')
    return start_date, end_date

def reduce_to_region(image):
    """Reduce each image to the maximum precipitation rate over the Valencia region."""
    stats = image.reduceRegion(
        reducer=ee.Reducer.max(),
        geometry=VALENCIA_COORDS,
        scale=10000,
        maxPixels=1e6
    )
    precip = stats.get('hourlyPrecipRate')
    return image.set('date', image.date().format('YYYY-MM-dd HH:mm')).set('precip', precip)

def process_monthly_data(reduced_collection, year, month, cumulative_start):
    """Processes reduced collection into a DataFrame with cumulative precipitation."""
    dates, precip_list = [], []
    for img in reduced_collection.getInfo()['features']:
        properties = img['properties']
        dates.append(properties['date'])
        precip_list.append(properties['precip'])
    
    df = pd.DataFrame({'date': dates, 'precip': precip_list})
    df['date'] = pd.to_datetime(df['date'])
    df['hour_of_year'] = (df['date'] - pd.Timestamp(f'{year}-01-01')).dt.total_seconds() // 3600
    df['cumulative_precip'] = df['precip'].fillna(0).cumsum() + cumulative_start
    df['year'] = year
    df['month'] = month
    return df
