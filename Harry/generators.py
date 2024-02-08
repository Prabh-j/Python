def fumc(): #generator create the value on the spot instead of storing it ahead of time, saving memory 
    for i in range(50):
        yield i #here loop will run only when its needed
        

x = fumc()

print(next(x)) #next will call next value from genertor after previous values, here it is first so it is 0 
print(next(x)) #here it is 1
print(next(x)) #here it is 2
print(next(x)) #here 3 and so on 

for t in x: # this is another way to call constructor, since we used next previously x here begin at 4
    if t <25:
        print(t)
    else:
        break










