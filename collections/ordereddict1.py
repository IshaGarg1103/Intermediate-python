#ORDERED DICT

from collections import OrderedDict

od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
print(od)  # Output: OrderedDict([('first', 1), ('second', 2), ('third', 3)])

od.move_to_end('first')
print(od)  # Output: OrderedDict([('second', 2), ('third', 3), ('first', 1)])
od.move_to_end('third', last=False)
print(od)  # Output: OrderedDict([('third', 3), ('second', 2), ('first', 1)])

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
print(od1 == od2)  # Output: False (because the order differs)
#meanwhile, if dictionary was out of order, it would still be equal if key and pair matches

#reversing :
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
for key in reversed(od):
    print(key)