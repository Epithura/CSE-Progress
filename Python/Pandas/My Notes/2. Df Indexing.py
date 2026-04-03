import pandas as pd

Summer=pd.read_csv("C:/Users/Aviral Singh/OneDrive/Desktop/CS/Python/Pandas/Appendix_Materials/summer.csv")
print(Summer.info()) #9 columns (indexing is done from 0 to 31164)

Summer1=pd.read_csv("C:/Users/Aviral Singh/OneDrive/Desktop/CS/Python/Pandas/Appendix_Materials/summer.csv", index_col="Athlete")
print(Summer1.info()) #8 columns (Athlete column is now the index column, indexing is done from HAJOS, Alfred to LIDBERG, Jimmy)

print(Summer1.iloc[0]) #zero based indexing is also applicable here #Series

"""print(Summer1.iloc[0].equals(Summer1.iloc["HAJOS, Alfred"]))""" #error, iloc only accepts integer indexing

print(Summer1.iloc[0].equals(Summer1.loc["HAJOS, Alfred"])) #False
print(Summer1.loc["HAJOS, Alfred"]) #Dataframe (HAJOS, Alfred occurs twice in Summer1)

print(Summer1.iloc[0].equals(Summer1.loc["HAJOS, Alfred"].iloc[0])) #Now True

print(Summer1.iloc[-1]) #returns the last row as a Series #-ve based indexing

L=[14,69,143]
print(Summer1.iloc[L]) #accessing multiple indexes using a list of indexes #Dataframe

print(Summer1.iloc[2:9:2]) #start,stop,step (2 inclusive, 9 exclusive)
print(Summer1.iloc[-5:-1]) #last five rows with last row exclusive
print(Summer1.iloc[-5:]) #last five rows

print(Summer1.iloc[0,4]) #[row index, column index]
print(Summer1.iloc[0,:4])
print(Summer1.iloc[0,[0,4,5,1]])
print(Summer1.iloc[L,[0,4,5,1]])

print(Summer1.iloc[:,4].equals(Summer.Country)) #False
print(Summer1.iloc[:,4].equals(Summer1.Country)) #True
print(Summer1.iloc[:,4].equals(Summer1["Country"])) #True

print(type(Summer1.loc["DRIVAS, Dimitrios"])) #<class 'pandas.core.series.Series'> #label based indexing
print(type(Summer1.loc["PHELPS, Michael"])) #<class 'pandas.core.frame.DataFrame'>

print(Summer1.loc[["PHELPS, Michael", "LEWIS, Carl"], ["Medal", "Year"]]) #[row label, column label]
print(Summer1.head(10).loc[:, ["Medal", "Year"]])

print(Summer1.loc[:"CHASAPIS, Spiridon"]) #start and stop both inclusive unlike iloc operator

"""print(Summer1.loc[:"PHELPS, Michael"])""" #error, multiple occurences of "PHELPS, Michael" and the system is unaware where to stop
#label based slicing is only allowed with unique labels unlike zero based slicing

print(Summer1.loc["BLAKE, Arthur":"DRIVAS, Dimitrios"]) #Empty DataFrame #"DRIVAS, Dimitrios" occurs before "BLAKE, Arthur"
print(Summer1.loc["DRIVAS, Dimitrios":"BLAKE, Arthur"]) #Now Okay

print(Summer1.loc["PHELPS, Michael", "Discipline":"City"]) #No columns appear coz "City" occurs before "Discipline"
print(Summer1.loc["PHELPS, Michael", "City":"Discipline"]) #Now Okay

#loc operator does not work with columns or labels that do not exist

#Boolean Indexing (Very Important)

print(Summer1["Medal"]=="Gold") #returns boolean Series
print(Summer1[Summer1["Medal"]=="Gold"]) #filters all Gold medals

print(Summer1[(Summer1["Medal"]=="Gold") & (Summer1["Year"]==2012)]) #multiple condition filtering
#Use & (not and) for multiple conditions
#Each condition must be inside parentheses

print(Summer1[(Summer1["Country"]=="IND") & (Summer1["Medal"]=="Gold")]) #Indian Gold medals

print(Summer1.loc[(Summer1["Year"]==2012) & (Summer1["City"]=="London"), ["Country","Medal"]]) #row filter + column selection together

#Difference between loc and iloc
#iloc -> integer position based
#loc  -> label based
#iloc slicing stop is exclusive
#loc slicing stop is inclusive

"""In which Wrestling Freestyle "Event" did the Spanish female Athlete "UNDA, Maider" win the Bronze Medal in London 2012?
(print the Event)"""

result=Summer1.loc["UNDA, Maider"] #this is a dataframe (multiple entries possible)

filters=result[(result["Medal"]=="Bronze") & (result["Year"]==2012) & (result["City"]=="London")]
print(filters["Event"]) #correct answer

#Explanation:
#and works only with single boolean values
#& works element-wise on pandas Series
