from ..ViewBase import ViewBase
from lib.Session.Session import Session
from UI.Terminal.components.Timer import Timer
from time import sleep
from datetime import datetime

class SessionView(ViewBase):
    session: Session
    timer: Timer
    _active_view: bool

    def __init__(self, session: Session):
        super().__init__()
        self.session = session
        self.timer = Timer()
        self._active_view = True

    def _exit(self):
        self._active_view = False
        self.shortcuts.clear()
        self.shortcuts.stop_thread()

    def print_session(self):
        for session_time in self.session:
            minutes, seconds = divmod(session_time.time.seconds, 60)
            print(f"{session_time.type} - {minutes:02}:{seconds:02}")

    def display_session_menu(self):
        start = None
        def _start():
            nonlocal start
            start = True

        def _exit():
            nonlocal start
            start = False

        self.shortcuts.add_terminal_shortcut("s", "Start", lambda: _start())
        self.shortcuts.add_terminal_shortcut("x", "Exit", lambda: _exit())

        print(f"Session {self.session.name}")
        self.print_session()
        print()
        print(self.shortcuts.render_list())
        while start is None:
            self.shortcuts.listen_once()

        return start

    def display_view(self):
        if not self.display_session_menu():
            self._exit()
            return

        self.shortcuts.clear()

        self.shortcuts.add_terminal_shortcut("s", "start", lambda: self.timer.start())
        self.shortcuts.add_terminal_shortcut("h", "stop timer", lambda: self.timer.stop())
        self.shortcuts.add_terminal_shortcut("r", "resume timer", lambda: self.timer.resume())
        self.shortcuts.add_terminal_shortcut("x", "exit", lambda: self._exit())
        self.shortcuts.listen_thread()

        session_iter = iter(self.session)
        while self._active_view:
            try:
                session_time = next(session_iter)
            except StopIteration:
                self.terminalUtils.clear_screen()
                self.terminalUtils.ascii_print("End of session")
                sleep(1)
                break

            self.timer.reset()
            self.timer.set_time(seconds=session_time.time.total_seconds())
            self.terminalUtils.clear_screen()

            while self.timer.get_seconds_left() > 0 and self._active_view:
                self.terminalUtils.clear_screen()
                self.terminalUtils.ascii_print(session_time.type)
                print(self.timer.render())
                print(self.shortcuts.render_inline())
                sleep(0.4)

