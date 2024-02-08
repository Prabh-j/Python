a = input('give me a number between 5 and 11: ')

if a == "quit":
    print(' you are out')

elif 5>int(a) or int(a)>11:
     raise ValueError('write a number betwwen 5 and 11: ')


print('the inpur is coreect')

#with error handling, code will not work because if try is sucessfull, it will raise error means except will also excute, means another error with except, because a is a string and not 'quit'.

# try:
#     if 5>int(a) or int(a)>11:
#         a = int(a) #to fix the above problem
#         raise ValueError('write a number betwwen 5 and 11')


# except:     # run this code if there is an exception in try
#     raise ValueError('write a number betwwen 5 and 11')
# else:
#      if a == str(a) and a != "quit":
#        raise ValueError('invalid outcome')

# print('the input is coreect')
# no fix