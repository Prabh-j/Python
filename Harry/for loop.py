name = 'Prabhjot Singh Dhaliwal'
colors = ['white', 'blue', 'green', 'orange', 'pink', 'lavander']

for c in name:
    print(c)
    if c == 'o':
        print('here is o') #it do not replace the o, just excute after it

for color in colors:
    print(color)
    for co in color:
        print(co)

for i in range(10): #count start will zero by default and given value itself is not included
    print(i) # order of excicution is 14, 15, 16 and then 14 agian, hence two result mix
    print(i + 1)

for t in range(5,10): #we can define intial and final value
    print(t)

for t in range(0, 12, 3): # third value is for increment or deincrement, or can be called difference between output values
    print(t)

