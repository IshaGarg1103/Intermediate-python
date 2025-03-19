#try and except
try : 
    a = 5 / 0
except Exception as e:
    print(e)

try:
    a = 5/0
    b=a+'10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally : #always runs, if there is exception or not
    print('cleaning up...')

