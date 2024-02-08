import time 
t = time.strftime('%H:%M,%S')
print(t)
h = int(time.strftime('%H'))
m = int(time.strftime('%M'));
s = int(time.strftime('%S'))

if(1<=h and h<6 and m<=59 and s<=59 or 21<=h and h<24 and m<=59 and s<=59):
     print('Good Night')
elif(6<=h and h<12 and m<=59):
      print('Good Morning')
elif(12<=h and h<16 and m<=59):
      print('Good afternoon')
elif(16<=h and h<21 and m<=59):
      print('Good Evening')
