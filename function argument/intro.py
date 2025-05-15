#positional arguments

#the order in which you provide the arguments when you call the function directly
#correspnds to the order of the parameters.

def des(color,sides):
    print(f"This shape is {color} and has {sides} sides.")

des("blue",4)
des(6,"red")

#their meaning is determined by their position in the function call

def calc(length, width):
    area = length*width
    print(f"The area is :{area}")

calc(5,10) #'the area is : 50' -both arguments provided
#calc(5) #TypeError
#calc()  #TypeError

#order matters
#number of arguments is fixed
