from time import sleep

from UI.Terminal.TerminalUtils import TerminalUtils
from UI.Terminal.views.TimeView import TimeView
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
        self.register_option("Exit", self.handler_exit)

        self.timer.set_time(minutes=25)

    def handler_set_time(self):
        print("Setup your timer:")
        minutes = TerminalUtils.get_int("Minutes", 0)
        seconds = TerminalUtils.get_int("Seconds", 0)
        self.timer.set_time(
            minutes=minutes,
            seconds=seconds
        )

    def handler_start_timer(self):
        TerminalUtils.clear_screen()
        view = TimeView(self.timer)
        view.display_view()
        self.timer.reset()

    def handler_exit(self):
        exit(0)

    def register_option(self, name, handler):
        self.options.append(Option(name, handler))

    def handle_pick_option(self):
        pick = TerminalUtils.get_range("Choice", 1, len(self.options), 1) - 1
        self.options[pick].handler()

    def show_options(self):
        for i, option in enumerate(self.options, start = 1):
            print(f"{i}. {option.name}")

    def run(self):
        while True:
            TerminalUtils.clear_screen()
            print("Current timer:", self.timer, "\n")
            self.show_options()
            print()
            self.handle_pick_option()