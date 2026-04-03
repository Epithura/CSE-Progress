import pandas as pd

Summer=pd.read_csv("C:/Users/Aviral Singh/OneDrive/Desktop/CS/Python/Pandas/Appendix_Materials/summer.csv")

print(Summer.head())

#Basic Groupby

print(Summer.groupby("Country")) #returns a GroupBy object (does not compute anything)

print(Summer.groupby("Country").size()) #counts total rows per country (includes nan)

print(Summer.groupby("Country")["Medal"].count()) #counts non-missing medals per country

#size() vs count()
#size() counts total rows
#count() ignores missing values

#Aggregation

print(Summer.groupby("Country")["Year"].min()) #earliest medal year per country
print(Summer.groupby("Country")["Year"].max()) #latest medal year per country

print(Summer.groupby("Country")["Year"].agg(["min","max"])) #multiple aggregations

#Sorting grouped result

print(Summer.groupby("Country").size().sort_values(ascending=False)) #countries with highest medals first

#Groupby on multiple columns

print(Summer.groupby(["Country","Gender"]).size()) #multi-level index result

print(Summer.groupby(["Country","Gender"]).size().unstack()) #converts inner index to columns

#Using agg() with dictionary

print(Summer.groupby("Country").agg({"Year":["min","max"],"Medal":"count"}))

#Named aggregation (clean column names)

print(Summer.groupby("Country").agg(
    TotalMedals=("Medal","count"),
    FirstMedalYear=("Year","min"),
    LatestMedalYear=("Year","max")
))

#as_index parameter

print(Summer.groupby("Country",as_index=False)["Medal"].count()) #Country becomes normal column

#Filtering groups

country_medals=Summer.groupby("Country").size()

print(country_medals[country_medals>1000]) #countries with more than 1000 medals

#transform() (Very Important Concept)

print(Summer.groupby("Country")["Year"].transform("min")) #returns Series aligned with original dataframe

Summer["FirstMedalYear"]=Summer.groupby("Country")["Year"].transform("min")
print(Summer.head())

#Difference between agg and transform
#agg reduces dimension (grouped result)
#transform returns same length as original data

#Practical example

print(Summer.groupby("Sport")["Medal"].count().sort_values(ascending=False)) #which sport has most medals

print(Summer.groupby(["Year","Country"]).size()) #medals per country per year

#idxmax()

print(Summer.groupby("Country")["Year"].max().idxmax()) #country with most recent medal year
