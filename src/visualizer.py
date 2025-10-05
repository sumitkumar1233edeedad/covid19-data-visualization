import pandas as pd
import matplotlib.pyplot as plt
import os

def visualize(data_cleaned: pd.DataFrame, country_wise_count: pd.DataFrame) -> pd.DataFrame:
    # Create output directory if it doesn't exist
    output_dir = "c:/Users/sumit/OneDrive/Desktop/project work/covid19-data-visualization/outputs/visualizations"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Plot total confirmed cases over time
    plt.figure(figsize=(10, 6))
    plt.plot(country_wise_count['Date'], country_wise_count['Confirmed'], marker='o')
    plt.title('Total Confirmed COVID-19 Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Confirmed Cases')
    plt.xticks(rotation=90)
    plt.grid()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'total_confirmed_cases_over_time.png'))
    plt.close()

    # Plot total deaths over time
    plt.figure(figsize=(10, 6))
    plt.plot(country_wise_count['Date'], country_wise_count['Deaths'], marker='o', color='red')
    plt.title('Total COVID-19 Deaths Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Deaths')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'total_deaths_over_time.png'))
    plt.close()

    return data_cleaned, country_wise_count