
mydict={"name":"isha","age":20,"city":"new york"}
print(mydict)

mydict_cpy=mydict #both of them are pointing to the same dictionary
mydict_cpy["email"]="max@yz.com"
print(mydict_cpy) #hence, changes made in dict 1 can be seen in 2nd dictionary
print(mydict) #both the dictionaries will change

mydict={"name":"isha","age":20,"city":"new york"}
mydict_cpy=dict(mydict)
mydict_cpy["email"]="max@yz.com"
print(mydict_cpy)
print(mydict)