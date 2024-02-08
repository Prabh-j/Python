class Person: #class is a blueprint for code 
    name = "Pascal"
    age  = 38
    occupation = "Photographer"
    def intro(self): #self means value in that perticular object
        print(f'{self.name} is a {self.occupation}')
 
#
a = Person() #we can built as many structure as we want with blueprint
b = Person() #here self is b and its value is independent from a and c or any other variable
c = Person() #c is a object

print(a.name)
a.name = 'Jason' #we can modify values to personalize the blueprint
a.occupation = 'Actor'


b.name = 'Brittney'
b.occupation = 'Racer'

a.intro()
b.intro()
c.intro() # if we do not make any changes then the values remain default


