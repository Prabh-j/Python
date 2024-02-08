x = [1,2,3.4,5]

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Person('baj', 19)

print(a.__dict__) #give the variable and their valuees in the form of key values pairs
print(help(Person)) #give details about the given argument
print(dir(x)) #give all the methods and fuctions that can be used on argument



