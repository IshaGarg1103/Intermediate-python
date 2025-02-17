#defaultdict
from collections import defaultdict

#why is it used? : because it assigns default value to the
#key that doesn't exist, when we try to access that key

count = defaultdict(int) #creating dict with default value of keys set as 0

#1) Count the frequency of elements in a list
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
for item in data:
    count[item] += 1

print(dict(count)) #{'apple': 3, 'banana': 2, 'orange': 1}

#2) Create a defaultdict with default value []
grouped_data = defaultdict(list)

# Group items by their first letter
data = ['apple', 'banana', 'orange', 'avocado', 'berry']
for item in data:
    grouped_data[item[0]].append(item)

print(grouped_data)