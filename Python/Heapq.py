import heapq
HEAP=[]
heapq.heappush(HEAP,10) #[10]
heapq.heappush(HEAP,1)  #[1,10]
heapq.heappush(HEAP,5)  #[1,10,5]
heapq.heappush(HEAP,6)  #[1,6,5,10]
#heapq.heappush(HEAP,i) maintains the min-heap property.
print(HEAP)
Min=heapq.heappop(HEAP) #heapq.heappop() removes and returns the smallest element from the heap while maintaining the heap (min-heap) property.
List=[1,2,4,5,3,6,8,9,2,3,5,7,4]
heapq.heapify(List) #[1,2,4,2,3,4,8,9,5,3,5,7,6]
print(List) #heapq.heapify() converts a regular list into a min-heap in-place.
A=heapq.heappushpop(HEAP,8) #[6,8,10]
"""
heapq.heappushpop(heap, item) pushes item onto the heap and then pops and returns the smallest element, 
doing both operations more efficiently than calling them separately.
"""
#A=5
#Min=1
B=heapq.heapreplace(List,0) #B=1 #[0,2,4,2,3,4,8,9,5,3,5,7,6]
"""heapq.heapreplace(heap, item) pops and returns the smallest element, then pushes item into the heap — always replacing the top element."""
New_List=heapq.nsmallest(6,List) #heapq.nsmallest(n,iterable) returns a list of the n smallest elements from the iterable in sorted order.
print(New_List) #[0,2,2,3,3,4]
New_List1=heapq.nlargest(6,List) #heapq.nlargest(n,iterable) returns a list of the n largest elements from the iterable in descending order.
print(New_List1) #[9,8,7,6,5,5]
PL=[(1,"DSA"),(2,"CodeForces"),(3,"GTA"),(4,"Pandas"),(5,"Git")] #(Priority,Item) #Higher the priority, Lower it's value.
heapq.heapify(PL) #Now PL is a Priority Queue.
for i in range(len(PL)):
    print(heapq.heappop(PL))