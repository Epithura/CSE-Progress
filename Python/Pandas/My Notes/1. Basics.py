import pandas as pd
import numpy as np 

Titanic = pd.read_csv("C:/Users/Aviral Singh/OneDrive/Desktop/CS/Python/Pandas/Appendix_Materials/titanic.csv")
Titanic #won't do anything
print(Titanic) #to print the dataframe

"""
pd.options.display.max_rows = 891
pd.options.display.min_rows = 20
print(Titanic)
"""

print(Titanic.head(7)) #will show first 7 rows of Titanic
print(Titanic.tail(12)) #will show last 12 rows of Titanic

Titanic.info() #gives column names, non-null count and datatype

print(Titanic.describe()) #summary of numeric columns
print(Titanic.describe(include="O")) #summary of non numeric data (object type)

print(type(Titanic)) #<class 'pandas.core.frame.DataFrame'>

len(Titanic) #891 (number of rows)

n=3
round(Titanic, n) #rounds off decimal to n places (only numeric columns)

min(Titanic) #minimum column label (NOT minimum values)

print(Titanic.shape) #returns (row,column)
Titanic.size #returns number of all elements in a dataframe (row*column)

print(Titanic.index) #Range of indices (start,stop,step)
Titanic.columns #returns all column labels

"""Titanic.min()""" #returns the minimum value for each column (by default, column-wise) #error because some columns have non-numeric data types

print(Titanic.min(numeric_only=True)) #minimum value of numeric columns
print(Titanic.max(numeric_only=True)) #maximum value of numeric columns
print(Titanic.mean(numeric_only=True)) #mean of numeric columns
print(Titanic.median(numeric_only=True)) #median of numeric columns

print(Titanic.mean(numeric_only=True).sort_values()) #chaining two methods
print(Titanic.mean(numeric_only=True).sort_values().head(2)) #chaining three methods

print(Titanic.sort_values(by="age",ascending=False)) #descending order
print(Titanic.sort_values(by=["pclass","age"])) #sorting by multiple columns (first pclass then age)

print(Titanic["age"]) #selecting a particular column
print(type(Titanic["age"])) #<class 'pandas.core.series.Series'>

print(type(Titanic[["age"]])) #<class 'pandas.core.frame.DataFrame'>

"""print(Titanic["age","sex"])""" #error (columns must be inside list)

print(Titanic[["age","sex"]]) #selecting two particular columns #the columns must be given in a list
print(type(Titanic[["age","sex"]])) #<class 'pandas.core.frame.DataFrame'>

print(Titanic.age.equals(Titanic["age"])) #True (both are same)
print(Titanic.age.equals(Titanic[["age"]])) #False (Two different datatypes)

Titanic.dtypes #returns datatype of each column
Titanic["age"].dtype #returns datatype of a particular column

Titanic.isnull() #returns boolean dataframe (True where value is missing)
Titanic.isnull().sum() #counts total missing values column-wise

Titanic["age"].min() #minimum value in age column
Titanic["age"].max() #maximum value in age column
Titanic["age"].mean() #mean of age column

Titanic["sex"].unique() #unique values in sex column
Titanic["sex"].nunique() #number of unique values

Titanic.value_counts #attribute reference (won't execute)
Titanic["sex"].value_counts() #frequency count of each category

Titanic.sample(5) #random 5 rows
Titanic.sample(frac=0.1) #random 10% of dataset

Titanic.sort_index() #sort dataframe by index
