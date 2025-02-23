#lambda arguments: expression

from functools import reduce

# map(func, seq)

# map(): function in python that operates the function seperately on each element of an iterable object and returns iterator as a result
#map has two argument : function, argument
#lazy operator
a = [1,2,3,4,5]
b = map(lambda x: x*2,a)
print(list(b))

c = [x*2 for x in a]
print(c)#same as map function

#filter (func, seq)
#filter(): It returns an iterator containing only the elements for which the condition (provided as a function) evaluates to True
b = filter(lambda x: x%2==0, a)
print(list(b)) #[2,4]

c =[x for x in a if x%2==0]
print(c) #[2,4]

#reduce(func, seq)
#the reduce function is used to combine all the elements in an itearble into a single value
#it takes 3 arguments, 3rd optional
#1) function: that i want to perform on then
#2) argument: iterable object
#3) initializer : initialize the operation with this element

product_a = reduce(lambda x,y: x*y, a)
print(product_a) # 1*2*3*4*5=120



