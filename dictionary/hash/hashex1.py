class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))  # Hash based on name and age

    def __eq__(self, other):
        return (self.name, self.age) == (other.name, other.age)

# Create instances
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

# Use as dictionary keys
d = {p1: "Alice's data", p2: "Bob's data"}
print(d[p1])  # Output: "Alice's data"