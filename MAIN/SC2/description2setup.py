import bge, bgl
import blf
import bpy
import math

cont = bge.logic.getCurrentController()
sc = bge.logic.getCurrentScene()
own = cont.owner

def recalculateRotation(obj,deg):
    rec = obj.localOrientation.to_euler()
    rec[1] = math.radians(deg)
    obj.localOrientation = rec.to_matrix()    
    
def rescaleObject(desc,frame):
    frameScale = desc.localScale[0] * (len(desc['Text']) / 9)
    frame.localScale[0] = frameScale 
    
def repositionObjects(desc,frame,posXYZ):
    frame.localPosition = posXYZ    
    desc.localPosition = [posXYZ[0]+2, posXYZ[1]*0.6, posXYZ[2]-0.1]   
    
desc = sc.objects['Description2']
bubble = sc.objects['Bubble2']
msgNo = desc['msgProp']

if msgNo == 1:
    repositionObjects(desc,bubble,[-3, 1.9, 2.0])
    rescaleObject(desc,bubble)
    recalculateRotation(bubble,0)
    
# TODO - Jos sadrzaja