import copy

class MyClass:
    def __init__(self, value):
        self.value = value

    def __copy__(self):
        print("Shallow copy of MyClass")
        return MyClass(self.value)

    def __deepcopy__(self, memo):
        print("Deep copy of MyClass")
        return MyClass(copy.deepcopy(self.value, memo))

# Create an instance
obj = MyClass([1, 2, 3])

# Shallow copy
shallow_obj = copy.copy(obj)

# Deep copy
deep_obj = copy.deepcopy(obj)