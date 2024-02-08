t = (1, 5 , 85, 54, 13,23, 35, 49)
g = (12) #class is int because there is only one value, avoid it by using coma like (12,)
print(type(g))
print(t)

if 54 in t:
    print('it is')

t2 = t[1:5] #it create a new tuple and original tuple remain unchanged
print(t2) 
print(t)

#to change type

c = ('canada', 'usa', 'india', 'japan', 'russia')
temp = list(c) #it change tuple into list to allow changes
temp.append('china')
temp.pop(2) #pop accept only one value and only integar value
temp[2]= 'finland' #it will replace the existing value
c =tuple(temp)
print(c)

NorthAmerica = ('Greenland', 'Canada', 'Maxico')
SouthAmerica = ('Brazil', 'Peru', 'chile', 'argentina')
America = NorthAmerica + SouthAmerica #it will merge and create new tuple
print(America)

tup = (0,1,1,2,3,5,6,2,3,4,0,1,5,6,6,8)
print(tup.count(3)) #count the accurance
y = tup.index(2, 6, 11) #first is the value we are finding idex of, after the slicing acoording to second and thired value
print(y)
print(len(tup))