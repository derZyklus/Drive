#!/usr/bin/python3
# Hauptprogramm des Projektes Drive
from DriveSense import DriveSense
from time import sleep
import time
from periodic_timer import PeriodicTimer
from numpy import *

# Definition der LED-Farben
Re = [255, 0, 0]  # Red
Gr = [0, 255, 0]  # Green
Bl = [0, 0, 255]  # Blue
Wh = [255, 255, 255]  # White
Bk = [0, 0, 0]  # Black (BkFF)

ds = DriveSense()

ds.Set_TxtSpeed(1)
ds.sense.low_light = True
ds.sense.set_rotation(270)

# Startmeldung ausgeben und Pfeil für die korrekte Einbaulage anzeigen
#ds.ShowWelcomeMsg()
ds.show_arrow(Re, Bk)

# Warten bis Benutzer bereit ist und Button gedrückt hat
#while ds.WaitForButton() == False:
#    sleep(0.1)

# Countdown durchführen und dann starten...
#ds.ShowCountdown()

pt = PeriodicTimer(0.005)
pt.start()
#           1  2  3  4  5  6  7  8  9 10
#dataList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dataList = zeros(5)
index = 0
oIndex = 0

# Hier der Main-Task
xx = True
while xx:
    # Alle 20ms ausführen
    if (pt.ticks % 20) == 0:
        dataList[index] = ds.get_z_value()
        index += 1
        if index >= 5:
            index = 0


    # Alle 100ms ausführen
    if pt.ticks % 100 == 0:
        wert = 0.0
        for x in range(0, 4, 1):
            wert += dataList[x]
        wert = wert / 5
        #print("Orginal Wert: {0}".format(wert))

    # Alle 500 ms ausführen
    if (pt.ticks % 500) == 0:
        test = 0
        #orientation = ds.sense.get_orientation_degrees()
        #print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
        #raw = ds.sense.get_accelerometer_raw()
        #print("x: {x}, y: {y}, z: {z}".format(**raw))
        #print("Orginal Wert: {0}".format(ds.get_z_value()))


    # Alle 1s ausführen
    if pt.ticks >= 1000:
        pt.reset() # Zähler für die Ticks wieder auf 0 setzen
        #print("Temp: {0}".format(ds.sense.get_temperature()))
        ds.check_temperature(32)

    # Hier eventuell Berechnen wie lange die einzelnen Tasks dauern
    #time.sleep(0.005)
