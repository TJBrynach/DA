import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv('investments_VC.csv', encoding= 'unicode_escape')

# For the purpose of analysis we can safely exclude the permalink and url from our dataframe as they arent likely to shed any useful analysis.  
df.drop(columns=['permalink','homepage_url'], inplace=True)

df.dropna(subset=['name', 'funding_rounds'], inplace=True)
#print(df.isna().sum().sort_values(ascending=False))

#some columns have some pesky whitespaces which may be frustrating later on.
df.columns = df.columns.str.strip()

