nums = [1, 2, 3, 4, 5]
# For loop
for num in nums:
    if num == 3:
        print('found')
        break
    print(num) #it print values until it gets to the specific value but it stop before printing that value

for num1 in nums:
    if num1 == 4:
        print('found')
        continue
    print(num1) #it print all values but replace the value with the text we wanted

for num in nums:
    for letter in 'abc':
        print(num, letter) #nested loop, loop inside a loop

for i in range(10):
    print(i)        #it print all values within given range of values, start from 0 by defalut

for i in range(1, 11):
    print(i)        #we can specify intial value and limit

#While loop
x = 0
while x < 10: #keep looping until conditions are met, do not inlude the last value itself
    if x == 5:
        break # to break the loop at given condition
    print(x)
    x+= 1    #increase value each time it loop back

y = 8
while True: #infinite loop, break statement is must , ctrl+c to break a loop
    if y == 15:
        break # to break the loop at given condition
    print(y)
    y+= 1 

