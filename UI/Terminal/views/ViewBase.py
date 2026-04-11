from abc import ABC, abstractmethod
from UI.Terminal.common.TerminalKeyboard import TerminalKeyboard
from UI.Terminal.components.TerminalShortcuts import TerminalShortcuts
from UI.Terminal.common.TerminalUtils import TerminalUtils

class ViewBase(ABC):
    keyboard: TerminalKeyboard
    shortcuts: TerminalShortcuts
    terminalUtils = TerminalUtils

    def __init__(self):
        self.keyboard = TerminalKeyboard()
        self.shortcuts = TerminalShortcuts()

    @abstractmethod
    def display_view(self):
        pass