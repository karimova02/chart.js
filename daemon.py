import threading 
import time

def first():

  print("first is started")
  print("second is started")

def second():
   print("Please start")
   print("Please stop") 

first()
second()