#!/usr/bin/python3
# Hauptprogramm des Projektes Drive
from DriveSense import DriveSense
from sense_hat import ACTION_PRESSED, ACTION_RELEASED
from time import sleep
import csv
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
#ds.ShowWelcomeMsg()
ds.show_arrow(Re, Bk)

# Warten bis Benutzer bereit ist und Button gedrückt hat
#while ds.WaitForButton() == False:
#    sleep(0.1)

# Countdown durchführen und dann starten...
#ds.ShowCountdown()

#pt = PeriodicTimer(0.005)
#pt.start()
#           1  2  3  4  5  6  7  8  9 10
#dataList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#dataList = zeros(5)
index = 0
oIndex = 0

test_counter = 0
ds.sense.clear()
# Hier der Main-Task
xx = True
t_schwelle = 0 # Ein kleiner Timer für die 0,05g Schwelle
z_count = 0
z_mean_value = 0
n_shutdown = 0
is_pressed = False

fileObj = open('Test_Data.csv')
csvReader = csv.reader(fileObj)

calc_Acc.show_bar_graph(calc_Acc.anzeige, Line_Acc)
calc_Brake.show_bar_graph(calc_Brake.anzeige, Line_Brake)
calc_Curve.show_bar_graph(calc_Curve.anzeige, Line_Curve)

for row in csvReader:
    #print("Wert3: {0}".format(row[3]))
    #print("Wert2: {0}".format(row[2]))
    zvalue = float(row[3])
    if zvalue > 0:
        calc_Acc.add_value(zvalue)
    else:
        calc_Brake.add_value(abs(zvalue))
    calc_Curve.add_value(abs(float(row[2])))
    sleep(0.02)
    # Alle 100ms ausführen
    if test_counter == 4:
        calc_Acc.calc_MeanValue()
        calc_Acc.calc_Result()
        print("Acc {0}:".format(calc_Acc.get_MeanValue()))
        calc_Brake.calc_MeanValue()
        calc_Brake.calc_Result()
        calc_Curve.calc_MeanValue()
        calc_Curve.calc_Result()
        print("Curve {0}:".format(calc_Curve.get_MeanValue()))

    test_counter += 1
    if test_counter >= 5:
        test_counter = 0

fileObj.close()