#!/usr/bin/python3
# Hauptprogramm des Projektes Drive
from DriveSense import DriveSense
from sense_hat import ACTION_PRESSED, ACTION_RELEASED
from time import sleep
import time
from periodic_timer import PeriodicTimer
from drive_algo import DriveAlgo

# Definition der LED-Farben
Re = [255, 0, 0]  # Red
Gr = [0, 255, 0]  # Green
Bl = [0, 0, 255]  # Blue
Wh = [255, 255, 255]  # White
Bk = [0, 0, 0]  # Black (BkFF)

#LED-Zeile fuer Beschleunigung
Line_Acc = 0
#LED-Zeile fuer Bremsung
Line_Brake = 3
#LED-Zeile für Kurvengeschwindigkeit
Line_Curve = 6

ds = DriveSense()
calc_Acc = DriveAlgo(5, Line_Acc)
calc_Brake = DriveAlgo(5, Line_Brake)
calc_Curve = DriveAlgo(5, Line_Curve)

ds.Set_TxtSpeed(1)
ds.sense.low_light = True
ds.sense.set_rotation(270)

# Startmeldung ausgeben und Pfeil für die korrekte Einbaulage anzeigen
ds.ShowWelcomeMsg()
ds.show_arrow(Re, Bk)

# Warten bis Benutzer bereit ist und Button gedrückt hat
while ds.WaitForButton() == False:
    sleep(0.1)
ds.sense.clear()

# Countdown durchführen und dann starten...
#ds.ShowCountdown()

pt = PeriodicTimer(0.005)
pt.start()
#           1  2  3  4  5  6  7  8  9 10
#dataList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#dataList = zeros(5)
index = 0
oIndex = 0

# Hier der Main-Task
xx = True
t_schwelle = 0 # Ein kleiner Timer für die 0,05g Schwelle
z_count = 0
z_mean_value = 0
n_shutdown = 0
is_pressed = False

# Bar-Graph auf Ausgangswerte setzen
calc_Acc.show_bar_graph(calc_Acc.anzeige, Line_Acc)
calc_Brake.show_bar_graph(calc_Brake.anzeige, Line_Brake)
calc_Curve.show_bar_graph(calc_Curve.anzeige, Line_Curve)

while xx:
    # Alle 20ms ausführen
    if (pt.ticks % 20) == 0:
        zvalue = ds.get_z_value()
        if zvalue > 0:
            calc_Acc.add_value(zvalue)
        else:
            calc_Brake.add_value(abs(zvalue))
        calc_Curve.add_value(abs(ds.get_y_value()))

    # Alle 100ms ausführen
    if pt.ticks % 100 == 0:
        calc_Acc.calc_MeanValue()
        calc_Acc.calc_Result()
        calc_Brake.calc_MeanValue()
        calc_Brake.calc_Result()
        calc_Curve.calc_MeanValue()
        calc_Curve.calc_Result()
        #print("Brake: {0}".format(calc_Brake.get_MeanValue()))
        #print("Curve: {0}".format(calc_Curve.get_MeanValue()))
        #print("Orginal Wert: {0}".format(wert))

    # Alle 500 ms ausführen
    if (pt.ticks % 500) == 0:
        for event in ds.sense.stick.get_events():
            if event.action == 'pressed':
                is_pressed = True
            elif event.action == 'released':
                is_pressed = False
        if is_pressed:
            n_shutdown += 1
        else:
            n_shutdown = 0
        #print("Wert {0}".format(n_shutdown))
        if n_shutdown >= 2:
            ds.shutdown()

    # Alle 1s ausführen
    if pt.ticks >= 1000:
        pt.reset() # Zähler für die Ticks wieder auf 0 setzen
        #ds.check_temperature(65)

    # Hier eventuell Berechnen wie lange die einzelnen Tasks dauern
    #time.sleep(0.005)
