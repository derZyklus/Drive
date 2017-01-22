# Pythonklasse
__author__ = "Rob Knight, Gavin Huttley, and Peter Maxwell"
__copyright__ = "Copyright 2017, The Drive Project"
__credits__ = ["Rob Knight", "Peter Maxwell", "Gavin Huttley",
                    "Matthew Wakefield"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Ingo Fiedler"
__email__ = "rob@spot.colorado.edu"
__status__ = "Development"

# Import der benötigten Module
from sense_hat import SenseHat
import time

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
        for i in reversed(range(0, 10)):
            self.sense.show_letter(str(i))
            time.sleep(1)
        self.sense.clear()

    def SageHallo(self):
        print("Hallo Ingo {}".format(self.KONST))

if __name__ == "__main__":
    x = DriveSense()
