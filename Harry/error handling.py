n = input('enter a number: ')

try: # try to run code only if it can be run
    for i in range(1, 11):
        print(f"{n} x {i} = {i*int(n)}")

except Exception as e: # this will tell the type of error
    print(e)

a = [1 , 4 , 5]
print(a[n])
try: # try to run code only if it can be run
    for i in range(1, 11):
        print(f"{n} x {i} = {i*int(n)}")

except SyntaxError: # to excecute different code in the case of differet errosrs
    print('syntakerror')
except ValueError:
    print('valueerror')


try: # try to run code only if it can be run
    for i in range(1, 11):
        print(f"{n} x {i} = {i*int(n)}")

except:
    print("it is an error")





