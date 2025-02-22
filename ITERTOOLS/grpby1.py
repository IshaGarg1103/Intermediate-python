from itertools import groupby

persons = [{'name':'Tim','age':25},{'name':'Dan','age':26},
           {'name':'lisa','age':27}]
group_obj = groupby(persons,key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))