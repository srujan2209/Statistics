import pandas as pd
import numpy as np
import pickle
import os

path = os.path.dirname(os.path.realpath(__file__))
# LoadingDatasets
file_name = path+'/LoadingDatasets/load.csv'
with open(file_name) as f:
    data_csv = pd.read_csv(f)
    print(data_csv.head())

with open(path+'/LoadingDatasets/load_pickle.pickle',"rb") as fd:
    data_picke = pickle.load(fd)
    print(data_picke.head())

#PreparingDatasets
df = pd.read_csv(path+'/PreparingDatasets/Diabetes.csv')
print(df)
print(df.info())
print(df.head())
df = df.fillna(0)
print(df.info())
df2 = df[["Glucose","BMI","Age","Outcome"]]
df2 =df2.head()
print(df2)
print(df2.describe())
print(df2[df2.columns[:-1]] == 0)
