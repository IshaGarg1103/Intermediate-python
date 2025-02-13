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
print(myset) #{}