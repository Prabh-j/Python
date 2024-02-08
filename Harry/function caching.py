from functools import lru_cache
from time import sleep

@lru_cache(maxsize = None) #lru decorator save result that program know so avoid running function again if input is repeated
def func(a): #use memory so use only when needed
    sleep(4)
    return a*a
    

print(f'Square of 4: {func(4)} ')
print(f'Square of 9: {func(9)} ')
print(f'Square of 24: {func(24)} ')
print(f'Square of 4: {func(4)} ')
print(f'Square of 14: {func(14)} ')
print(f'Square of 9: {func(9)} ')
print(f'Square of 24: {func(24)} ')










