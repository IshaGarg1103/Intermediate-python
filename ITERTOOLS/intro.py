from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby

import operator #for operations other than multiplication
#itertools : product, permutations, combinations, accumulate, groupby, and infinite iterators.

#product : cartesian product
a = [1,2]
b = [3]
prod = product(a,b,repeat=1)
print(list(prod)) #[(1, 3), (1, 4), (2, 3), (2, 4)]
 
prod=product(a,b, repeat=2)
print(list(prod))  #[(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

#permutations: making 2 students sit on their seats, position matters
a=[1,2,3]
b=[3]
perm = permutations(a,2)
print(list(perm))
#permutations(a,2) : 2=set of 2 to permutate.

#combinations : picking 2 people for a team, hence position doesn't matter
comb = combinations(a,2)
print(list(comb)) #[(1, 2), (1, 3), (2, 3)]

#combinations with repetitions : repetion is allowed, but position of the elements doesn't matter
comb = combinations_with_replacement(a,2)
print(list(comb)) #[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

#ACCUMULATE : default setting is addition 
a=[1,2,3,4]
acc = accumulate(a)
print(a) #[1,2,3,4]
print(list(acc)) #[1, 3, 6, 10]
#3 -> 2+1
#6 -> 3+2+1

#for operation other than addition
acc = accumulate(a,func=operator.mul)
print(list(acc))  #[1,2,6,24]

a=[1,2,5,1]
acc= accumulate(a,func=max)
print(list(acc)) #[1, 2, 5, 5]
