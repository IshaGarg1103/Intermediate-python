mydict={"name":"Max","age":28,"email":"max@xyz.com"}
my_dict_2=dict(name="Marry",age=27,city="boston")

#all the attributes will be changed to the dictionary, and city attribute will be added to the list
mydict.update(my_dict_2)
print(mydict)

#new attribute can be added directly to the dictionary this way
my_dict_3=dict(major="compsci")
mydict.update(my_dict_3)
print(mydict)

my_dict={3:9,6:36,9:81}
print(my_dict)

#value=my_dict[0]
#print(value) #Keyerror:0 
#use key directly to obtain the value, instead of index no.

mytuple=[8,7]
#mydict={mytuple:15}
#print(mydict) #Type Error : unhashable type : 'list' 
#In Python, dictionary keys must be hashable and immutable, meaning they must 
# have a fixed value that doesn’t change over time

mytuple=(8,7)
mydict={mytuple : 15}
print(mydict)