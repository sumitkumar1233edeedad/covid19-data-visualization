import pandas as pd
import numpy as np
import os 

def analyze(df:pd.DataFrame, cu: pd.DataFrame) -> pd.DataFrame:
    
    global_daily = df.groupby('Date', as_index=False)['Confirmed'].sum().sort_values('Date')
    global_daily['CumulativeConfirmed'] = global_daily['Confirmed'].cumsum()
    global_new_cases = global_daily.copy()
    global_new_cases['NewCases'] = global_new_cases['Confirmed'].diff().fillna(global_daily['CumulativeConfirmed'])
    
    country_daily = cu.copy()
    country_daily['CumulativeConfirmed'] = country_daily.groupby('Country/Region')['Confirmed'].cumsum()
    country_daily['NewCases'] = country_daily.groupby('Country/Region')['Confirmed'].diff().fillna(country_daily['CumulativeConfirmed'])
    
    
    window = 3
    global_new_cases['SmoothedNewCases'] = global_new_cases['NewCases'].rolling(window=window, min_periods=1).mean()
    country_daily['SmoothedNewCases'] = country_daily.groupby('Country/Region')['NewCases'].transform(lambda x: x.rolling(window=window, center=True).mean())
    print("Global Daily New Cases with Smoothed Values:", global_new_cases)
    print("Country Daily New Cases with Smoothed Values:", country_daily)