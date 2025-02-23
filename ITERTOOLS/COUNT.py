from itertools import count, cycle, repeat

a=[1,2,3]
for i in repeat(1, 4):
    print(i, end =' ')

print('\n')
for i in count(10):
    print(i,end=' ') #10 11 12 13 14 15
    if i == 15:
        break
