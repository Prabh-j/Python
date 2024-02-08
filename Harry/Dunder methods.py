class employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __len__(self):
        return len(self.name)
     
    def __call__(self):
        print("This method is used to call a object like a function.")
    
    def __str__(self):
        return 'This method is called when we try to print obejct itself'
    
    def __repr__(self):
        return 'This method is does same as str method but it is second priorety, means it will be envoked in the absence of str method'
    
e = employee('baj', 19)

print(len(e))
print(e)
e()
repr(e())











