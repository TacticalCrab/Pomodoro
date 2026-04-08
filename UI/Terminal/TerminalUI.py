from time import sleep

from UI.Terminal.TerminalUtils import TerminalUtils
from lib.Timer import Timer

class Option:
    def __init__(self, name, handler):
        self.name = name
        self.handler = handler

class TerminalUI:
    timer = Timer()
    options: list[Option] = []

    def __init__(self):
        self.register_option("Set timer time", self.handler_set_time)
        self.register_option("Start timer", self.handler_start_timer)
        self.timer.set_time(
            minutes=25
        )

    def handler_set_time(self):
        print("Setup your timer:")
        minutes = TerminalUtils.get_int("Minutes", 0)
        seconds = TerminalUtils.get_int("Seconds", 0)
        self.timer.set_time(
            minutes=minutes,
            seconds=seconds
        )

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

    def register_option(self, name, handler):
        self.options.append(Option(name, handler))

    def handle_pick_option(self):
        pick = TerminalUtils.get_range("Choice", 1, len(self.options), 1) - 1
        self.options[pick].handler()

    def show_options(self):
        for i, option in enumerate(self.options, start = 1):
            print(f"{i}. {option.name}")

    def get_timer_str(self):
        total_seconds_left = self.timer.get_time_left().total_seconds()
        minutes_left, seconds_left = divmod(total_seconds_left, 60)
        return f"{round(minutes_left):02}:{round(seconds_left):02}"

    def run(self):
        while True:
            TerminalUtils.clear_screen()
            print("Current timer:", self.get_timer_str(), "\n")
            self.show_options()
            print()
            self.handle_pick_option()