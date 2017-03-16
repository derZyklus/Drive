from numpy import *
from sense_hat import SenseHat

class DriveAlgo():
    def __init__(self,nMeanValues, line):
        """
        Konstruktor der Klasse.
        1. Parameter: Update-Intervall in Sekunden
        """
        self.nMeanValues = nMeanValues
        self.dataList = zeros(nMeanValues)
        self.listIndex = 0
        self.meanValue = 0.0
        self.resultIndex = 0
        self.resultMeanValue = 0.0
        self.sh = SenseHat()
        self.anzeige = 8
        self.line = line

    def add_value(self,value):
        """ Kommentar """
        self.dataList[self.listIndex] = value
        self.listIndex += 1
        if self.listIndex >= self.nMeanValues:
            self.listIndex = 0

    def calc_MeanValue(self):
        value = 0.0
        for x in range(0, self.nMeanValues-1, 1):
            value += self.dataList[x]
        self.meanValue = value / self.nMeanValues

    def calc_Result(self):
        if self.meanValue > 0.05:
            self.resultIndex += 1
            self.resultMeanValue += self.meanValue
        else:
            if self.resultIndex <= 0:
                return
            self.resultMeanValue = self.resultMeanValue / self.resultIndex
            if not (self.resultMeanValue > 0.1):
                self.anzeige += 2
            elif not (self.resultMeanValue > 0.2):
                self.anzeige += 1
            elif not (self.resultMeanValue > 0.3):
                self.anzeige += 0
            elif not (self.resultMeanValue > 0.4):
                self.anzeige -= 1
            elif not (self.resultMeanValue > 0.5):
                self.anzeige -= 2
            else:
                self.anzeige -= 3
            if self.anzeige > 8:
                self.anzeige = 8
            else:
                if self.anzeige < 0:
                    self.anzeige = 0
            self.show_bar_graph(self.anzeige, self.line)
            self.resultIndex = 0
            self.resultMeanValue = 0.0

    def show_Results(self, value):
        self.sh.show_letter('A')

    def get_MeanValue(self):
        return self.meanValue

    def show_bar_graph(self, output, line):
        self.sh.clear() #
        # Farbauswahl nach Wert
        if output > 4:
            colour = [0, 255, 0]
        elif output > 2:
            colour = [255, 127, 0]
        elif output > 0:
            colour = [255, 0, 0]
        for i in range(0, output):
            self.sh.set_pixel(i, line, colour)
            self.sh.set_pixel(i, line + 1, colour)
        for i in range(output, 8):
            self.sh.set_pixel(i, line, [0, 0, 0])
            self.sh.set_pixel(i, line + 1, [0, 0, 0])
        for i in range(0, 8):
            self.sh.set_pixel(i, 2, [0, 0, 0])
            self.sh.set_pixel(i, 5, [0, 0, 0])

if __name__ == "__main__":
    x = DriveSense()