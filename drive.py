#!/usr/bin/python3
# Hauptprogramm des Projektes Drive
from DriveSense import DriveSense
from time import sleep
import time
from periodic_timer import PeriodicTimer

ds = DriveSense()

ds.Set_TxtSpeed(1)

# Startmeldung ausgeben und Pfeil für die korrekte Einbaulage anzeigen
#ds.ShowWelcomeMsg()

# Warten bis Benutzer bereit ist und Button gedrückt hat
#while ds.WaitForButton() == False:
#    sleep(0.1)

# Countdown durchführen und dann starten...
#ds.ShowCountdown()


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
