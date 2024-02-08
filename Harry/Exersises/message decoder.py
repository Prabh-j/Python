import string
import random

def reverse(x): #we can also reverse string with, a[::-1]
    k = ''
    for y in range(len(x)):
       p = (x[len(x)-1-y])
       k = k+p
    return k
       
#encryption

a = input('Enter the mesaage you want to encrypt: ').lower()
b = input('Do you want to encrypt it. (y/n): ').lower()

if b == 'y':
    c = a.split()
    for n,i in enumerate(c):
        
        r = ''.join(random.choices(string.ascii_letters, k = 3))
        p = ''.join((random.choices(string.ascii_letters, k = 3)))
    
        if len(i) >= 3:
            c[n] = r + reverse(i) + p 
        else:
            c[n] = reverse(i)
elif b == 'n':
    print("Thanks for typing,\nBye.")

else:
    print("Please enter a valid response,\nThanks.")

print(' '.join(c))

#deencyption

u = input('Do you want to deencrypt a sentance. (y/n): ').lower()

if u == 'y':
    d = input('Do you want to deencrypt\na) Previous encrypted message\nb) A Custom Message\n:').lower()

    if d == 'a':
        for m,p in enumerate(c):
            if len(p) >= 3:
                c[m]= reverse(p[3:-3])
            else:
                c[m] = reverse(p)

        print(''.join(c).capitalize())

    elif d == 'b':
        e = input('Enter the Message you want to Deencrypt: ')
        g = e.split()
        for o,q in enumerate(c):
            if len(q) >= 7:
                g[o] = reverse(q[3:-3])
            elif len(q) <= 2:
                g[o] = reverse(q)
            else:
                print(f"{len(q)} is not encryped.")

        print(' '.join(g).capitalize())

    else:
        print("Please enter a valid response,\nThanks.")

elif u == 'n':
    print("Thanks for typing,\nBye.")

else:
    print("Please enter a valid response,\nThanks.")



