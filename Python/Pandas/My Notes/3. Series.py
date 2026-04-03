import pandas as pd

Titanic=pd.read_csv("C:/Users/Aviral Singh/OneDrive/Desktop/CS/Python/Pandas/Appendix_Materials/titanic.csv")

AgeCol=Titanic["age"]
print(type(AgeCol)) #<class 'pandas.core.series.Series'>

"""
A Pandas Series is a one-dimensional labeled array-like object in the Pandas library for Python. 
It is a fundamental data structure in Pandas, similar to a column in a spreadsheet or a single column within a Pandas DataFrame.
"""

print(AgeCol.dtype) #float64
print(AgeCol.shape) #(891,) #(row,column)

"""AgeCol.info()""" #error #info is not a series attribute

AgeColDf=AgeCol.to_frame() #converts a series into a single column dataframe

print(AgeCol.describe()) #summary stats
print(AgeCol.size) #returns total number of all values #(missing or non-missing) #891
print(AgeCol.count()) #returns number of non-missing values

print(AgeCol.sum()) #returns sum of all numeric values 
print(sum(AgeCol)) #nan #sum function can't handle missing values
print(AgeCol.sum(skipna=False)) #nan #usually set to true by default

mean=AgeCol.mean()
median=AgeCol.median()
std=AgeCol.std() #Standard Deviation
minimum=AgeCol.min()
maximum=AgeCol.max()

unique=AgeCol.unique() #returns unique values in the series #removes duplicates of a particular value
print(len(unique)) #returns total number of unique values #counts missing values #89

print(AgeCol.nunique()) #excludes missing values #88
print(AgeCol.nunique(dropna=False)) #89

print(AgeCol.value_counts()) #returns count of all unqiue values in sorted order of freq #excludes nan
print(AgeCol.value_counts(sort=False,dropna=False)) #now sorted in order of first appearance
print(AgeCol.value_counts(ascending=True)) #returns count of all unqiue values in sorted order of freq from least frequent to most frequent
print(AgeCol.value_counts(normalize=True)) #returns relative frequencies
print(AgeCol.value_counts(normalize=True,dropna=False)) #now total is 891 instead of 714 because missing values are now considered

print(AgeCol.value_counts(bins=5,sort=False).sort_index()) #now data is distributed into 5 class intervals (equal size each)
print(AgeCol.value_counts(bins=[10*k for k in range(9)],sort=False).sort_index()) #now the shape and size of class intervals is manually specified with a list

#Index of a Series

print(AgeCol.index) #returns the index of the Series
print(AgeCol.index[0]) #returns first index label

#Accessing elements

print(AgeCol.iloc[0]) #position based access
print(AgeCol.loc[0]) #label based access (here labels are also integers)

print(AgeCol.iloc[0:5]) #slicing (stop exclusive)
print(AgeCol.loc[0:5]) #slicing (stop inclusive)

#Arithmetic operations (Vectorized Operations)

print(AgeCol+10) #adds 10 to each element
print(AgeCol*2) #multiplies each element by 2

print(AgeCol.mean()) #mean before transformation
print((AgeCol+10).mean()) #mean after transformation

#Comparison operations (Boolean Series)

print(AgeCol>30) #returns boolean Series
print(AgeCol[AgeCol>30]) #filters values greater than 30

print(AgeCol[(AgeCol>20) & (AgeCol<40)]) #multiple conditions

#Missing values handling

print(AgeCol.isnull()) #True where value is missing
print(AgeCol.isnull().sum()) #total missing values

print(AgeCol.dropna()) #removes missing values
print(AgeCol.fillna(AgeCol.mean())) #replaces missing values with mean

#Sorting

print(AgeCol.sort_values()) #sorts values ascending
print(AgeCol.sort_values(ascending=False)) #descending order

print(AgeCol.sort_index()) #sort by index labels

#Applying custom function

print(AgeCol.apply(lambda x: x*2)) #applies function element-wise

