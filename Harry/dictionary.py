s = {'Name': 'Prabh', 'Age': 19, 'height': 178, 'Race': 'Brown', 'Nationality': 'Punjab'}
print(s['Age'])
print(s.get('Age')) #it key do not exit, it will not throw error

print(s.keys()) #give keys
print(s.values()) #give values

for key in s.keys():
    print(s[key]) #print values
    print(f"value of {key} is {s[key]}") #prints keys and their values

print(s.items()) #gives keys and their values

for key, values in s.items():
     print(f"value of {key} is {values}") 



