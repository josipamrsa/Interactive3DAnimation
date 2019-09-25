import bge, bgl # Game engine i logika
import blf      # Upravljanje fontovima
import math     # Matematicke operacije

# Kontrolerske varijable
cont = bge.logic.getCurrentController() # Aktivni kontroler
sc = bge.logic.getCurrentScene()        # Aktivna scena
own = cont.owner                        # Vlasnik

# Rekalkulacija rotacije, translacije i skaliranja 
# opisa/obavijesti u sceni

def recalculateRotation(obj,deg):
    rec = obj.localOrientation.to_euler()
    rec[1] = math.radians(deg)
    obj.localOrientation = rec.to_matrix()    
    
def rescaleObject(desc,frame):
    frameScale = desc.localScale[0] * (len(desc['Text']) / 6.5)
    frame.localScale[0] = frameScale 
    
def repositionObjects(desc,frame,posXYZ):
    frame.localPosition = posXYZ    
    desc.localPosition = [posXYZ[0]+2, posXYZ[1]*0.8, posXYZ[2]-0.1]   
    
# Objekti aktivne scene
desc = sc.objects['Description']
bubble = sc.objects['BubbleText']
msgNo = desc['msgProp']

# Broj poruke oznacava interaktivni objekt na sceni
if msgNo == 0:
    repositionObjects(desc,bubble,[-3, 3.9, 2.0])
    rescaleObject(desc,bubble)
    recalculateRotation(bubble,0)
    
elif msgNo == 1:    
    repositionObjects(desc,bubble,[-3, 2.9, 2.0])
    rescaleObject(desc,bubble)
    recalculateRotation(bubble,0)
    
elif msgNo == 2:    
    repositionObjects(desc,bubble,[-3, 1.0, 2.0])
    rescaleObject(desc,bubble)
    recalculateRotation(bubble,0)
    
elif msgNo == 3:    
    repositionObjects(desc,bubble,[-3, 0.2, 2.0])
    rescaleObject(desc,bubble)
    recalculateRotation(bubble,0)
    
# TODO - adaptirati skriptu za sve scene