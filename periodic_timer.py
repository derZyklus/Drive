from threading import Timer,Thread,Event

class PeriodicTimer():

    def __init__(self,t):
        """
        Konstruktor der Klasse.
        1. Parameter: Update-Intervall in Sekunden
        """
        self.t = t
        self.ticks = 0
        self.ready = True
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.ticks += 5
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def get_ticks(self):
        return self.ticks

    def start(self):
        """
         Startet die zyklische Ausführung.
        """
        self.thread.start()

    def cancel(self):
        self.thread.cancel()

    def reset(self):
        self.ticks = 0