from lib.Timer import Timer
from UI.Terminal.TerminalUtils import TerminalUtils
from UI.Terminal.TerminalKeyboard import TerminalKeyboard

from time import sleep

class TimeView:
    keyboard: TerminalKeyboard = TerminalKeyboard()
    timer: Timer
    _view_active = True

    def __init__(self, timer):
        self.timer = timer

    def __del__(self):
        self._clean_up()

    def _exit(self):
        self._view_active = False
        self._clean_up()

    def _clean_up(self):
        self.keyboard.clear_events()
        self.keyboard.stop_thread()

    def _start_timer(self):
        if not self.timer.time:
            print("Time in timer is not set!")
            sleep(2)
            return

        self.timer.start()

        while self._view_active:
            TerminalUtils.clear_screen()
            print(f"[{self.timer}]")
            self._print_key_events()
            sleep(0.4)

    def _print_key_events(self):
        key_events = [
            ["s", "Stop Timer"],
            ["r", "Resume Timer"],
            ["x", "Exit"]
        ]

        key_events_str = ""
        for [key, name] in key_events:
            key_events_str += f"[{key}] {name}  "

        print("")
        print(key_events_str)

    def _setup_keyboard_events(self):
        self.keyboard.register_key_event("s", lambda: self.timer.stop())
        self.keyboard.register_key_event("r", lambda: self.timer.resume())
        self.keyboard.register_key_event("x", lambda: self._exit())

    def display_view(self):
        self._setup_keyboard_events()
        self.keyboard.start_thread()
        self._start_timer()
