import threading 

event =threading.Event()

def func():
   print("Install Flask")
   event.wait()
   print("Flask installation is started")

t1 = threading.Thread(target=func)
t1.start()

assignment = input("Do you want to start installation of Flask")
if assignment =="yes":
   event.set()
