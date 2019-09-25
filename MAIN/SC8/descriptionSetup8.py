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
    frameScale = desc.localScale[0] * (len(desc['Text']) / 7)
    frame.localScale[0] = frameScale 
    
def repositionObjects(desc,frame,posXYZ):
    frame.localPosition = posXYZ    
    desc.localPosition = [posXYZ[0], posXYZ[1]*0.3, posXYZ[2]-0.8]   
    
# Objekti aktivne scene
desc = sc.objects['Description4']
bubble = sc.objects['Bubble4']
msgNo = desc['msgProp']

# Broj poruke oznacava interaktivni objekt na sceni
if msgNo == 0:  
    repositionObjects(desc,bubble,[-1, 1.5, 3.0])
    rescaleObject(desc,bubble)
    recalculateRotation(bubble,0)
    
elif msgNo == 1:    
    repositionObjects(desc,bubble,[-1, 1.5, 3.0])
    rescaleObject(desc,bubble)
    recalculateRotation(bubble,0)
       
# TODO - adaptirati skriptu za sve scene