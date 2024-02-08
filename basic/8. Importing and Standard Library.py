import Module # can also say as m to shorten name
Course = ['history', 'math', 'cs', 'art']
index = Module.find_index(Course, 'cs')
print(index)

from Module import find_index, test # functions can also be named, can also import everything with *
inde = find_index(Course, 'cs') #can also import a specific function from a module
print(inde)
print(test)