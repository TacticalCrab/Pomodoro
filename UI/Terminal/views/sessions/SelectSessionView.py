from lib.Session.SessionManager import SessionManager
from ..ViewBase import ViewBase
from .SessionView import SessionView


class SelectSessionView(ViewBase):
    sessionManager: SessionManager
    _active_view: bool

    def __init__(self):
        super().__init__()
        self.sessionManager = SessionManager("./data/sessions")
        self._active_view = True
    
    def _exit(self):
        self._active_view = False

    def handle_session_view(self, session_file):
        session = self.sessionManager.resolve_session_file(session_file)
        self.terminalUtils.clear_screen()

        view = SessionView(session)
        view.display_view()

    def display_view(self):
        session_files = self.sessionManager.get_session_files()
        for key, session_file in enumerate(session_files, start=1):
            self.shortcuts.add_terminal_shortcut(
                str(key), 
                session_file.name, 
                lambda f=session_file: self.handle_session_view(f)
            )

        self.shortcuts.add_terminal_shortcut("x", "Exit", lambda: self._exit())

        while self._active_view:
            self.terminalUtils.clear_screen()
            print("Session Manager")
            print(self.shortcuts.render_list())
            self.shortcuts.listen_once()

        self.shortcuts.clear()
