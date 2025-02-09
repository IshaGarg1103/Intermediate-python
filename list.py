mylist=["banana","cherry","apple"]
print(mylist)

item=mylist[::-1]
for i in mylist:
    print(i)

#how to isert an element
mylist.append("orange")
mylist.insert(1,"apple")
mylist.remove("apple")
print(mylist)
mylist.pop()
print(mylist)
list1=['1','2','3','4','5']
list1.pop(2) #index as argument
print(list1)
list1.clear()
print(list1)
mylist.reverse()
print(mylist)
list1=[2,4,3,1]
list1.sort()
print(list1)