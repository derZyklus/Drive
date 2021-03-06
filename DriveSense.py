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
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED
import time
import math
import os
import sys

class DriveSense:

    def __init__(self):
        """ Initialisierung der Klasse """
        self.sense = SenseHat()
        #self.sense.set_rotation(270)
        self.KONST = 9.81
        self.txtSpeed = 0.15 # Geschwindigkeit der Textausgabe über die 8x8-LEDs

    def Set_TxtSpeed(self, speed=.15):
        """ Setzt die Geschwindigkeit der Textausgabe auf einen neuen Wert """
        self.txtSpeed = speed
        
    def ShowWelcomeMsg(self):
        """ Gibt die Startnachticht aus """
        #self.sense.show_message("Drive " + __version__ )
        self.sense.show_message("Drive")

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

    def get_y_value(self):
        return self.sense.accelerometer_raw['y']

    def check_temperature(self, limit):
        """ ttt """
        if self.sense.get_temperature() > limit:
            self.sense.show_message("Hot! Bye", scroll_speed=0.05, text_colour=[255, 0, 0])
            self.sense.clear()
            os.system("sudo shutdown -h now")
            sys.exit()

    def shutdown(self):
        Symbol = [
        [255, 0, 0], [255, 0, 0], [255, 87, 0], [255, 196, 0], [205, 255, 0], [95, 255, 0], [0, 255, 13], [0, 255, 122],
        [255, 0, 0], [255, 96, 0], [255, 205, 0], [196, 255, 0], [87, 255, 0], [0, 255, 22], [0, 255, 131], [0, 255, 240],
        [255, 105, 0], [255, 214, 0], [187, 255, 0], [78, 255, 0], [0, 255, 30], [0, 255, 140], [0, 255, 248], [0, 152, 255],
        [255, 223, 0], [178, 255, 0], [70, 255, 0], [0, 255, 40], [0, 255, 148], [0, 253, 255], [0, 144, 255], [0, 34, 255],
        [170, 255, 0], [61, 255, 0], [0, 255, 48], [0, 255, 157], [0, 243, 255], [0, 134, 255], [0, 26, 255], [83, 0, 255],
        [52, 255, 0], [0, 255, 57], [0, 255, 166], [0, 235, 255], [0, 126, 255], [0, 17, 255], [92, 0, 255], [201, 0, 255],
        [0, 255, 66], [0, 255, 174], [0, 226, 255], [0, 117, 255], [0, 8, 255], [100, 0, 255], [210, 0, 255], [255, 0, 192],
        [0, 255, 183], [0, 217, 255], [0, 109, 255], [0, 0, 255], [110, 0, 255], [218, 0, 255], [255, 0, 183], [255, 0, 74]
        ]
        self.sense.set_pixels(Symbol)
        time.sleep(2)
        self.sense.clear()
        time.sleep(0.02)
        os.system("sudo shutdown -h now")
        sys.exit()

if __name__ == "__main__":
    x = DriveSense()
