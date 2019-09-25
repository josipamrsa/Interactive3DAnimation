import bge
import bpy
import math
import random

cont = bge.logic.getCurrentController()
sc = bge.logic.getCurrentScene()
own = cont.owner

def moveAround(obj,act,speed):
    currPosition = obj.localPosition
    speed = speed + 0.01
    act.dLoc = [0, speed, 0]
    if obj.localPosition > 0.2:
        cont.deactivate(act)
        act.dLoc = [speed, 0, 0]
    else:  
        cont.activate(act)
        print(obj.localPosition)
    
    
wolf = sc.objects['WolfArm']
movAct = cont.actuators['WolfMove']
speed = movAct.dLoc[1]

moveAround(wolf,movAct,speed)

