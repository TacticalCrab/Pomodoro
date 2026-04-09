from UI.Terminal.common.TerminalUtils import TerminalUtils
from UI.Terminal.common.TerminalKeyboard import TerminalKeyboard
from UI.Terminal.components import TerminalShortcuts, Timer

from time import sleep

class TimeView:
    _view_active: bool
    shortcuts: TerminalShortcuts
    keyboard: TerminalKeyboard
    timer: Timer

    def __init__(self, timer):
        self.shortcuts = TerminalShortcuts()
        self.keyboard = TerminalKeyboard()
        self.timer = timer
        self._view_active = True

    def __del__(self):
        self._clean_up()

    def _exit(self):
        self._view_active = False
        self._clean_up()

    def _clean_up(self):
        self.shortcuts.stop_thread()

    def _start_timer(self):
        if not self.timer.time:
            print("Time in timer is not set!")
            sleep(2)
            return

        self.timer.start()

        while self._view_active:
            TerminalUtils.clear_screen()
            stopped_text = "stopped" if self.timer.is_stopped else ""

            print(self.timer.render())
            print(stopped_text)
            print("")
            print(self.shortcuts.render_inline())
            sleep(0.4)

    def _setup_keyboard_events(self):
        self.shortcuts.add_terminal_shortcut("s", "stop timer", lambda: self.timer.stop())
        self.shortcuts.add_terminal_shortcut("h", "start / resume timer", lambda: self.timer.resume())
        self.shortcuts.add_terminal_shortcut("r", "reset timer", lambda: self.timer.reset())
        self.shortcuts.add_terminal_shortcut("x", "exit", lambda: self._exit())

    def display_view(self):
        self._setup_keyboard_events()
        self.shortcuts.listen_thread()
        self._start_timer()
