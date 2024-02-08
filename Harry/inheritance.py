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

class programers(employee): #interharitance means inheriting everything from pre defined class
    def __init__(self, name, id, lan):
        super().__init__(name, id)
        self.lan = lan

    def show2(self):
        print(f'{self.name} use {self.lan} language.')

e4 = programers('Baj', 456, 'Python')
e4.show2()

