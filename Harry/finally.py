# finally is used to execute code no matter what, even if function return before it, useful for functions
def func():
    try:
        l = [1, 5, 9, 4, 5]
        i = int(input('enter the index: ')) 
        print(l[i])
        return 1 # return means take the value and leave the function and ignore the code in latter lines
    except:
        print('error 404')
        return 0
    
    print('i will not execute always') # here this code will not execute because function return before reacing the code



def func1():
    try:
        l = [1, 5, 9, 4, 5]
        i = int(input('enter the index: '))
        print(l[i])
        return 1
    except:
        print('error 404')
        return 0
    
    finally:
        print('i will execute always') #finally will always execute, mostly used for must actions like closing the page after the everything done and stuff

print(func()) # first the code inside the function will run then the print statement
print(func1())
