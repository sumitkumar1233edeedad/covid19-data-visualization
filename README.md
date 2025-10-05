🌍 COVID-19 Data Visualization

Visualize COVID-19 cases over time using Pandas and Matplotlib.
Analyze trends, spikes, and rolling averages with real-world datasets.

📖 Table of Contents

About

Dataset

Features

Folder Structure

Installation

Usage

Example Plots

Applications

Future Scope

License

📝 About

This project demonstrates how to load, clean, and visualize COVID-19 case data.
You can plot:

Total cases

Daily new cases

7-day moving averages

for any country or worldwide.

📊 Dataset

We use the Our World in Data (OWID) COVID-19 dataset.

Source: Our World in Data – COVID-19 Data

Format: CSV, updated daily

Columns: date, location, total_cases, new_cases, total_deaths, population

Save it locally as:

data/owid-covid-data.csv

✨ Features

Load global or country-level COVID-19 data

Handle missing values and parse dates

Plot:

Total cases over time

Daily new cases with 7-day rolling average

Optional log-scale charts

Export plots as PNG for reports

📂 Folder Structure
 covid19-data-visualization/
├── src/
│   ├── main.py            # Orchestrates loading, cleaning, plotting
│   ├── data_loader.py     # Reads CSV files
│   ├── cleaner.py         # Handles NaNs, fixes columns, filters dates
│   ├── analyzer.py        # Calculates totals, moving avg, growth
│   └── visualizer.py      # Builds all charts
├── data/
│   ├── raw/               # Original Kaggle CSV files
│   └── cleaned/           # Processed data (optional)
├── outputs/
│   ├── plots/             # Saved PNG charts
│   └── summary.txt        # Insights & stats
├── tests/
│   └── test_analyzer.py   # Simple unit tests for calculations
├── README.md
└── requirements.txt

⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/covid19-data-visualization.git
cd covid19-data-visualization


Install dependencies:

pip install -r requirements.txt

🚀 Usage

Download the OWID dataset and save it to the data/ folder as owid-covid-data.csv.

Run the project:

python src/main.py


Edit main.py to change country, date range, or chart options.

📈 Example Plots
Total Cases (India)	Daily New Cases (World)

	
💡 Applications

Track pandemic trends for specific countries

Compare spikes and waves across regions

Use rolling averages to smooth noisy data

Export graphs for presentations or reports

🔮 Future Scope

Add interactive dashboards (Plotly/Streamlit)

Include vaccination & testing data

Automate daily updates via API