# Pythonklasse
__author__ = "Stephan Psenner, Hendrik Schulz, Hannes Grefe und Ingo Fiedler"
__copyright__ = "Copyright 2017, The Drive Project"
__credits__ = ["Stephan Psenner", "Hendrik Schulz", "Hannes Grefe",
               "Ingo Fiedler"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Ingo Fiedler"
__email__ = "xxx"
__status__ = "Development"

# Import der benötigten Module
from sense_hat import SenseHat
import time
import math
import os
import sys

class DriveSense:

    def __init__(self):
        """ Initialisierung der Klasse """
        self.sense = SenseHat()
        self.KONST = 9.81
        self.txtSpeed = 0.15 # Geschwindigkeit der Textausgabe über die 8x8-LEDs

    def Set_TxtSpeed(self, speed=.15):
        """ Setzt die Geschwindigkeit der Textausgabe auf einen neuen Wert """
        self.txtSpeed = speed
        
    def ShowWelcomeMsg(self):
        """ Gibt die Startnachticht aus """
        self.sense.show_message("Drive " + __version__ )

    def ShowCountdown(self):
        """ Fuert einen Countdown durch und zaehlt von 10 runter """
        for i in reversed(range(0, 10)):
            self.sense.show_letter(str(i))
            time.sleep(1)
        self.sense.clear()

    def show_arrow(self, fg, bg):
        """
        Gibt den Pfeil für die Richtungsangabe aus
        :param fg: Farbe des Vordergrundes (Pfeil)
        :param bg: Hintergrundfarbe
        """
        arrow = [
            bg, bg, bg, fg, bg, bg, bg, bg,
            bg, bg, fg, bg, bg, bg, bg, bg,
            bg, fg, bg, bg, bg, bg, bg, bg,
            fg, fg, fg, bg, bg, bg, bg, bg,
            fg, fg, fg, bg, bg, bg, bg, bg,
            bg, fg, bg, bg, bg, bg, bg, bg,
            bg, bg, fg, bg, bg, bg, bg, bg,
            bg, bg, bg, fg, bg, bg, bg, bg
        ]
        self.sense.set_pixels(arrow)
    
    def WaitForButton(self):
        for event in self.sense.stick.get_events():
            if event.action == "pressed" and event.direction == "middle" :
                return True
        return False

    def get_z_value(self):
        #pitch = self.sense.gyroscope['pitch'] - 270 # in Grad
        #pitch = self.sense.get_orientation_degrees()
        #pitch = pitch * 3.141592654 / 180
        return self.sense.accelerometer_raw['z']

    def check_temperature(self, limit):
        """ ttt """
        if self.sense.get_temperature() < limit:
            return
        self.sense.show_message("Hot! Bye", scroll_speed=0.05, text_colour=[255, 0, 0])
        self.sense.clear()
        os.system("sudo shutdown -h now")
        sys.exit()

if __name__ == "__main__":
    x = DriveSense()
