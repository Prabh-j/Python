#lambda create a light weight unnamed function, in the form of a variable, it is used to pass function as argument 
#it consists of three parts, first one is variable name, second is values accepted by fuction and third is what function returns


percent = lambda x,y: (x*100)/y 
print(percent(567, 600), '%')

def jpg(fuc, x , y):
    return fuc(x, y) + 5

print(jpg(percent, 567, 600)) 

def jpu(fuc, x):
    return fuc(x) + 5

print(jpu(lambda a: a*a*a, 25)) # lambda can also define the functin on the spot

