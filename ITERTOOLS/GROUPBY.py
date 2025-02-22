from itertools import groupby

def smaller_than3(x):
    return x<4   #returns True for x<3

a = [1,2,3,4]
group_obj = groupby(a, key = smaller_than3)
for key, value in group_obj:
    print(key, list(value))

group_obj1=groupby(a, key=lambda x : x<3)
for key, value in group_obj1:
    print(key, list(value))