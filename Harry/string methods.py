a = '!?haryy ??"?!\n!! jesharyy'
b = 'hello My frIenDs'
print(a.upper())
print(a.rstrip('!')) #strips the given trailing character, not in the front
print(a.replace('haryy', 'john')) #replace characters everywhere
print(a.split()) # split the string at the given indication(here the value is empty so it will split the string everytime there is a space) into values of lists
print(b.capitalize()) #capatalize first character and lower any other case
print(b.center(50)) #centre method add spce in front to alighn text in centre
print(a.count('r')) #count the occurance of given value
print(b.endswith("d")) #check if string end with this value
print(b.endswith('my', 2, 8)) # we can slice and check
print(a.startswith("!")) #same as endswith
print(b.swapcase()) #swap upper case with lower and vica versa
print(b.title()) # capatalize each word, and lower case any unnessary upper cased character
c = "he's name is hona, he is smart" 
print(c.find('is'))
print(b.isalnum()) #true if strings contain only a-z, A-Z, 0-9. this contain space, hence false
print(a.isalnum()) #contain " and ?!
print(a.isalpha()) # true with a-z A-Z only
print(a.islower()) #true if all are in lower case
print(a.isprintable()) #true if all values in string are presentable, here no becauz \n
print(a.isspace()) #check for space
print(a.istitle()) #check if ecah word of string is capatlize 
print(a.isupper()) #like islower

