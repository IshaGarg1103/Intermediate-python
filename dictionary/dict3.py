mydict={"name":"Max","age":28,"email":"max@xyz.com"}
my_dict_2=dict(name="Marry",age=27,city="boston")

#all the attributes will be changed to the dictionary, and city attribute will be added to the list
mydict.update(my_dict_2)
print(mydict)

#
my_dict_3=dict(email="maxton@xyz.com")
mydict.update(my_dict_3)
print(mydict)