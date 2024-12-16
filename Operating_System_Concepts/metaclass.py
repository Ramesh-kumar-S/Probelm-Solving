# Define a custom metaclass
class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        # Add a custom method to the class
        dct['custom_method'] = lambda self: f"This is a custom method in {
            name}"
        # Create the class
        return super().__new__(cls, name, bases, dct)

# Define a class using the custom metaclass


class MyClass(metaclass=CustomMeta):
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value is {self.value}")


# Example usage
obj = MyClass(10)
obj.display()  # Output: Value is 10
print(obj.custom_method())  # Output: This is a custom method in MyClass
