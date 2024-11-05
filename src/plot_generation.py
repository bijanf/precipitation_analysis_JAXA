import matplotlib.pyplot as plt

def plot_precipitation(all_years_data):
    """Plots the cumulative precipitation for multiple years."""
    plt.figure(figsize=(12, 8))
    for year in all_years_data['year'].unique():
        yearly_data = all_years_data[all_years_data['year'] == year]
        if year == 2024:
            plt.plot(yearly_data['hour_of_year'], yearly_data['cumulative_precip'], color='red', label=f"{year} (Current Year)", linewidth=2.5)
        else:
            plt.plot(yearly_data['hour_of_year'], yearly_data['cumulative_precip'], color='gray', alpha=0.6, label='since 2015' if year == all_years_data['year'].unique()[0] else None)
    
    plt.title("Cumulative Hourly Total Precipitation Time-Series \n  maximum value over Valencia region with 200 km radius (Satellite Data GSMaP)")
    plt.xlabel("Hour of the Year")
    plt.ylabel("Cumulative Precipitation (mm)")
    plt.legend()
    plt.grid(True)
    plt.savefig("cumulative_sum_precipitation_valencia_hourly.png", dpi=300, bbox_inches='tight', pad_inches=0)
    plt.show()
