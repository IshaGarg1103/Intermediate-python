from collections import namedtuple
Mypoint=namedtuple('Point',['x','y'])
p=Mypoint(3,4)
#KEY FEATURES OF namedtuple

#immutable
#p.x=20 #AttributeError: can't set attribute

print(p._asdict()) #{'x': 3, 'y': 4}

#default values when not assigned:
Point=namedtuple('Point',['x','y'],defaults=[0,0])
p=Point()
print(p) #Point(x=0, y=0)

#Find field names:
print(Point._fields)

#Replace Values:
p=Point(10,20)
p_new=p._replace(x=30)
print(p_new) #Point(x=30, y=20)

#returning multiple values from functions:
def cool():
    return namedtuple('UserInfo',['Name','email'])('Isha','isha@xyz.com')
user1=cool()
print(user1.Name)

