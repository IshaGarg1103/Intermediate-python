#Strings: ordered, immutable, text representation

str= 'I\'m a programmer'
print(str) #I'm a programmer

str="""Hello \
World"""
print(str) #Hello World #no line break

str="   hello world   "
print(str.strip()) #wouldn't change the string because it is immutable
print(str) #'   hello world   '
str=str.strip()
print(str) #hello world

print(str.replace("World","universe")) #hello world 
#it is case sensitive

print(str.replace("world","universe")) #hello universe


