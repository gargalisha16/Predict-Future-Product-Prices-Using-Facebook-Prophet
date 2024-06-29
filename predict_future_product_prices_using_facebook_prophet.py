# -*- coding: utf-8 -*-
"""Predict-Future-Product-Prices-Using-Facebook-Prophet.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ytdrcrscfY0aknu2SXoJrCqMgfTULiHf
"""

#project: predicting future prices of avocados using facebook prophet
#prophet is a open source tool for time series forecasting

#importing libraries
import pandas as pd#import pandas for data manipulation using dataframes
import matplotlib.pyplot as plt#import matplotlib for data visualisation
from prophet import Prophet#import facebook prophet library

#dataframe creation for both training and testing datasets
avocado_df= pd.read_csv('avocado.csv')

#viewing the head of the training dataset
#the df.head() function in pandas is used to display the first few rows of a dataframe
#by default, df.head() shows the first 5 rows, but you can specify a different number of rows to display by
#passing an integer as an argument, like df.head(10) to show the first 10 rows
avocado_df.head()

#viewing the last elements in the training dataset
avocado_df.tail(10)

#viewing dataset description
#the df.describe() function in pandas generates descriptive statistics that summarize
#the central tendency, dispersion, and shape of a dataset’s distribution, excluding NaN values
#this function is particularly useful for getting a quick overview of numeric data in a dataframe
avocado_df.describe()

#viewing dataset summary or information
#the df.info() function in pandas provides a concise summary of a dataframe
#this summary includes the following details:
#number of rows and columns
#column names
#data type of each column
#number of non-null (non-missing) values in each column
#memory usage of the DataFrame
#this function is useful for getting a quick overview of the structure and composition of a dataframe,
#which can help identify potential issues with data types or missing values
avocado_df.info()

#viewing missing values in dataset
#the avocado_df.isnull().sum() function in pandas is used to check for missing values in a dataframe
#here's what it does:
#1. avocado_df.isnull(): this part of the function creates a dataframe of the same shape as avocado_df,
#where each element is a Boolean value (True or False)
#a True value indicates that the corresponding element in the original DataFrame is NaN (missing),
#and False indicates that the element is not missing
#2. .sum(): this part of the function sums the True values (considered as 1) for each column,
#resulting in a Series where each element represents the number of missing values in that column
avocado_df.isnull().sum()

#sorting dataset
#the df.sort_values() function in pandas is used to sort a dataframe by one or more columns
avocado_df.sort_values('AveragePrice')

#plotting date and average price
plt.plot(avocado_df["Date"], avocado_df["AveragePrice"])

#select date and price
avocado_df_partial= avocado_df[['Date', 'AveragePrice']]#choosing particular columns from the dataset
avocado_df_partial

#renaming the features
avocado_df_partial= avocado_df_partial.rename(columns={'Date': 'ds', 'AveragePrice': 'y'})
avocado_df_partial

#creating prophet object(model)
obj= Prophet()
#training of fit the model
obj.fit(avocado_df_partial)

#forcasting future
#creating a new dataframe future that extends the "ds" (datetime) column from the original dataset to include future dates
future= obj.make_future_dataframe(periods=365)
#using the fitted prophet model to make predictions(forecast) for the dates specified in the future dataframe
forecast= obj.predict(future)
forecast

#plotting the forecasted results generated by a model
obj.plot(forecast, xlabel='Date', ylabel="Price")
obj.plot_components(forecast)

#selecting specific region
avocado_df_sample=avocado_df[avocado_df['region']=='West']
avocado_df_sample

#select date and price
avocado_df_sample= avocado_df_sample[['Date', 'AveragePrice']]#choosing particular columns from the dataset
avocado_df_sample

#renaming the features
avocado_df_sample= avocado_df_sample.rename(columns={'Date': 'ds', 'AveragePrice': 'y'})
avocado_df_sample

#creating prophet object(model)
obj_sample= Prophet()
#training of fit the model
obj_sample.fit(avocado_df_sample)

#forcasting future
#creating a new dataframe future that extends the "ds" (datetime) column from the original dataset to include future dates
future_sample= obj_sample.make_future_dataframe(periods=365)
#using the fitted prophet model to make predictions(forecast) for the dates specified in the future dataframe
forecast_sample= obj_sample.predict(future_sample)
forecast_sample

#plotting the forecasted results generated by a model
obj_sample.plot(forecast_sample, xlabel='Date', ylabel="Price")
obj_sample.plot_components(forecast)