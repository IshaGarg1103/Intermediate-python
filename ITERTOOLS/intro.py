#itertools : product, permutations, combinations, accumulate, groupby, and infinite iterators.
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b,repeat=1)
print(list(prod)) #[(1, 3), (1, 4), (2, 3), (2, 4)]
print("hello")