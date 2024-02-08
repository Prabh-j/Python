Student = {'name': 'John', 'Age': 19, 'courses': ['Math', 'Science']} #called dictionaeries, store data in form of keys and their values(age is key, 19 is value)
print(Student) 
print(Student['courses']) #use key to acess values in it
print(Student.get('courses')) #use key to acess values in it
print(Student.get('phone', 'not found')) #we can make a default value for keys(only mentioned in this command) that do not exist
Student['phone'] = '5555-555555' #create a new key and value in it
Student['name'] = 'Jenney' #update an value
Student.update({'name': 'Britney', 'Age': 20, 'sex': 'male'}) #update multiple values and add any number of new value in one shot
print(Student.get('phone')) 
print(Student) 
del Student['Age'] #delete key and value alongside
name = Student.pop('name') #delete the key from dic
print(Student)
print(name) #pop return the value it deleted
print(len(Student)) #gives number of keys
print(Student.keys()) #gives names of individual keys
print(Student.values()) #gives only values
print(Student.items()) #gives keys and values inform of pairs

for look in Student: #loop, will only give name of keys, not values
    print(look)
for look, here in Student.items(): #this loop will give both keys and value
    print(look, here)