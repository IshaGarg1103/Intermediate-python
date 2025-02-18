from itertools import count, cycle, repeat, product
#itertools : product, permutations, combinations, accumulate, groupby, and infinite iterators.

a = [1,2]
b = [3,4]
prod = product(a,b,repeat=1)
print(list(prod)) #[(1, 3), (1, 4), (2, 3), (2, 4)]



# Infinite counter
for i in count(10, 2):
    print(i, end =" ")
    if i > 20:
        break
print("\n")
# Cycling through elements
cycler = cycle("ABC")
for _ in range(5):
    print(next(cycler))

# Repeating an element
repeater = repeat("Hello", 3)
print(list(repeater))