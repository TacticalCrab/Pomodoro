from lib.Timer import Timer
from time import sleep
from os import system


class Option:
    def __init__(self, name, handler):
        self.name = name
        self.handler = handler

class TerminalInput:
    INPUT_CHAR = ">"

    @staticmethod
    def get_int(text: str, default = None):
        default_text = f" (default: {default})" if default is not None else ""

        while True:
            value = input(f"{text}{default_text}{TerminalInput.INPUT_CHAR} ")
            if len(value) == 0:
                return default

            try:
                return int(value)
            except ValueError:
                pass

    @staticmethod
    def get_range(text: str, start: int, end: int, default = None):
        start_end_text = f"({start} - {end})" if end - start > 0 else ""
        space = " " if text and start_end_text else ""
        print(f"{text}{space}{start_end_text}", end="")

        while True:
            value = input(f"{TerminalInput.INPUT_CHAR} ")
            if len(value) == 0:
                return default

            try:
                integer = int(value)
            except ValueError:
                continue

            if integer < start or integer > end:
                print("Number not in range. Try again.")
                continue

            return integer


class TerminalUI:
    timer = Timer()
    options: list[Option] = []

    def __init__(self):
        self.register_option("Set timer time", self.handler_set_time)
        self.register_option("Start timer", self.handler_start_timer)
        self.timer.set_time(
            minutes=25
        )

    def clear_screen(self):
        system("cls")

    def handler_set_time(self):
        print("Setup your timer:")
        minutes = TerminalInput.get_int("Minutes", 0)
        seconds = TerminalInput.get_int("Seconds", 0)
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
                self.clear_screen()
                print(self.get_timer_str())
                sleep(0.5)
        except KeyboardInterrupt:
            print("Timer stopped")
            sleep(1)
            self.timer.reset()

    def register_option(self, name, handler):
        self.options.append(Option(name, handler))

    def handle_pick_option(self):
        pick = TerminalInput.get_range("Choice", 1, len(self.options), 1) - 1
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
            self.clear_screen()
            print("Current timer:", self.get_timer_str(), "\n")
            self.show_options()
            print()
            self.handle_pick_option()