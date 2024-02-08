#make a reminder app 
from win10toast import ToastNotifier
import time
from plyer import notification

toast = ToastNotifier()
def a1():
    while True:
        toast.show_toast(
            "Water Break",
            "Its time to drink water, take a break and rest for a bit.",
            duration = 2,
            icon_path = "wolf.ico",
            threaded = True
        )
        time.sleep(7)

#other way
def a2():
    while True:
        time.sleep(7)
        notification.notify(title="water",
                            message ="you should drink water",
                            timeout=2)

a2()
