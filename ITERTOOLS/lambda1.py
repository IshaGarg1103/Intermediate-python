#lambda arguments : expression

#lambda are considered anonymous functions, bcoz they don't require formal name like regular functions defined with def

#syntax:
#lambda arguments: expression
#1) expression : that is needed to be calculated, 
#2) arguments: that we pass just like in normal def function

add10 = lambda x: x +10
print(add10(5))

def add10_func(x):
    return x+10
mult = lambda x,y: x*y
print(mult(2,7))