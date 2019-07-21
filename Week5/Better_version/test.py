import pandas as pd
import os

def read_csv_to_mysql(filename):
    value = pd.read_csv(filename)
    return value


#os.chdir('/visualization/Week5/Better_version/')
df = read_csv_to_mysql('data/countriesData.csv')
df.drop(range(df.shape[0] - 5, df.shape[0]), inplace=True)
df = df.drop(columns=['CountryCode','SeriesCode'])
df.shape