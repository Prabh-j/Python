class math:
     def __init__(self, num):
          self.num = num

     def addt(self, n):
          self.num = self.num + n
          return self.num

     @staticmethod #static method is an independant method
     def add (a, b): #static method eleminate need of self argument
          return a+b


a = math(5)
print(a.addt(7)) 

print(a.add(5, 8)) # we can call it with object
print(math.add(5, 8)) # or we can also call it with class
