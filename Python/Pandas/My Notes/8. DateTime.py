import pandas as pd
import numpy as np

#------------------------------------------------------------#
#Creating Dataset with Date Information
#------------------------------------------------------------#

data=pd.DataFrame({
    "Date":["2020-01-01","2020-01-05","2020-02-10","2021-03-15","2021-06-20"],
    "Sales":[100,150,200,130,170]
})

print(data)

#------------------------------------------------------------#
#Converting to DateTime
#------------------------------------------------------------#

data["Date"]=pd.to_datetime(data["Date"]) #converts string to datetime
print(data.dtypes)

#------------------------------------------------------------#
#Setting Date as Index
#------------------------------------------------------------#

data.set_index("Date",inplace=True)
print(data)

#------------------------------------------------------------#
#dt Accessor (Extracting Components)
#------------------------------------------------------------#

data["Year"]=data.index.year
data["Month"]=data.index.month
data["Day"]=data.index.day
data["Weekday"]=data.index.day_name()

print(data)

#------------------------------------------------------------#
#Filtering with Dates
#------------------------------------------------------------#

print(data["2020"]) #all data from year 2020

print(data.loc["2020-01-01":"2020-12-31"]) #date slicing (inclusive)

#------------------------------------------------------------#
#Sorting by Date
#------------------------------------------------------------#

print(data.sort_index())

#------------------------------------------------------------#
#Resampling (Time-based Aggregation)
#------------------------------------------------------------#

print(data["Sales"].resample("Y").sum()) #yearly total sales

print(data["Sales"].resample("M").sum()) #monthly aggregation

#Common frequency codes:
#D -> daily
#M -> month end
#Y -> year end
#W -> weekly

#------------------------------------------------------------#
#Rolling Window (Moving Average)
#------------------------------------------------------------#

print(data["Sales"].rolling(window=2).mean()) #2-period moving average

#------------------------------------------------------------#
#Shift (Lag Feature)
#------------------------------------------------------------#

data["PreviousSales"]=data["Sales"].shift(1) #shifts values down by 1
print(data)

#------------------------------------------------------------#
#Date Difference
#------------------------------------------------------------#

data["DaysDiff"]=data.index.to_series().diff().dt.days
print(data)

#------------------------------------------------------------#
#Generating Date Range
#------------------------------------------------------------#

dates=pd.date_range(start="2022-01-01",periods=5,freq="D")
print(dates)

#------------------------------------------------------------#
#Creating Time Series Directly
#------------------------------------------------------------#

ts=pd.Series([10,20,30,40,50],index=dates)
print(ts)
