def greet(fx): # a decorator modify a functions result
    def mx(): #this is basic syntax to write a constructor
        print('Good Morning')
        fx()
        print('Thanks for using this function.')
    return mx


def greeting(f):
    def mjx(*args, **qwargs): #if the function we are using arguments, we have to put args and qwargs as agrument
        print('Good Morning')
        f(*args, **qwargs)
        print('Thanks for using this function.')
    return mjx

@greet # this way we only have to use decorator once and it will automatically appear each time we call function hlo
def hlo():
    print('Hello world')

def add(a,b, c): # we can pass as many argumesnt as we want
    print(a+b+c)


hlo()

greeting(add(5, 7, 10)) #this way we have to use decorator every time we use the function
greeting(add)(5, 7, 10)
