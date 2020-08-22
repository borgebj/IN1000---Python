# coding=utf-8
"""Hackerman simulator"""
#optimert for bærbar pc
import random
import time

time.sleep(1)

txt = "Processing ....."
center = txt.center(180)
print("\n",center,"\n")

time.sleep(3)
def hackerman():
    list = []
    def rand():
        tall = random.randint(1,999)
        list.append(tall)
    def sc():
        rand()
        rand()
        rand()
        rand()
        rand()
        rand()
        rand()
        rand()
        rand()
        rand()
        rand()
        rand()
        rand()
        #
    sc()
    sc()
    sc()
    list.pop()
    print(list)
    time.sleep(0.05)

def shortcut():
    hackerman()
    hackerman()
    hackerman()
    hackerman()
    hackerman()
    hackerman()
    hackerman()
    hackerman()
    hackerman()
    hackerman()
    hackerman()

shortcut()
shortcut()
shortcut()
shortcut()
shortcut()
shortcut()
shortcut()
shortcut()
shortcut()
shortcut()
shortcut()
shortcut()
shortcut()

time.sleep(3)

txt2 = "Process complete!"
center2 = txt2.center(180)
print("\n",center2,"\n")


