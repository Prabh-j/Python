class dj:

    def __init__(self, name, age):
         self.name = name
         self.age = age
    
    def intro(self):
         print(f'Employee name is {self.name} and age is {self.age}')
    
    @classmethod 
    def chac(cls, str): #this way we can modify the input
         return cls(str.split('-')[0], str.split('-')[1]) #this is a instance of class method 

e1 = dj('baj', 19)
x = 'prabh-19'
e2 = dj.chac(x) #calling func this way because its class method
e1.intro()
e2.intro()


