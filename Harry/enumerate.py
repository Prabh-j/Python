a = [42, 54, 60, 33, 21, 14, 84, 67, 91]

index =0
for mark in a:
    print(mark)
    if index == 5:
        print('Boo')
    index+=1


#enumerate, unpack a list,or similar dts, in form of index and values
for index, mark in enumerate(a): #here first variable contain index of the value and second one contain value itself
    print(mark)
    if index == 5:
        print('Boo')
    index+=1 


for index, mark in enumerate(a, start = 1): #we can also decide what is index of first value
    print(mark)
    if index == 5:
        print('Boo')
    index+=1 



