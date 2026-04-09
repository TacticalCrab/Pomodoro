from lib.Timer import Timer

from UI.Terminal.common.TerminalUtils import TerminalUtils

class SetupTimerView:
    timer: Timer

    def __init__(self, timer: Timer):
        self.timer = timer
    
    def display_view(self):
        print("Setup your timer:")
        minutes = TerminalUtils.get_int("Minutes", 0)
        seconds = TerminalUtils.get_int("Seconds", 0)

        self.timer.set_time(
            minutes=minutes,
            seconds=seconds
        )