class Animal:
    def __init__(self, animal, breed):
        self.animal = animal
        self.breed = breed

    def makes(self):
        return f'{self.animal} make some sound'
    
class Cat(Animal):
    def __init__(self,breed, color):
        super().__init__('cat' ,breed)
        self.color = color

    def makes(self):
        return f'{self.breed} Mew!'
    
d = Animal('snake', 'black mamba')
c = Cat('Mountain cat', 'black')

print(d.makes())
print(c.makes())








