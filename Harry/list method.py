l = [1,2,3,45,75,42,3,8,13,27]
l.append(9) #add value at the end
l.sort(reverse=True) #sort the list both ways, assending by default
l.reverse() #reverse the order of original list
print(l.index(45)) #gives the index of first occurance of the value
print(l.count(3)) #count the occuranceof given value
m=l.copy() #copy the content of whole list into another list, without copy it would have reffered to original list
m[0] = 0 #this will not effect original list
m.insert(1, 169) #here first value(1) is index and second value(169) is the value to be inserted in the list
n = [22,33,44,55]
m.extend(n) #it will take values from n list and put them into m, but it will modify original list
k = m + n #lists can be merged this way too to prevent changes in original list
print(l)
print(m)
print(k)