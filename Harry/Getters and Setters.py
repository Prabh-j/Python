class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property #getter,a type of decorator,with syntax @property, A method that allows you to access an attribute in a given class
    def ten_value(self):
        return 10* self._value

    @ten_value.setter #setter, syntax name.setter, A method that allows you to set or mutate the value of an attribute in a class
    def ten_value(self, new_value):
        self._value = new_value/10


obj = MyClass(10)
obj.ten_value = 67
obj.show()

