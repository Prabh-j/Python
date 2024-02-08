#recursion means putting function inside a function

#fn = f(n-1) + f(n-2)
def Febonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Febonachi(n-1) + Febonachi(n-2)
    
print(Febonachi(5))
print(Febonachi(4))
print(Febonachi(3))
print(Febonachi(2))
print(Febonachi(1))
print(Febonachi(0))