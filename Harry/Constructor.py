class Person:
    
    def __init__(self, n, occ, age): #__init__ is a built in function used to make a consructor
        print('This function will be automatically called each time a object is made.')
        self.name = n # name is a constructor
        self.occ = occ #no need for default values
        self.a = age

    def intro(self):
        print(f'{self.name} is a {self.occ} of {self.a} years.')


a = Person('Harry', 'Actor', 25) # values can be passed as arguments
b = Person('Prabh', 'Finder', 19) #no need to modify each variable individually.

a.intro()
b.intro()

