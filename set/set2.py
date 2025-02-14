set1={1,2,3,4,5,6,7,8,9}
set2={1,2,3,10,11,12}

print(set1.difference(set2)) #{4,5,6,7,8,9}

print(set1.symmetric_difference(set2)) #{4, 5, 6, 7, 8, 9, 10, 11, 12}
print(set2.symmetric_difference(set1)) #{4, 5, 6, 7, 8, 9, 10, 11, 12}

print(set1)
print(set2)

print(set1.intersection_update(set2)) #None
#the intersection_update() does not return anything, hence None
print(set1) #{1,2,3}

#DIFFERENCE
set1={1,2,3,4,5,6,7,8,9}
set2={1,2,3,10,11,12}
set1.difference_update(set2)
print(set1) #{4,5,6,7,8,9}

#SYMMETRIC DIFFERENCE 
set1={1,2,3,4,5,6,7,8,9}
set2={1,2,3,10,11,12}
print(set1.symmetric_difference(set2))
#set1={1,2,3,4,5,6,7,8,9}
#set2={1,2,3,10,11,12}

#SYMMETRIC DIFFERENCE UPDATE
set1.symmetric_difference_update(set2)
print(set1)  #{4, 5, 6, 7, 8, 9, 10, 11, 12}
