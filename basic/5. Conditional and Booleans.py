lan = 'python'

if lan == 'python':  
    print('Its true')
if lan == 'pythn':
    print('pytho')
elif lan == 'java':
    print('its java')
elif lan == 'python':
    print('its python') 
else:
    print('no match')

#bollian
user='admin'
logged = True
if user == 'admin' and logged: #only excecute code if both conditions meet
    print('welcome')
else:
    print('denied') 

if user == 'admin' or logged: #excecute code if any of the conditions meet
    print('welcome')
else:
    print('denied')

if not logged: #excecute code if conditions is not met2
    print('log in')
else:
    print('welcome')

a= [1, 2, 3]
b= [1, 2, 3]
print(id(a))
print(id(b))
print(a == b) #check if they are equal
print(a is b) #check if they are same object(id)
c=a
print(a is c) #a and c are same objects, their id is same

#conditions that are false by default 
condition1 = False # obious
if condition1:
    print('true')
else:
    print('false')

condition2 = None #no value
if condition2:
    print('true')
else:
    print('false')

condition3 = 0 #zero of any numeric type
if condition3:
    print('true')
else:
    print('false')

condition4 = [] #empty sequence like sets(), strings'' and tuples[], used to check if it is empty
if condition4:
    print('true')
else:
    print('false')

condition5 = {} #empty dictionary, used to check if it is empty
if condition5:
    print('true')
else:
    print('false')

