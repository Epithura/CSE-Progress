import pandas as pd

#------------------------------------------------------------#
#Creating Clean Artificial Datasets
#------------------------------------------------------------#

medals=pd.DataFrame({
    "Country":["USA","USA","IND","FRA","GER","IND"],
    "Year":[2012,2016,2012,2016,2012,2016],
    "Medal":["Gold","Silver","Bronze","Gold","Silver","Gold"]
})

countries=pd.DataFrame({
    "Country":["USA","IND","FRA","GER","JPN"],
    "Continent":["North America","Asia","Europe","Europe","Asia"],
    "Population_millions":[331,1391,67,83,125]
})

hosts=pd.DataFrame({
    "Year":[2012,2016,2020],
    "HostCity":["London","Rio","Tokyo"]
})

print(medals)
print(countries)
print(hosts)

#------------------------------------------------------------#
#Concat (Combining DataFrames)
#------------------------------------------------------------#

df1=pd.DataFrame({"A":[1,2],"B":[3,4]})
df2=pd.DataFrame({"A":[5,6],"B":[7,8]})

print(pd.concat([df1,df2])) #row-wise concat (axis=0 default)

print(pd.concat([df1,df2],ignore_index=True)) #resets index

print(pd.concat([df1,df2],axis=1)) #column-wise concat

#------------------------------------------------------------#
#Merge (Relational Join)
#------------------------------------------------------------#

print(pd.merge(medals,countries,on="Country")) #inner join (default)

#Only matching Country values will appear

#------------------------------------------------------------#
#Different Types of Joins
#------------------------------------------------------------#

print(pd.merge(medals,countries,on="Country",how="left"))
#keeps all rows from medals

print(pd.merge(medals,countries,on="Country",how="right"))
#keeps all rows from countries

print(pd.merge(medals,countries,on="Country",how="outer"))
#keeps everything from both

#------------------------------------------------------------#
#Merge on Different Column Names
#------------------------------------------------------------#

countries2=countries.rename(columns={"Country":"Nation"})

print(pd.merge(medals,countries2,left_on="Country",right_on="Nation"))

#------------------------------------------------------------#
#Merge on Multiple Columns
#------------------------------------------------------------#

print(pd.merge(medals,hosts,on="Year"))
#adds HostCity to medals

#------------------------------------------------------------#
#Suffixes (Handling Overlapping Columns)
#------------------------------------------------------------#

df3=pd.DataFrame({
    "Country":["USA","IND"],
    "Year":[2012,2016]
})

print(pd.merge(medals,df3,on="Country",suffixes=("_medals","_df3")))

#------------------------------------------------------------#
#Merge on Index
#------------------------------------------------------------#

countries_indexed=countries.set_index("Country")

print(pd.merge(medals,countries_indexed,left_on="Country",right_index=True))

#------------------------------------------------------------#
#Indicator Parameter
#------------------------------------------------------------#

print(pd.merge(medals,countries,on="Country",how="outer",indicator=True))
#_merge column shows:
#left_only
#right_only
#both

#------------------------------------------------------------#
#Validate Parameter (Interview Important)
#------------------------------------------------------------#

print(pd.merge(medals,countries,on="Country",validate="many_to_one"))
#many medals per country but only one country entry

#Possible validations:
#one_to_one
#one_to_many
#many_to_one
#many_to_many
