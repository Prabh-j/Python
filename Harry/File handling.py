# #open function to open a file, first argument is the path to the file, while second is mode of opening
# f = open('d:/python fake/textf.txt', 'w') # w means writing mode, it create a file if it does not exist already
# f.write('This is a new file.') # write delete previous data and write new data
# f.writelines('This is a new file.\n', 'this is sencod line') # to write multiple values
# f.close() # close the file, a mandory function to exceute the code, kinda like a bottom of bucket , content fall out with it

# f = open('d:/python fake/textf.txt', 'rb') # r for read mode, throws an error if file do not exist, b is to indicate that open file in binary format, t is for text but it is there by default
# print(f.read()) #read reads the file in form of a pharagraph
# print(f.readline()) #readline reads only one line of the file
# print(f.readlines()) #read reads all the lines of file and return it inform of a LIST, use loop to print all lines one by one
# f.close()

f = open('d:/python fake/textf.txt', 'r')
while True:
    l=f.readline()
    if not l:
        break
    print(l)


# f = open('d:/python fake/textf.txt', 'a') # a for append mode, create new file if it does not exist
# f.seek(0) # it moves the cursor to beginning, without it append will add value at end of fileby default 
# f.write('This is a new file.') #add value at the end of existing value
# f.close()

# # f = open('d:/python fake/textf.txt', 'x') # x mode create a file, thows an error if it already exit 
# #f.close()

# f = open('d:/python fake/textf.txt', 'r+') #it means read plus write,create new file if it dont exist
# print(f.read())
# f.write('This is a new very file.')
# f.close()

# f = open('d:/python fake/textf.txt', 'w+') #it means write plus read,create new file if it dont exist, + can also be used as a+
# f.write('This is a new file.')
# print(f.read()) #unable to print, don't know why
# f.close()

# # print(f) # this will print details of file like its name and mode in which its opened

# with open('d:/python fake/textf.txt', 'r') as file: #with closes the file automatically so no need of close function
#     print(file.read())

#seek, tell and trunkate
f = open('d:/python fake/textf.txt', 'r')
f.seek(5) #set the cursor position, here it is 5
f.tell() #give the cursor position
f.truncate(12) #truncate set a size limit on file, if we try to add more values than the limit it will siply drop the rest of the values
l=f.readline()
print(l)

# a example of practical use of file handling
with open('d:/python fake/textf.txt', 'a+') as file: 
    for i in range(10):
        a = input('Enter your name:')
        file.writelines([a, '\n'])
        print(file.readline()) #dont know why list appear empty
        # if len(file.readlines()) >=10:
        #     break 
    print(file.read()) #this one also dont work



