def funtionname(a, b):
    mean = (a*b)/(a+b)
    print(mean)

num1 = 5
num2 = 12
funtionname(num1, num2)

def avg(a=5, b=9):
    print('the average is: ', (a+b)/2)

avg() #default values
avg(1, 7) #new values will overide default values
avg(b = 11, a = 7) #keyword argument

def name(fname, mname = 'Wattson', lname = 'Smith'):
    print('Hello,', fname, mname, lname)

name('rohan', 'kumar')

def ave(*nuers): #tuple is creaded with name numbers, one * is for tuple, two are for dictionary
    s = 0
    for i in nuers:
        s = i + s
    print('average is:', s/len(nuers))
    return s/len(nuers)
    return s/len(nuers) #return comand works only once
ave(5,8,6,7)
c = ave(5, 11)
print(c)