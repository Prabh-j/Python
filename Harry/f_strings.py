#how code was usedto before f string
l = 'Hello, my name is {} and i am from {}'
n = 'Prabh'
c = 'Punjab'
print(l.format(n, c)) # format assign value to placeholders, respectavely(to aviod this sequence, we can put index number in placeholders).

#f string
print(f"My name is {n}, from {c}") #with f strint we can directly assign variables to placeholders
print(f'{20*5}') #inside of placeholder work like a variable
print(f"My name is {{n}}, from {{c}}") #double brackets for raw output

