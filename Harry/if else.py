a = int(input('your age: '))
print("your age is:", a)
if(a>=18 and a<100):
    print("you are permited")
elif(a>=100):
    print('die already you old man')
else:
    print("fuck off kid")

n = int(input('any number: '))
if(n>0):
    print("its positive")
if(n==0):
    print("its zero") 
else:
    print("its negative") #else statement is excepion only for previous if statement, it has no link with any other if statement, that is why we use elif 

if(n<0):
    print("its an integer")
else:
    if(n==0):
        print('its whole number')
    else:
        print('its a natural number')

