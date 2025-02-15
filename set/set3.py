set1={1,2,3,4,5,6}
set2={1,2,3}

#SUBSET
print(set1.issubset(set2)) #False
print(set2.issubset(set1)) #True
print(set2.issubset(set2)) #True

print(set2.issuperset(set1)) #True
print(set1.issuperset(set2)) #False
print(set1.issuperset(set1)) #True

#DISJOINT

#checks whether they have no common elements, or not
#returns True if there is o common element
print(set1.isdisjoint(set2)) #False
set3={17,29}
print(set3.isdisjoint(set1))
