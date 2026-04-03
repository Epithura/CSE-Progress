import pandas as pd
import numpy as np

Titanic=pd.read_csv("C:/Users/Aviral Singh/OneDrive/Desktop/CS/Python/Pandas/Appendix_Materials/titanic.csv")
Summer=pd.read_csv("C:/Users/Aviral Singh/OneDrive/Desktop/CS/Python/Pandas/Appendix_Materials/summer.csv")

#------------------------------------------------------------#
#Filtering with One Condition
#------------------------------------------------------------#

print(Titanic[Titanic["age"]>30]) #filters passengers with age greater than 30

print(Titanic["age"]>30) #returns boolean Series

#------------------------------------------------------------#
#Filtering with Multiple Conditions (AND)
#------------------------------------------------------------#

print(Titanic[(Titanic["age"]>30) & (Titanic["sex"]=="male")])
#use & for AND
#each condition must be inside parentheses

#------------------------------------------------------------#
#Filtering with Multiple Conditions (OR)
#------------------------------------------------------------#

print(Titanic[(Titanic["age"]<10) | (Titanic["age"]>60)])
#use | for OR

#------------------------------------------------------------#
#NOT operator
#------------------------------------------------------------#

print(Titanic[~(Titanic["sex"]=="male")]) #selects all females

#------------------------------------------------------------#
#isin() method
#------------------------------------------------------------#

print(Titanic[Titanic["pclass"].isin([1,2])]) #passengers in class 1 or 2

#------------------------------------------------------------#
#between() method
#------------------------------------------------------------#

print(Titanic[Titanic["age"].between(20,40)]) #age between 20 and 40 (inclusive)

#------------------------------------------------------------#
#Filtering with Missing Values
#------------------------------------------------------------#

print(Titanic[Titanic["age"].isnull()]) #rows where age is missing

print(Titanic[Titanic["age"].notnull()]) #rows where age is not missing

#------------------------------------------------------------#
#Filtering Strings
#------------------------------------------------------------#

print(Titanic[Titanic["sex"].str.contains("male")]) #string contains

#------------------------------------------------------------#
#query() method (cleaner syntax)
#------------------------------------------------------------#

print(Titanic.query("age > 30 and sex == 'male'"))

#------------------------------------------------------------#
#Sorting after Filtering
#------------------------------------------------------------#

print(Titanic[Titanic["age"]>30].sort_values("age",ascending=False))

#------------------------------------------------------------#
#Creating New Columns
#------------------------------------------------------------#

Titanic["AgePlus10"]=Titanic["age"]+10
print(Titanic.head())

Titanic["IsAdult"]=Titanic["age"]>=18 #boolean column
print(Titanic.head())

#------------------------------------------------------------#
#np.where() (Conditional Column Creation)
#------------------------------------------------------------#

Titanic["AgeGroup"]=np.where(Titanic["age"]<18,"Child","Adult")
print(Titanic[["age","AgeGroup"]].head())

#------------------------------------------------------------#
#apply() with lambda
#------------------------------------------------------------#

Titanic["FareCategory"]=Titanic["fare"].apply(lambda x:"High" if x>50 else "Low")
print(Titanic[["fare","FareCategory"]].head())

#------------------------------------------------------------#
#map() for categorical transformation
#------------------------------------------------------------#

Titanic["SexCode"]=Titanic["sex"].map({"male":1,"female":0})
print(Titanic[["sex","SexCode"]].head())

#------------------------------------------------------------#
#inplace parameter
#------------------------------------------------------------#

Titanic.sort_values("age",inplace=True) #modifies original dataframe
print(Titanic.head())

#------------------------------------------------------------#
#Filtering with Summer dataset
#------------------------------------------------------------#

print(Summer[Summer["Country"]=="IND"]) #Indian medals

print(Summer[(Summer["Year"]==2012) & (Summer["Country"]=="USA")])

print(Summer[Summer["Sport"].isin(["Swimming","Athletics"])])

print(Summer[Summer["City"].str.contains("London")])

#------------------------------------------------------------#
#Combining Filtering + Column Creation
#------------------------------------------------------------#

Summer["IsRecent"]=Summer["Year"]>=2000
print(Summer[["Year","IsRecent"]].head())
