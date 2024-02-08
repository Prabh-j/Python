listname = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(listname[2])
print(listname[1:])
print(listname[1:-3])
print(listname[4:11:3]) # 4 is initial index, 11 is final and 3 is difference between them

if 4 in listname:
    print('yes')
else:
    print('no')

if 'har' in 'harry': #same thing applies for string
    print('yes')

lst = [i for i in range(5)] #list comprehension
print(lst)

lst1 = [i*i for i in range(5) if i%2==0] #conditions can be added too
print(lst1)
