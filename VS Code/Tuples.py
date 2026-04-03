#lists are mutable but tuples are immutable
list=[1,2,3,4]
tup=(1,2,3,4)
tup1=(1,2,3,4,) #tup1 and tup are same
list[2]=5 #valid
print(list)
#tup[2]=5 is invalid coz tup is immutable
t=(1)
print(type(t)) #returns integer
t1=(1,) #single value tuple
print(type(t1)) #returns tuple
t2=("a")
print(type(t2)) #returns string  
t3=() #empty tuple (it is a tuple)
print(tup[1:3]) #slicing
T=(1,2,3,1,2,4,5,3,1,3,3,5,6,7,8,9,0,0,0,7,7,5,4,3,)
L=[1,2,3,1,2,4,5,3,1,3,3,5,6,7,8,9,0,0,0,7,7,5,4,3,]
print(T.count(1))
print(T.index(1)) #returns index of very first occurence of the element 
print(L.count(1))
print(L.index(1)) #returns index of very first occurence of the element
# count and index methods work with both Tuples and Lists