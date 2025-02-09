#lists: ordered, mutable allows duplicate elements

mylist=["banana","herry","apple"]
print(mylist)

new_list=sorted(mylist)
print(new_list)

mylist=[0]*5
print(mylist)

#if change is made in one list, then it is seen in the second list as well
list_org=["banana","cherry","apple"]
list_cpy=list_org
list_cpy.append("lemon")
print(list_org)
print(list_cpy)

#if doesn't want the change to appear in the original list
#first method
list_org=["banana","cherry","apple"]
list_cpy=list_org.copy()
list_cpy.append("lemon")
print(list_cpy)
print(list_org)
#second method
list_org=["banana","cherry","apple"]
list_cpy=list(list_org)
list_cpy.append("lemon")
print(list_cpy)
print(list_org)
#third method
list_org=["banana","cherry","apple"]
list_cpy=list_org[::1]
list_cpy.append("lemon")
print(list_cpy)
print(list_org)
