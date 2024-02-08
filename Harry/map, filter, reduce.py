l = [1,5,6,8,7,89,9,9,44,94,66,465,45]

def squ(x):
    return x*x

print(map(squ, l)) #map function is used to pass all values of collective data through a function one by one
print(list(map(squ, l))) #typecasting to convert map object to list 

print(filter(lambda x: x>20, l)) #filter fuction will filter the list(or such) according to function, if function return true then filter will keep it and otherwise drop it
print(list(filter(lambda x: x>20, l)))


from functools import reduce #reduce fuction must me imported every time

sum = reduce(lambda x, y: x+y, l) #reduce will redunce the elements of list by replacing used elements with its result in list and it will keep running on first values
print(sum) #in this example, x and y will be replaced by x+y and it will become first element, third element will become second and function will be applied on first(the result) and second(originally third) values
