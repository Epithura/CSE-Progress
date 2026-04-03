from collections import deque #double-ended queue

People=["Anakin","Obi-Wan","Luke"] #list
Queue=deque(People) #list is now converted to a deque

Queue.append("Vader")
print(Queue)

Queue.popleft()
print(Queue)

Queue.appendleft("Yoda")
print(Queue)

Queue.rotate(-1)
print(Queue)

Queue.rotate(+2)
print(Queue)

Queue.extend(["Padme","Windu"])
print(Queue)

Queue.extendleft(["Analchin","Obi-Cum"])
print(Queue)

Queue.reverse()
print(Queue)

Final=list(Queue) #deque is now converted to a list
print(Final)