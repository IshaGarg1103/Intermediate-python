#Strings: ordered, immutable, text representation

str= 'I\'m a programmer'
print(str) #I'm a programmer

str="""Hello \
World"""
print(str) #Hello World #no line break

#STRIP
str="   hello world   "
str.strip() #wouldn't change the string because it is immutable
print(str) #'   hello world   '
print(str.strip()) #hello world
#it printed stripped string, but the actual string is still the same 
str=str.strip() 
print(str) #hello world

print(str.replace("World","universe")) #hello world 
#it is case sensitive
print(str.replace("world","universe")) #hello universe