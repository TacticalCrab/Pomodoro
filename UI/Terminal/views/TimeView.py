from lib.Timer import Timer
from UI.Terminal.TerminalUtils import TerminalUtils

from time import sleep

class TimeView:
    timer: Timer

    def __init__(self, timer):
        self.timer = timer

    def handler_start_timer(self):
        if not self.timer.time:
            print("Time in timer is not set!")
            sleep(2)
            return

        self.timer.start()
        print(self.timer.get_seconds_left(), self.timer.time)
        try:
            while self.timer.get_seconds_left() > 0:
                TerminalUtils.clear_screen()
                print(self.get_timer_str())
                sleep(0.5)
        except KeyboardInterrupt:
            print("Timer stopped")
            sleep(1)
            self.timer.reset()

    def display_view(self):
        print("Hello World")