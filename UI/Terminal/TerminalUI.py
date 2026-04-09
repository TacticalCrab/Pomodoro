from UI.Terminal.common.TerminalUtils import TerminalUtils
from UI.Terminal.views.TimeView import TimeView
from UI.Terminal.components.TerminalShortcuts import TerminalShortcuts
from lib.Timer import Timer

class TerminalUI:
    timer: Timer
    shortcuts: TerminalShortcuts

    def __init__(self):
        self.timer = Timer()
        self.shortcuts = TerminalShortcuts()

        self.shortcuts.add_terminal_shortcut("1", "Set timer time", self.handler_set_time)
        self.shortcuts.add_terminal_shortcut("2", "Start timer", self.handler_start_timer)
        self.shortcuts.add_terminal_shortcut("3", "Exit", self.handler_exit)

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

    def run(self):
        while True:
            TerminalUtils.clear_screen()
            print("Current timer:", self.timer, "\n")
            print(self.shortcuts.render_list())
            self.shortcuts.listen_once()
