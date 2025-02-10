import copy
mydict={"name":"isha","age":20,"city":"new york"}
print(mydict)

#shallow copy
mydict_cpy=mydict #both of them are pointing to the same dictionary
mydict_cpy["email"]="max@yz.com"
print(mydict_cpy) #hence, changes made in dict 1 can be seen in 2nd dictionary
print(mydict) #both the dictionaries will change

mydict={"name":"isha","age":20,"city":"new york"}
mydict_cpy=dict(mydict)#making shallow copy
mydict_cpy["email"]="max@yz.com"
print(mydict_cpy) #here the changes in one dictionary doesnt make any in 2nd dictionary except lists
print(mydict)

mydict={"name":"isha","age":20,"city":"new york"}
mydict_cpy=mydict.copy() #making shallow copy method 2
mydict_cpy["email"]="max@yz.com"
print(mydict_cpy) 
print(mydict)

#deep copy
mydict={"name":"isha","age":20,"city":"new york","scores" : [10,20,30]}
mydict_cpy=copy.deepcopy(mydict) #making deepcopy
mydict_cpy["scores"][1]=10
print(mydict_cpy) 
print(mydict)