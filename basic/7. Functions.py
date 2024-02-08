# fuction, set of instructions, help so we dont need to repeat the code
def hel():
    pass #to leave a function empty to do it later
print(hel())

def hell():
    print('hello f')
hell()

def hello():
    return 'hello g' #it turn the function equal to itself, in this case into a string
print(hello().upper()) #same commanads as strings can be used

def hel1(greet): #greet is an parametre, 
    return '{} function.'.format(greet) 
print(hel1('hi')) #hi is argument, this way we can decide the value of greet every time we execute the function

def hel2(greet, name = 'jack'): #jack is default value, order is alwalys non default then default values
    return '{}, {} function.'.format(name ,greet) #placeholders are assigned respectively to the format
print(hel2('hi', name = 'corn'))

def info(*args, **kwargs): #we can use different name but args and kwargs are commonly used
    print(args) # * means a tuple and ** means a dictionary, any extra value passed in fuction the dont have a parametre gets positioned into tupil or diction depending on data type
    print(kwargs) # 
info('math', 'art', name= 'john', age= 25)
courses = ['math', 'art']
inf = {'name': 'john', 'age': 25}
info(*courses, **inf) #*, ** unpack the tuples and dictionaries and pass them individually


Days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #list of days in months, first value is place holder to manle naming months easier

def lyear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) # formula for leap year

def mdays(month, year): #return number of days in month
    if not 1 <= month <=12 : 
        return 'invalid'
    if month == 2 and lyear(year):
        return 29
    return Days[month]

print(lyear(2020))
print(mdays(2, 2010))