#immutable objects are hashable : tuple, strings, integer, float
x = 42
print(hash(x))

s=(1,2,3)
print(hash(s))