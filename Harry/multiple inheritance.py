#multiple inheritance means inheriting from multiple parent classes

class empl:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'Name is {self.name}')

class danceer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f'Dance is {self.dance}')

class ed(empl,danceer):
    def __init__(self, name, dance):
       self.name = name
       self.dance = dance
    
o = ed('Baj', 'break dance')
print(o.dance)
print(o.name)

o.show() #it will pioritize which parent class is inherited first
print(ed.mro()) # Method Resolution Order, give the order of places python will look for mentioned method








