#SHALLOW COPY
dict1={"name":"isha","age":20,"scores":[20,30,40]}
dict1_cpy=dict(dict1)
dict1_cpy["major"]="compsci"
print(dict1_cpy)
dict1["scores"][1]=50
print(dict1)
print(dict1_cpy)

#If you change something inside the nested list in the shallow copy, 
# it will also change in the original dictionary because both are pointing to the same list.

#If you change something at the top level (e.g., add a new key-value pair), 
# it will not affect the original dictionary.