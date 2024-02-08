s = {'Name': 'Prabh', 'Age': 19, 'height': 178, 'Race': 'Brown', 'Nationality': 'Punjab'}
n = {'Sex': 'Male', 'Alive': True, 'Occupation': 'Student'}
print(s)
s.update(n) #update first dict by adding values of second
print(s)
n.clear() #to clear the dictionary, create empty dictionary

s.pop('Age') #delete the key value pair, only one at a time
s.popitem() #delete last key value pair

del n #delete the whole dict
del s['Nationality'] #delete key vaue pairs, one at a time