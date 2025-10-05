import numpy as np
import pandas as pd
import os

def clean(data:pd.DataFrame) ->pd.DataFrame:
        print(data.info())
        checking = data.isnull().sum()
        # print('Before \n',checking)
        
        if checking.sum() == 0:
            return data
        
        
        else:
            data = data.dropna()
            checking = data.isnull().sum()
            print("After : ",checking)
            
            
        # Convert columns to string
        data[['Province/State', 'Country/Region', 'Date', 'WHO Region']] = (
            data[['Province/State', 'Country/Region', 'Date', 'WHO Region']].astype(str)
        )

        # Convert Lat and Long to float
        data[['Lat', 'Long']] = data[['Lat', 'Long']].astype('float64')

        # Convert numerical columns to int
        data[['Confirmed', 'Deaths', 'Recovered', 'Active']] = (
            data[['Confirmed', 'Deaths', 'Recovered', 'Active']].astype('int64')
        )
        
        #country wise grouping of the data set..
        df_agg = data.groupby(["Country/Region", "Date"], as_index=False)[["Confirmed", "Deaths"]].sum()
        
        
        if  checking.sum() == 0:
                return data, df_agg