from UI.Terminal.common.TerminalUtils import TerminalUtils
from UI.Terminal.views import TimeView, SetupTimerView, SelectSessionView
from UI.Terminal.components import Timer
from UI.Terminal.views.ViewBase import ViewBase

class TerminalUI(ViewBase):
    timer: Timer

    def __init__(self):
        super().__init__()
        self.timer = Timer()

        self.shortcuts.add_terminal_shortcut("1", "Set timer time", self.handler_set_time)
        self.shortcuts.add_terminal_shortcut("2", "Start timer", self.handler_start_timer)
        self.shortcuts.add_terminal_shortcut("3", "Sessions", self.handler_sessions)
        self.shortcuts.add_terminal_shortcut("4", "Exit", self.handler_exit)

        self.timer.set_time(minutes=25)

    def handler_set_time(self):
        self.terminalUtils.clear_screen()
        view = SetupTimerView(self.timer)
        view.display_view()

    def handler_start_timer(self):
        self.terminalUtils.clear_screen()
        view = TimeView(self.timer)
        view.display_view()
        self.timer.reset()
    
    def handler_sessions(self):
        self.terminalUtils.clear_screen()
        view = SelectSessionView()
        view.display_view()

    def handler_exit(self):
        exit(0)

    def display_view(self):
        while True:
            self.terminalUtils.clear_screen()
            print(self.timer.render(), "\n")
            print(self.shortcuts.render_list())
            self.shortcuts.listen_once()
