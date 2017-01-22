#!/usr/bin/python3
# Hauptprogramm des Projektes Drive
from DriveSense import DriveSense

ds = DriveSense()
ds.SageHallo()

ds.Set_TxtSpeed(1)
#ds.ShowWelcomeMsg()

ds.ShowCountdown()