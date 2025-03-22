class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self, message,value):
        self.message = message
        self.value = value


def test_value(x):
    if x>100:
        raise ValueTooHighError('value is too high')
    if x<5:
        raise ValueTooSmallError("Value is too small",x)
try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
print("bye")