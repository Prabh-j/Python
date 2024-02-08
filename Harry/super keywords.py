class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show1(self):
        print(f'Employee id of {self.name} is {self.id}.')


e1 = employee('Rohit', '420')
e2 = employee('Naval', '410')
e3 = employee('Maan', '400')

e1.show1()
e3.show1()

class programers(employee):
    def __init__(self, name, id, lan):
        super().__init__(name, id) #this will inherit given variable so we do not need to define them again.
        self.lan = lan
        super().show1() #this will call the function from parent class

    def show2(self):
        print(f'{self.name} use {self.lan} language.')

e4 = programers('Baj', 456, 'Python')
e4.show2()
e4.show1() #this will first check if child class has any show1 func, if not then it will look in parent class.








