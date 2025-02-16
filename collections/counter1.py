#collections : Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

#EXAMPLE-1
a="aaaaaaaabbbbccc"
counter=Counter(a)
print(counter) #Counter({'a': 8, 'b': 4, 'c': 3})
print(counter.values()) #dict_values([8, 4, 3])

print(counter.most_common()) #[('a', 8), ('b', 4), ('c', 3)]
print(counter.most_common(1)) #[('a', 8)]
print(counter.most_common(2)) #[('a', 8), ('b', 4)]

print(counter.most_common(1)[0][0]) #a

#EXAMPLE-2
a="aaaaabbbbcccdde"
counter=Counter(a)
print(counter.items()) #dict_items([('a', 5), ('b', 4), ('c', 3), ('d', 2), ('e', 1)])
print(counter.keys()) #dict_keys(['a', 'b', 'c', 'd', 'e'])
print(counter.values()) #dict_values([5, 4, 3, 2, 1])

mylist=[0,1,0,1,2,1,1,3,2,3,2,4]
counter=Counter(mylist) 
print(counter) #Counter({1: 4, 2: 3, 0: 2, 3: 2, 4: 1})
print(list(counter.elements())) #[0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]