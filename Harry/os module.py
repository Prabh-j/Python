import os

# if not os.path.exists('harry\data'):
#     os.mkdir('harry\data')

# for i in range(1, 13):
#     if not os.path.exists(f'harry\data\day {i}'):
#         os.mkdir(f'harry\data\day {i}')
#     os.rename(f'harry\data\day {i}', f'harry\data\month {i}')


folders = os.listdir('harry\data')
print(folders)
for f in folders:
    print(f)
    print(os.listdir(f"harry\data\{f}"))

# f = open('harry\data\month 5\doc.txt', 'w+') 


print(os.getcwd())
os.chdir('Apps')
print(os.getcwd())
