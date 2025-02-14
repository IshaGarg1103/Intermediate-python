myset=set()

#ADDITION OF ELEMENTS
#!) only one element
myset.add(1)
myset.add(2)
myset.add((3,5)) #{1,2,(3,5)}
#2) only add multiple elements
myset.update([5,6])
print(myset) #{1,2,5,6,(3,5)}

#REMOVAL OF ELEMENTS
myset={1,2,3,4,5,6}
myset.remove(3)
print(myset) #{1, 2, 4, 5, 6}

myset.discard(2)
print(myset) #{1, 4, 5, 6}

myset.pop() #{4, 5, 6}
print(myset)

myset.clear()
print(myset) #set()

#NO INDEXING 
#print(myset[0])  #error : 'set' is not subscriptable
#subscriptable : can't slice because set is a hash table

#ques: WHY CAN'T WE SLICE THRU SET
#>>>   each piece is placed in a location based on its hash value
#>>>   there is no "first" and "second" position

#MEMBERSHIP
myset={1,2,3}
print(2 in myset) #true
print(4 in myset) #False

#UNION
set1={1,2,3}
set2={3,4,5}
print(set1 | set2) #{1,2,3,4,5}

set=set1.union(set2)
print(set)   #{1,2,3,4,5}
print(set1)  #{1,2,3}
print(set2)  #{3,4,5}

#INTERSECTION
set1={1,2,3}
set2={3,4,5}
print(set1 & set2)

set=set1.intersection(set2)
print(set)
print(set1)  #{1,2,3}
print(set2)  #{3,4,5}

#SYMMETRIC DIFFERENCE 
set1={1,2,3}
set2={3,4,5}
print(set1^set2) #{1,2,4,5}

#FROZEN SETS- is an immutable version of a set, once created its elements can't be changed
myset=frozenset((1,2,3))
print(myset) #frozenset({1, 2, 3})

#frozen sets are immutable
#myset.add(4) #Error: AttributeError (frozen sets are immutable)

#immutable (integers, strings, tuples)
#mutable : lists, dictionaries, sets are not hashable because they are mutable
