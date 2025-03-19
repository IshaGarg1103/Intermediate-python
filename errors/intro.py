#Errors and Exceptions
a=5
print(a)) #syntax error

a = 5 + '10' #TypeError

b=c   #NameError : name 'c' is not defined

f=open('somefile.txt') #file not found error

a = [1,2,3]
a.remove(4) #Value Error
a[4] #indexerror

my_dict = {'name':'Max'}
my_dict['age'] #KeyError

x = -5
if x<0 :
    raise Exception('x should be positive')
#to get out of program

x=5
assert(x<=0),'x is positive' #Assertion Error 

try:
    a= 5 / 0
except Exception as e:
    print(e)

