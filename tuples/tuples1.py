#tuples
i1,*i2,i3=1,2,3,4,5
print(i1)
print(i3)
print(i2)

import sys
my_list=[0,1,2,"hello",True]
my_tuple=(0,1,2,"hello",True)
print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(my_tuple),"bytes")
#the above prompt returns the no. of bytes

import timeit
print(timeit.timeit(stmt='[0,1,2,3,4]',number=1000000))
print(timeit.timeit(stmt='(0,1,2,3,4)',number=1000000))