#set : no duplicates, mutable, unordered
myset={1,2,3,1,2}
print(myset) #{1,2,3}

myset=set((1,2,3))#one argument allowed, hence use iterable
print(myset) 
#what is an iterable : object that cn be looped over such as list, tuple, set

myset={1,"hello",3.14}
print(myset)  #{1, 3.14, 'hello'}

myset={1,3.14,5.0,2}
print(myset) #{1, 2, 3.14, 5.0}

myset=set("hello")
print(myset) #{'h','e','o','l'}

#DECLARING TYPES

#can't declare like this
myset={}
print(type(myset)) #<class 'dict'>

#declare like this
myset=set()
print(type(myset)) #<class 'set'>