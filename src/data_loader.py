import pandas as pd
import os

def load():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data')
    df = pd.read_csv(os.path.join(data_path, 'covid_19_clean_complete.csv'))
    # print(df.head())
    
    return df