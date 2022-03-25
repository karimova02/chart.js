import threading
def a():
    for x in range(20):
        print("What's up bro!")
def b():
    for x in range(20):
        print("Encapsulation")
def c():
    for x in range(20):        
         print("Human Computer Intraction")
t1=threading.Thread(target=a)
t2=threading.Thread(target=b)
t3=threading.Thread(target=c)    
t1.start()
t2.start()
t3.start()
