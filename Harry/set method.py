s1 = {1,2,3,5,4,8,6}
s2 = {8,5,9,7,0}
s3 = {8,5,9}
s4 = {1,5,8,5,8,5,9}

print(s1.isdisjoint(s2)) #check if set have anything in common(false) or not(true)
print(s1.issuperset(s2)) #check if first set have all values os second set(true) or not(false)
print(s1.issubset(s2)) #opposite of superset
s1.add(15) #add any one value to the set
s1.update(s2) #add more than one value to the set
s1.remove(15) #remove given value from the set
s1.discard(15) #remove given value from the set, does not raise error
s1.pop() #remove any random value from the set
print(s1.pop())
del s3  #delete whole set
s4.clear() # delete all values within the the set but keep the set
if 4 in s1:
    print('it is')
else:
    print('not')

#union
print(s1.union(s2)) #this create a new set as a byproduct of both
s1.update(s2) #this add the second set in the first original set
print(s1, s2)
#intersection
print(s1.intersection(s2)) #takes commom value
s1.intersection_update(s2)
print(s1, s2)
#symmetric difference
print(s1.symmetric_difference(s2)) #takes non commom value
s1.symmetric_difference_update(s2)
print(s1, s2)

print(s1.difference(s2)) #takes values that are in original set but not in second set
s1.difference_update(s2)
print(s1, s2)




