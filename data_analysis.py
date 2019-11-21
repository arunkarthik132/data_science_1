import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import os

os.chdir('/users/arunkarthik/downloads')

pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns',1000)
pd.set_option('display.width',1000)

le= LabelEncoder()
ohe = OneHotEncoder()

data= pd.read_csv('airbnb.csv')

data['last_review'] = pd.to_datetime(data['last_review'])

print(data.select_dtypes(include=['object']).head())
print(data.select_dtypes(exclude=['object']).head())

data = data.drop(['last_review','reviews_per_month'],axis='columns')

print(data.info())
print(data.isnull().sum())

#==============#===============#+=================#======================#
'''MANHATTAN DATA'''
manhattan_data = data[data['neighbourhood_group']=='Manhattan']

price_per_day = manhattan_data[manhattan_data['minimum_nights'] == 1]


print(manhattan_data.shape)
#==============#===============#+=================#======================#

'''BROOKLYN DATA'''
Brooklyn_data = data[data['neighbourhood_group'] == 'Brooklyn']

print(Brooklyn_data.shape)
#==============#===============#+=================#======================#

'''QUEENS DATA'''
Queens_data = data[data['neighbourhood_group'] == 'Queens']

print(Queens_data.shape)

#==============#===============#+=================#======================#
'''STATEN ISLAND DATA'''
StatenIsland_data = data[data['neighbourhood_group']=='Staten Island']
print(StatenIsland_data.shape)


#==============#===============#+=================#======================#
'''BRONX DATA'''
Bronx_data = data[data['neighbourhood_group']=='Bronx']
print(Bronx_data.shape)
