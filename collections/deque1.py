from collections import deque

#deque: "double ended queue" is a versatile and efficient data structure
# provided by the collections module in Python.

#creating an empty deque
d=deque()
print(d) #deque([])
#creating a deque from an iterable
d=deque([1,2,3])
print(d) #deque([1,2,3])

#KEY FEATURES OF DEQUE:
d.append(4)
print(d) #deque([1, 2, 3, 4])

d.appendleft(0)
print(d) #deque([0, 1, 2, 3, 4])

d.pop()
print(d) #deque([0, 1, 2, 3])

d.popleft() 
print(d) #deque([1, 2, 3])

d.extend([4,5])
print(d) #deque([1, 2, 3, 4, 5])

d.extendleft([-1,0])
print(d) #deque([0, -1, 1, 2, 3, 4, 5])

#deque doesnot support slicing method like lists
#indexing can only be done thru iteration and is an o(n) operation.

#ROTATION IN DEQUE
d=deque([1,2,3,4,5])

#rotate to the right by 2 steps
d.rotate(2)
print(d) #deque([4, 5, 1, 2, 3])
#first 5 moves to the left and then '4' element

d.rotate(-1)
print(d) #deque([5,1,2,3,4])

#limiting the size of deque
d=deque([1,2,3],maxlen=2)
d.append(4)
print(d)  #deque([3, 4], maxlen=2)