import time
timestamp = time.strftime("%H:%M:%S", time.localtime())
p = time.strftime("%H", time.localtime())
if int(p)<12 :
    print("Good Morning, Have a nice day sir")
elif int(p)>=12 or int(p)<20:
    print("Good evening sir")
elif int(p)>=20 :
    print("Good Night Sir")