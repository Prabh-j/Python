# global variable is a variable created anywhere except inside a function
a = 10 #global variables can accessed anywhere in the program, even inside a fuction
b = 1
c = 5

print('c is',c)

# local variable is a variable created inside a function
def c():
    b = 8 #local variable always overrule global variable but only inside function, outside the function global variable remain unchanged
    d = 13 # local variable can only be accessed inside a function
    global c # this will turn the following variable into a global variable and the overwritten value will reflect even outside the function
    c = 11 
    print('in the function')
    print('a is',a)
    print('b is',b)
    print('c is',c)
    print('d is',d)

c()

print('outside function')
print('a is',a)
print('b is',b)
print('c is',c)
# print(d)  #this will throw an error because it cannot access a variable inside a function 


