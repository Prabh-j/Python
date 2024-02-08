class area:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y

rect = area(5, 6)
print(rect.area())

class circle(area):
    def __init__(self, radius, radiu):
        super().__init__(radius, radiu)
    
    def area(self):
        return 3.14 * super().area() #super to modify method from parent class in child class.


a = circle(5,5)
print(a.area())
