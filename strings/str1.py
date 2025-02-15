from timeit import default_timer as timer

str='how are you doing ?'
mylist=str.split()
print(mylist) #['how', 'are', 'you', 'doing', '?']

mylist=str.split(" ")
print(mylist) #['how', 'are', 'you', 'doing', '?']

str='how,are,you,doing?'
mylist=str.split(",")
print(mylist) #['how', 'are', 'you', 'doing?']

newstr=' '.join(mylist)
print(newstr) #how are you doing?

#bad method to concatenate
start=timer()
mylist=['a']*100000
newstr=''
for i in mylist:
    newstr+=i
stop=timer()
print(stop-start)

#GOOD METHOD :
start=timer()
newstr=''.join(mylist)
stop=timer()
print(stop-start)