a = int(input('What is the hour right now: '))
m = int(input('What is the minutes right now: '))
b = (input('am or pm: ').capitalize())

if(b == 'Am'):
    if(1<=a<6 or 12==a):
        print('Good Night')
    else:
        print('Good Morning')
else:
    if(1<=a<4 or 12==a):
        print('Good afternoon')
    elif(4<=a<9):
        print('Good Evening')
    else:
        print('Good Morning')

print('Time right now is', str(a) + ':' + str(m), b)