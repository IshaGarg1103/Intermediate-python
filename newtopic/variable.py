#POINTER
list1=[1,2,3]

list2=list1 #when you assign one variable to another
#new copy isn't created, unless you explicitly ask for it
#both variables point to the same object in memory

#list1 --> memory(0x1000)
#list2 --> memory(0x1000)

#COPY
list3=list1.copy()

#list1 --> memory(0x1000)
#list3 --> memory(0x2000)

#VARIABLE
#list1, list2, list3

#POINTER (memory address)
#0X1000, 0X2000

#OBJECT IN MEMORY
#[1,2,3] 