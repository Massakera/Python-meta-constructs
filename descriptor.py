class CustomDescriptor:
    def __get__(self, instance, owner):
        print("Getting the attribute")
        return instance._value

    def __set__(self, instance, value):
        print("setting the attribute")
        instance._value = value

class MyClass:
    attribute = CustomDescriptor()

my_object = MyClass()
my_.my_object.attribute = 42
print(my_object.attribute)
