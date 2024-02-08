import time

innit = time.time() #this return seconds from the epoch,it is the point where the time starts,It is January 1, 1970, 00:00:00 (UTC) on all platforms.

i = 0
for i in range(50):
    print(i)

t = time.time()- innit #this way we can find how much time it took for code to run

init = time.time()

x=0
while x<50:
    print(x)
    x+=1

t1 = time.time()- init

print(t)
print(t1)


print(1)
time.sleep(3) #sleep will delay the excecution of the code, in this case by 3 seconds
print(4)


t = time.localtime() #it return the local time
for_time = time.strftime("%Y-%m-%d %H-%M-%S",t) #it is used to convert local time to readable form
for_time1 = time.strftime("%D %H:%M:%S",t)
for_time2 = time.strftime("%Y-%m-%d %H-%M-%S")
print(for_time)
print(for_time1)
print(for_time2)



#https://docs.python.org/3/library/time.html


