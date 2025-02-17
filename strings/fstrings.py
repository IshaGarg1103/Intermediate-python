#F-STRINGS

#can perform arithmatics 
x=20
y=10
print(f"the sum of {x} and {y} is {x+y}")

#calling functions
def call(name):
    return f"Hello {name}!"
str= f"{call('Isha')}"
print(str)

#format numbers to control decimal places
pi=3.14159
mystr = f"The value of pi is approximately {pi:.2f}."
print(mystr)

#using dictionaries
person={'name':'Alice','age':20}
str=f"My name is {person['name']} and i am {person['age']} years old."
print(str)
