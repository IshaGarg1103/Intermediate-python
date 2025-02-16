#collections : Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

a="aaaaaaaabbbbccc"
counter=Counter(a)
print(dict(counter)) #Counter({'a': 8, 'b': 4, 'c': 3})
print(counter.values()) #dict_values([8, 4, 3])

print(counter.most_common()) #[('a', 8), ('b', 4), ('c', 3)]
print(counter.most_common(1)) #[('a', 8)]
print(counter.most_common(2)) #[('a', 8), ('b', 4)]

print(counter.most_common(1)[0][0]) #a

print(counter.elements())
