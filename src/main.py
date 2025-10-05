import pandas as pd
import os
from data_loader import load
from cleaner import clean
from analyzer import analyze


def main():
    data = load()
    print('load data successful🔃')
    
    data_cleaned, country_wise_count = clean(data)
    
    data_path = "c:/Users/sumit/OneDrive/Desktop/project work\covid19-data-visualization/outputs/data"
    if not os.path.exists(data_path):
        os.mkdir(data_path)
    file_path = os.path.join(data_path, 'clean_data.csv')
    data_cleaned.to_csv(file_path)
    file_path1 = os.path.join(data_path, 'country_wise.csv')
    country_wise_count.to_csv(file_path1)
    
    print('Cleaned covid19 data set🧹')
    
    
    ans = analyze(data_cleaned, country_wise_count)
    
    
    
if __name__ == '__main__':
    main()