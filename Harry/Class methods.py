class dj:
    company = 'Google'
    def intro(self):
         print(f'Employee name is {self.name} and company name is {self.company}')

    def cha(cls, nc):
         cls.company = nc #this will change name only for that perticular instsnce
    
    @classmethod #classmethod is used to pass first argument as a class, it is normally passed as instance
    def chac(cls, nci): #it is used to address the class directly
         cls.company = nci

e1 = dj()
e2 = dj()
e1.name = "harry"
e2.name = "baj"

e1.intro()
e1.cha('samsung')
e1.intro()

print(dj.company)

e2.chac('Microsoft')
e2.intro()
print(dj.company)






