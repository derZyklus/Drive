#!/usr/bin/python3
# Hauptprogramm des Projektes Drive
from DriveSense import DriveSense
from time import sleep
import time
from periodic_timer import PeriodicTimer

# Definition der LED-Farben
Re = [255, 0, 0]  # Red
Gr = [0, 255, 0]  # Green
Bl = [0, 0, 255]  # Blue
Wh = [255, 255, 255]  # White
Bk = [0, 0, 0]  # Black (BkFF)


ds = DriveSense()

ds.Set_TxtSpeed(1)

# Startmeldung ausgeben und Pfeil für die korrekte Einbaulage anzeigen
ds.ShowWelcomeMsg()
ds.show_arrow(Re, Bk)

# Warten bis Benutzer bereit ist und Button gedrückt hat
while ds.WaitForButton() == False:
    sleep(0.1)

# Countdown durchführen und dann starten...
ds.ShowCountdown()


pt = PeriodicTimer(0.005)
pt.start()

# Hier der Main-Task
xx = True
while xx:
    # Alle 10ms ausführen
    if (pt.ticks % 10) == 0:
        #print('Task 10ms')
        test = 0

    # Alle 50ms ausführen
    if pt.get_ticks() % 50 == 0:
        print('Task 50ms')

    # Alle 100ms ausführen
    if (pt.ticks % 100) == 0:
        #print('Task 100ms')
        test = 0

    # Alle 1s ausführen
    if pt.ticks >= 1000:
        print('Task 1s')
        pt.reset()

    time.sleep(0.005)
