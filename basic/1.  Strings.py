print ('hello')
print ('let me show you something \nthis is a new line') # called escape squences, cut the line in output

my_name = 'its a vaariable'
print (my_name)
u1 = 'BOBY\' NAME, single quote problem'
u2 = "or you can' use double at beginig and end "
print (u1, u2)
u3 = '''use more
than 3 qoutes to 
make multipe 
line string'''

print(len(u1)) #to count length of string

print(u1[0]) #to print the value at given number in string, value is called index and it start with zero

print(u2[0:5]) #to print certain given amount of value, it will include first value but not last value
print(u2[:5]) #you can skip first index if counting from start,
print(u2[5:]) #same

print(u2.lower()) #to lower al characters, can use .upper() to uppercase

print(u1.count("a")) #to count repition of given value in string

print(u1.find('single')) #find the index of value

u4 = u3.replace('3', '7') #replace values or words, need new variable every time or set same variable, important
u1 = u1.replace('NAME', 'age') #have to be same case
print(u4)
print(u1)

u5 = u1+u2 # add string, called cancatination but leave no space
u6 = u1 + ', ' + u2 #can use string inbetween to modify result
u7 = u1 + ' and that is it' #combining andmaking new string
u8 = '{}, {}. Welcome!'.format(u1, u2) # {} are placeholders and format is used to fill those places and, follow their order
u9 = f'{u1}, {u2.upper()}. Welcome!' # called f strings, can write strings and code directly in placeholders.
print(dir(u1)) # dir tells every possible method that can be used with string
print(help(str)) #give avery possible method and their use, can be used to find  perticular method like -help(str.lower)
print(u5)
print(u6)
print(u7)
print(u8)
print(u9)