D={"Key":"Value"} #Standard form of a dictionary
#In each dictionary, any key can be of any datatype from these : (tuple,int,float,str,bool,NoneType); all these data types are hashable.
#Any data type can be a dictionary value in Python.
#Duplicate keys are not allowed in Python Dictionaries.
#Dictionaries are unordered unlike Lists and Tuples.
#Dictionaries are mutable.
print(D["Key"]) #We can obtain Dictionary values through their keys.
D["Key"]="NewValue" #We can update value corresponding to a key.
print(D["Key"])
D["Key1"]="Value1" #Adding new key-value pair to the Dictionary.
print(D)
null_dict={} #A Null Dictionary.
Scores={"Phy":98,"Chem":97,"Maths":100}
Student={"Name":"Avi","Subjects":Scores} #Nested Dictionary
print(Student["Subjects"]["Maths"])
"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""
print(Student.values())
print(Student["Subjects"].values())
print(Student["Name"]) #returns Avi
print(Student.get("Name")) #returns Avi 
#print(Student["Name2"]) #returns an error
print(Student.get("Name2")) #returns None
print(Student.items())
Student.update({"Name":"Aviral", #Overwrites Avi
                "Age":18,
                "City":"New Delhi"
                })
print(Student) #Name Avi is replaced by Aviral
