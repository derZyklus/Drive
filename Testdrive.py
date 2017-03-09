import time
import os
import math
from sense_hat import SenseHat, ACTION_RELEASED


#Ausgabefunktion für Balkendiagramm eines Kriteriums

def show_bar_graph(output, line):
    #Farbauswahl nach Wert
    if output > 4:
        colour = [0, 255, 0]
    elif output > 2:
        colour = [255, 127, 0]
    elif output > 0:
        colour = [255, 0 , 0]
    for i in range(0, output):
        sense.set_pixel(i, line, colour)
        sense.set_pixel(i, line+1, colour)
    for i in range(output, 8):
        sense.set_pixel(i, line, [0, 0, 0])
        sense.set_pixel(i, line+1, [0, 0, 0])
    for i in range(0, 8):
        sense.set_pixel(i, 2, [0, 0, 0])
        sense.set_pixel(i, 5, [0, 0, 0])

#Quantisierung des Beschleunigungswertes auf die LEDs
def quant(Value):
    if Value < 0.1:
        return 0
    elif Value < 0.2:
        return 1
    elif Value < 0.3:
        return 2
    elif Value < 0.4:
        return 3
    elif Value < 0.5:
        return 4
    elif Value < 0.6:
        return 5
    elif Value < 0.7:
        return 6
    elif Value < 0.8:
        return 7
    else:
        return 8

#Definitionen
FileRev = 0
path = "/home/shares/pi//Messwerte/Messwerte_"+str(FileRev)+".csv"
sense = SenseHat()
tempstring = ""
FILTER = 5
i = 0
j = 1
k = 0
record = False
#LED-Zeile fuer Beschleunigung
Line_Acc = 0
#LED-Zeile fuer Bremsung
Line_Brake = 3
#LED-Zeile für Kurvengeschwindigkeit
Line_Curve = 6
#Ausrichtung SenseHat (montiert)
sense.set_rotation(270)
sense.clear()
#Gedimmte Ausgabe
#sense.low_light = True
#Volle Helligkeit
sense.low_light = False

#Array zur Mittelwertbildung aufbauen
a_x = [0]   
a_y = [0]
for k in range(0,FILTER):    
    a_x.append(0)
    a_y.append(0)


sense.show_message("Bereit", scroll_speed=0.05, text_colour=[255, 255, 255])

while True:
    raw = sense.get_accelerometer_raw()
    #x = float("{x}".format(**raw))
    Curve = float("{y}".format(**raw)) 
    Acc = float("{z}".format(**raw))

    Curve = round(Curve, 2)
    Acc = round(Acc, 2)
    show_bar_graph(quant(abs(Curve)), Line_Curve)
    show_bar_graph(quant(abs(Acc)), Line_Brake)
    if Acc < 0:
        show_bar_graph(quant(abs(Acc)), Line_Acc)
    print(Curve, Acc)

    for event in sense.stick.get_events():
        if event.action == "pressed" and event.direction == "middle":
            if record == False:
                record = True
                sense.show_message("Start", scroll_speed=0.05, text_colour=[255, 255, 255])
                TimeZero = time.time()
                tempstring = tempstring + str(time.time()) +";" + "Acc" + ";" + "Curve" +";\n\r"
                fo = open(path, "a")
                fo.write(tempstring)
                fo.close()
            else:
                record = False
                sense.show_message("Stop", scroll_speed=0.05, text_colour=[255, 255, 255])
        if event.action == "pressed" and event.direction == "left" and record == True:
            tempstring = ""
            FileRev = FileRev + 1
            path = "/home/shares/pi/Messwerte/Messwerte_"+str(FileRev)+".csv"
            tempstring = tempstring + str(time.time()) +";" + "Acc" + ";" + "Curve" +";\n\r"
            fo = open(path, "a")
            fo.write(tempstring)
            fo.close()
            tempstring = ""
            sense.show_message("New File", scroll_speed=0.05, text_colour=[255, 255, 255])
        if event.action == "pressed" and event.direction == "right" and record == False:
            sense.show_message("Shutdown", scroll_speed=0.05, text_colour=[255, 255, 255])
            sense.clear()
            os.system("sudo shutdown -h now")

    if record == True:
        tempstring = tempstring + str(time.time()) +";" + str(Acc) + ";" + str(Curve) +";\r"
        fo = open(path, "a")
        fo.write(tempstring)
        fo.close()
        tempstring = ""