#Series alignment (Very Important Concept)

s1=pd.Series([1,2,3],index=["a","b","c"])
s2=pd.Series([10,20,30],index=["b","c","d"])

print(s1+s2) #alignment happens on index labels (not position) #NaN appears where labels don't match

#Creating a Series manually

s3=pd.Series([100,200,300])
print(s3)

s4=pd.Series([100,200,300],index=["x","y","z"])
print(s4)

s5=pd.Series({"a":1,"b":2,"c":3}) #dictionary based Series
print(s5)

Summer=pd.read_csv("C:/Users/Aviral Singh/OneDrive/Desktop/CS/Python/Pandas/Appendix_Materials/summer.csv")

Athlete=Summer["Athlete"]

print(Athlete.dtype) #object
print(Athlete.min()) #since Athlete is a series with dtype=object, the min attribute returns the lexicographically smallest element in the series

print(len(Athlete.unique())) #22762
print(Athlete.nunique()) #22762

print(Athlete.value_counts()) #Element-Frequency table #sorted by default in descending order of frequencies
print(Athlete.value_counts(ascending=True)) #now sorted in ascending order of frequencies
print(Athlete.value_counts(normalize=True)) #returns relative frequencies

print(Athlete.value_counts().idxmax()) #returns the row label of the maximum value
print(Athlete.value_counts().idxmin()) #returns the row label of the minimum value

#String operations (Vectorized String Methods)

print(Athlete.str.upper()) #converts all names to uppercase
print(Athlete.str.contains("MICHAEL")) #checks substring presence
print(Athlete.str.len()) #length of each string

#Key differences between Series and numpy array
#Series has index labels
#Series supports automatic alignment
#Series handles missing values (NaN)
#Operations are vectorized

#Datatype conversion

print(AgeCol.dtype) #float64
print(AgeCol.astype("int64",errors="ignore")) #attempts conversion (will ignore nan error)

print(Titanic["sex"].dtype) #object
print(Titanic["sex"].astype("category")) #converts object to categorical dtype (memory efficient)

print(Titanic["sex"].astype("category").cat.categories) #returns categories
print(Titanic["sex"].astype("category").cat.codes) #returns integer codes of categories

#map() method (Very Important for ML preprocessing)

print(Titanic["sex"].map({"male":1,"female":0})) #converts categorical values into numeric form
print(Titanic["sex"].map({"male":1,"female":0}).dtype) #int64

#replace() method (more flexible than map)

print(Titanic["sex"].replace({"male":1,"female":0}))

#between() method

print(AgeCol.between(20,30)) #boolean Series
print(AgeCol[AgeCol.between(20,30)]) #filters ages between 20 and 30 (inclusive)

#clip() method

print(AgeCol.clip(lower=0,upper=60)) #restricts values within range

#rank() method (useful in statistics and ML)

print(AgeCol.rank()) #assigns rank to each value
print(AgeCol.rank(method="average")) #default ranking method
print(AgeCol.rank(ascending=False)) #highest value gets rank 1

#where() and mask() (conditional replacement)

print(AgeCol.where(AgeCol>30)) #keeps values >30 else replaces with nan
print(AgeCol.mask(AgeCol>30)) #replaces values >30 with nan

print(AgeCol.where(AgeCol>30,other=0)) #replaces values <=30 with 0

#resetting index

print(AgeCol.reset_index()) #converts Series into dataframe with index column
print(AgeCol.reset_index(drop=True)) #drops old index

#Memory usage

print(AgeCol.memory_usage()) #memory consumed by Series (in bytes)
print(Titanic["sex"].astype("category").memory_usage()) #categorical consumes less memory

#Vectorized string cleaning (important in real datasets)

print(Athlete.str.strip()) #removes leading and trailing spaces
print(Athlete.str.lower()) #converts to lowercase
print(Athlete.str.replace(",","")) #removes commas
