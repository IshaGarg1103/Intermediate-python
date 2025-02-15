str='how are you doing ?'
mylist=str.split()
print(mylist) #['how', 'are', 'you', 'doing', '?']

mylist=str.split(" ")
print(mylist) #['how', 'are', 'you', 'doing', '?']

str='how,are,you,doing?'
mylist=str.split(",")
print(mylist) #['how', 'are', 'you', 'doing?']

newstr=' '.join(mylist)
print(newstr)