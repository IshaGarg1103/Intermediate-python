#METHODS TO MAKE SHALLOW COPY
import copy

mydict={1:"jim",2:"pam",3:"karen"}
dict1_copy=mydict
dict2_copy=dict(mydict)
dict3_copy=mydict.copy()
dict4_copy= copy.copy(mydict)
print(dict1_copy)
print(dict2_copy)
print(dict3_copy)
print(dict4_copy)