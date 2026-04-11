from lib.Timer import Timer
from .ViewBase import ViewBase

class SetupTimerView(ViewBase):
    def __init__(self, timer: Timer):
        super().__init__()
        self.timer = timer
    
    def display_view(self):
        print("Setup your timer:")
        minutes = self.terminalUtils.get_int("Minutes", 0)
        seconds = self.terminalUtils.get_int("Seconds", 0)

        self.timer.set_time(
            minutes=minutes,
            seconds=seconds
        )