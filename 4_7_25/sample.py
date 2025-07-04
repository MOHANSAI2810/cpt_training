import time
import os
try:
    a=int(input())
    print(a)
    raise ValueError  
except (ValueError,KeyboardInterrupt) as e:
    print(e)
finally:
    print("wait 5 seconds")
    time.sleep(5)
    os.system("cls")
