# -*- coding: utf-8 -*-
"""One-time-flight-arrivals.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a3GThFpb7BoZphBeaH0NvhzRrO-Ol_mN
"""

#Goal of the model is to predict weather a flight you are considering to book is liklely to arrive on time. 

#If we know 

#Purpose of this small project is to work on Jupyter Notebook: importing the data, view, prepare the data. 

#Using Pandas to clean and prepare data to be used for the machine-learning model. 
#Use scikit-learn to create machine learning model. 
#Use Matplotlib to visualize model's performance. 


#imports the data using Azure Blop tool. 
!curl https://topcs.blob.core.windows.net/public/FlightData.csv -o flightdata.csv

import pandas as pd
df = pd.read_csv('flightdata.csv')
df.head()

df.shape

df.isnull().values.any()
df.isnull().sum()
df = df.drop('Unnamed: 25', axis=1)

df.isnull().sum()

#Selecting the variables which play a major part in the delay of a flight, it will help us predictig the accuracy of our prediction. 

df = df[["MONTH", "DAY_OF_MONTH", "DAY_OF_WEEK", "ORIGIN", "DEST", "CRS_DEP_TIME", "ARR_DEL15"]]
df.isnull().sum()
df[df.isnull().values.any(axis=1)].head()

df = df.fillna({'ARR_DEL15':1})
df.iloc[177:185]

import math

for index, row in df.iterrows():
    df.loc[index, 'CRS_DEP_TIME'] = math.floor(row['CRS_DEP_TIME']/100)
df.head()

#creating dummy variables for ORIGIN and DEST

df = pd.get_dummies(df, columns=['ORIGIN', 'DEST'])
df.head()

"""##

# New Section
"""