import os
# def changer():
#     x = 1
#     for f in os.listdir('exi'):
#         if f.endswith('.txt'):
#             os.rename(f'exi\{f}', f'exi\{x}.txt')
#             x += 1

def changer2(path, ext):
    x = 1
    for f in os.listdir(path):
        if f.endswith(ext):
            os.rename(f'{path}\{f}', f'{path}\{x}.{ext}')
            x += 1
        else:
            print(f'No such file exit with {ext} extension.')

a = input('Give the path to the folder: ')
b = input('Give the extention of the file: ')
changer2(a, b)





