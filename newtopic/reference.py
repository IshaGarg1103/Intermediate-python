#REFERENCE
#python doesn't give you direct access to the memory address of the object
# ***VARIABLES IN PYTHON ACT AS REFERENCES TO OBJECTS IN MEMORY***

list1=[1,2,3]
list2 = list1 #Both list1 and list2 refernce to the smae object [1,2,3]
#both list1 and list2 are pointing to the same memory location where [1,2,3] is stored

#HOW PYTHON HANDLES REFERENCES INTERNALLY
#1)under the hood, python uses the concept of 'reference counting' to manage memory
#2)Each object in Python has a count of how many refernces point to it. when the refernce count
#  drops to zero, python frees the memory

x=[1,2,3]
y=x #two refernces to the same object

del x #deletes the reference x, but the object still exists, because y variable exists
del y #deletes the last refernce, now the object is removed from memory

