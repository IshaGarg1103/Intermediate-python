#format
name='Isha'
age=20
print("My name is {} and my age is {}".format(name,age))#My name is Isha and my age is 20

print("my name is {1} and my age is {0}".format(age,name))#My name is Isha and my age is 20

print("my name is {Name} and i am {Age} years old".format(Name="Isha",Age=19))

#padding
print("Name : {:<10} Age : {:>5}".format(name,age)) #Name : Isha       Age :    20
print("Name : {:^10} Age : {:^5}".format(name,age)) #Name :    Isha    Age :  20