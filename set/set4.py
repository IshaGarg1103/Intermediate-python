set1={1,2,3,4}

set2=set1
set2.add(5)
print(set1) #{1,2,3,4,5}
print(set2) #{1,2,3,4,5}

#craeting copies

#method-1
set2=set1.copy()
set1.add(6)
print(set1) #{1,2,3,4,5,6}
print(set2) #{1,2,3,4,5}

#method-2
set3=set(set1)
set3.add(7)
print(set1) #{1,2,3,4,5,6}
print(set3) #{1,2,3,4,5,6,7}
