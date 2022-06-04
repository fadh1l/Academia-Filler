
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
perm = input("open up ACADEMIA website \n open the feeback page (refresh if already opened up)... I need all fields to be blank \n now come back \n if done type 'y' to proceed (y/n) ")
if perm == "y":
    comment = input("what comment wud u lyk to add in common to all??  ")
    print("nice choice of words master")
    print("NOW OPEN UP ACADEMIA WEBSITE FAST, tap somewhere blank AND JUST STARE AT IT atleast for a minute, kay??\nsince this is basically a huge macro don't touch anything or else the keystrokes will be executed somewhere else")
    time.sleep(5)

    def autotab(u):
        for k in range(u):
            keyboard.tap(Key.tab)

    def fillerfn(z):
        keyboard.type('Excellent')
        time.sleep(z)
        keyboard.tap(Key.enter)
        keyboard.tap(Key.tab)
      

    def autofill(x,y,z):
        for i in range(x): 
            fillerfn(2)
            for j in range(y-1):
                fillerfn(z)
            keyboard.type(comment)
            autotab(2)   
            
    autotab(2)
    autofill(9,14,1.6)
    autotab(1)
    autofill(6,13,1.6)
    print("thank me later \n ~fadhil")
else:
     print("restart and just type 'y' plz ")

















