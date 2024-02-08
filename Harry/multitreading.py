import threading #to run multiple task parallel
import time
from concurrent.futures import ThreadPoolExecutor

def fun1(s):
    time.sleep(s)
    print(f'waited for {s} seconds')
    return s


t1 = threading.Thread(target = fun1, args= [5]) 
t2 = threading.Thread(target = fun1, args= [1])
t3 = threading.Thread(target=fun1, args= [4])

t1.start() # start the task that very second
t2.start()
t3.start()

t1.join() #have the program wait for t1 before fully excuting
t2.join()
t3.join()

def pj():
    with ThreadPoolExecutor() as executor:
        future = executor.submit(fun1, 5) #easier way
        future1 = executor.submit(fun1, 5)
        future2 = executor.submit(fun1, 5)
        print(future.result())
        print(future1.result())
        print(future2.result())
        
        l = [1,5,6,2,4,7]
        fu = executor.map(fun1, l) #to pass a list
        for f in fu:
            print(f)

pj()

