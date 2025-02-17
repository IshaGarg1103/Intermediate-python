#dictionary : key -value pairs, unordered, mutable
mydict={"name":"max","age":28,"city":"new york"}
print(mydict)

mydict2=dict(name="marry",age=27,city="boston")
print(mydict2)
value=mydict["age"]
print(value)

#value=mydict["lastname"]
#print(mydict) #keyerror : 'lastname'

#appending an element
mydict["email"]="max@xyz.com"
print(mydict)

try:
    print(mydict['lastname'])
except:
    print("Error") #will produce an error, since no key named lastname is present in mydict

#acquiring keys in dictionary
for value in mydict:
    print(value,end=' ') #will give keys in the output
    #ouput:name age city email

#for acquiring both at the same time
for key,value in mydict.items():
    print(key,value)
