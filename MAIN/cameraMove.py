# LOKALNE KOORDINATE I SVJETSKE KOORDINATE

# Lokalne (Local (Position/Orientation/Scale)
# Staticne koordinate (kod lika koji se kreće ostaju iste)

# Svjetske/globalne (World)
# Koordinate koje se mijenjaju s kretanjem lika 

import bge
import bpy
import math

# BGE
cont = bge.logic.getCurrentController()
sc = bge.logic.getCurrentScene()
own = cont.owner

# Objekt kamere
camNum = "CamScene" + str(own["camNo"])
cam = sc.objects[camNum]

# Okretaj - stupnjevi
degreeTurn = 0 
# Lista mogućih okretaja
# Cuva izometrijski poredak
degreeView = [45, 135, 225, 315] 
# Trenutna pozicija kamere 
camPosition = [10.0000, -9.7000, 9.2814]


# Za aktivan senzor desne strelice kamera se kreće
# u suprotnom smjeru od kazaljke sata
# Varijabla camView kamere prati u kojem je trenutno
# smjeru okrenuta kamera
# Ovisno o toj varijabli mijenjamo z-kut pogleda i 
# poziciju kamere na x-osi i y-osi (pozitivno/negativno)

if cont.sensors["RightArr"].positive:
    if cam['camView'] == 0:
        degreeTurn = degreeView[1]
        cam['camView'] = 1
        camPosition = [10.0000, 9.7000, 9.2814]
    
    elif cam['camView'] == 1:
        degreeTurn = degreeView[2]
        cam['camView'] = 2
        camPosition = [-10.0000, 9.7000, 9.2814]

    elif cam['camView'] == 2:
        degreeTurn = degreeView[3]
        cam['camView'] = 3
        camPosition = [-10.0000, -9.7000, 9.2814]
    
    elif cam['camView'] == 3:
        degreeTurn = degreeView[0]
        cam['camView'] = 0   
        camPosition = [10.0000, -9.7000, 9.2814]

    # Radimo transformacije i rotacije kamere
    # Dohvatimo orijentaciju kamere i pretvorimo
    # matricu u Eulerove xyz mjere
    # Uzimamo Eulerovu orijentaciju i z-osi dodamo
    # kut pretvoren u radijane
    # Konacno mijenjamo orijentaciju (uz obaveznu 
    # pretvorbu u matricu) i poziciju kamere
    
    camOrientation = cam.localOrientation.to_euler()
    camOrientation[2] = math.radians(degreeTurn)
    cam.localOrientation = camOrientation.to_matrix()   
    cam.localPosition = camPosition

# Za aktivan senzor desne strelice kamera se kreće
# u istom smjeru kao i kazaljka sata

if cont.sensors["LeftArr"].positive:
    if cam['camView'] == 1:
        degreeTurn = degreeView[0]
        cam['camView'] = 0
        camPosition = [10.0000, -9.7000, 9.2814]
    
    elif cam['camView'] == 2:
        degreeTurn = degreeView[1]
        cam['camView'] = 1
        camPosition = [10.0000, 9.7000, 9.2814]

    elif cam['camView'] == 3:
        degreeTurn = degreeView[2]
        cam['camView'] = 2
        camPosition = [-10.0000, 9.7000, 9.2814]
    
    elif cam['camView'] == 0:
        degreeTurn = degreeView[3]
        cam['camView'] = 3   
        camPosition = [-10.0000, -9.7000, 9.2814]

    camOrientation = cam.localOrientation.to_euler()
    camOrientation[2] = math.radians(degreeTurn)
    cam.localOrientation = camOrientation.to_matrix()   
    cam.localPosition = camPosition
