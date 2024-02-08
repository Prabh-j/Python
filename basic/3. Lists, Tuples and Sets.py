#List
course = ['history', 'math', 'science', 'geography'] # called lists, used [],
print(course)
print(len(course)) #number of values in list 
print(course[2]) #gives value in list at the position asked
print(course[-2]) #negative values start from last and it start with -1
print(course[0:2]) #give range values,called slicing
course.append('Art') #add value at the end of list
print(course)
course.insert(2, 'Art') #add value to list at assigned place
print(course)
Co = ['Bio', 'Phy']
course.insert(0, Co) #add one list with other as a single value, gets recoganised as integer
print(course)
course.extend(Co) #add values of list as individual values
print(course)
course.remove('math') #remove value from list
course.pop() #remove last value of list
poped = course.pop() #pop return the value it removed
print(course)
course.reverse() #reverse the order of list
course1 = ['history', 'math', 'science', 'geography']
course1.sort() #sort list in alphabetic/accending(if number) value, changes the list itself
print(course1)
course1.sort(reverse=True) #sort list in reverse alphabectic/decending order
sortedc = sorted(course1) #return sorted list, doesnt change original list
print (sortedc)
num = [1, 5 ,8, 45, 15, 13, 4]
print(min(num)) #give minimum value
print(max(num)) #give maximum value
print(sum(num)) #add the numbers
print(num.index(15)) #gives index of value
print(18 in num) #tells if value is in list
for subject in course1: #for loop 
    print(subject)
for index, subject in enumerate(course1, start=2): #enumerate give two values, one is index
    print(index, subject)
cstr = ' - '.join(course1) #join list to string
print(cstr)
cctr = cstr.split(' - ') #split string to list
print(cctr)
empty_list = []
empty_list = list()

#Tuple
t1 = ('History', 'Science', 'Geography', 'Math') #use (), cannot be modified once created.
t2 = t1
print(t1)
empty_tuple = ()
empty_tuple = tuple()

#Sets
S1 = {'History', 'Science', 'Geography', 'Math', 'Science'} #remove duplicate value and does not care about sequence
S2 = ('History', 'Science', 'Design', 'art') 
print('Math' in S1)
print(S1.intersection(S2)) #print the common values
print(S1.difference(S2)) #values that are in S1 but not in S2
print(S1.union(S2)) #combine values of both sets
empty_set = {} #this create a dictionary instead of empty set
empty_set = set()
