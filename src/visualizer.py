import pandas as pd
import matplotlib.pyplot as plt
import os

def visualize(data_cleaned: pd.DataFrame, country_wise_count: pd.DataFrame) -> pd.DataFrame:
    # Create output directory if it doesn't exist
    output_dir = "c:/Users/sumit/OneDrive/Desktop/project work/covid19-data-visualization/outputs/visualizations"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Ensure dates are datetime and sorted so ticks/labels render nicely
    country_wise_count = country_wise_count.copy()
    country_wise_count['Date'] = pd.to_datetime(country_wise_count['Date'])
    country_wise_count = country_wise_count.sort_values('Date')

    # Local import for date formatting
    import matplotlib.dates as mdates

    # Use an automatic date locator + concise formatter for readable x-axis labels
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)

    # Plot total confirmed cases over time (line)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(country_wise_count['Date'], country_wise_count['Confirmed'], marker='o', linewidth=1)
    ax.set_title('Total Confirmed COVID-19 Cases Over Time', fontsize=14)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Number of Confirmed Cases', fontsize=12)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ax.tick_params(axis='x', rotation=45, labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, 'total_confirmed_cases_over_time.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)

    # Plot total deaths over time (line)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(country_wise_count['Date'], country_wise_count['Deaths'], marker='o', color='red', linewidth=1)
    ax.set_title('Total COVID-19 Deaths Over Time', fontsize=14)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Number of Deaths', fontsize=12)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ax.tick_params(axis='x', rotation=45, labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, 'total_deaths_over_time.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)

    # Bar chart for death count (use same locator/formatter for consistent x-axis)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(country_wise_count['Date'], country_wise_count['Deaths'], color='orange')
    ax.set_title('Total COVID-19 Deaths Over Time - Bar Chart', fontsize=14)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Number of Deaths', fontsize=12)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ax.tick_params(axis='x', rotation=45, labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, 'total_deaths_over_time_bar_chart.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)

    return data_cleaned, country_wise_count