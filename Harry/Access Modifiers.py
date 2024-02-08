class emp:
    def __init__(self, name, age):
        self._name = name
        self.__age = age
    
    def greet():
        print('hlo')

e1 = emp('jot', 19)
# print(e1.__age) # this will throw an error
print(e1._emp__age) # we can put two _ for name mangling, and retrict direct acess to that variable, but we can still acess it indirectly

print(e1._name) # _ infront is for protected variables, that we decide to believe as protected, a kind of standardisation, but it does not perform any triks






