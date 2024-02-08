#a tower of classes built on one and another

class empl:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'Name is {self.name}')

class danceer(empl):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

    def show(self):
        super().show()
        print(f'Dance is {self.dance}')

class ed(danceer):
    def __init__(self, name, dance, job):
       self.name = name
       self.dance = dance
       self.job = job

    def show(self):
        super().show()
        print(f'job type is {self.job}')
    
o = ed('Baj', 'break dance', 'part time')
print(o.dance)
print(o.name)

o.show()
print(ed.mro()) # Method Resolution Order, give the order of places python will look for mentioned method












