#namedtuple is a subclass of tuple with named fields.
#it is immutable, that means its value can't be changed
from collections import namedtuple

Point=namedtuple('Point','x,y')
#'Point' is the name of the new class like object
#['x'','y'] are the strings of the field names
#and it is assigned to variable named Point. Point refers to this newly created class-like type

p=Point(3,4)
print(p,p.x,p.y,p[0],p[1]) #Point(x=3, y=4) 3 4 3 4

#WHY ARE THE OBJECT AND STRING NAMED THE SAME?
#it is not necessary to name them the same, but just for convinience
Mypoint=namedtuple('Point',['x','y'])
#the type is named Point, but it is refering to Mypoint.
p=Mypoint(3,4)
print(p) #Point(x=3, y=4)

#TERMINOLOGY RECAP
#Class/type- the blueprint (Mypoint)
#Object- an instance of the class #p with arguments 3 and 4
