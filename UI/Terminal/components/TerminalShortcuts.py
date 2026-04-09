from UI.Terminal.common.TerminalKeyboard import TerminalKeyboard

from dataclasses import dataclass
from typing import Any

@dataclass
class Shortcut:
    key: str
    name: str
    handler: Any

class TerminalShortcuts:
    keyboard: TerminalKeyboard
    shortcuts: list[Shortcut]

    def __init__(self):
        self.keyboard = TerminalKeyboard()
        self.shortcuts = []

    def _setup_keyboard_events(self):
        for s in self.shortcuts:
            self.keyboard.register_key_event(s.key, s.handler)
    
    def add_terminal_shortcut(self, key, name, handler):
        shortcut = Shortcut(
            key=key,
            name=name,
            handler=handler
        )
        self.shortcuts.append(shortcut)

        self.keyboard.register_key_event(shortcut.key, shortcut.handler)

    def remove_terminal_shortcut(self, key, handler):
        for s in self.shortcuts:
            if s.key == key and s.handler == handler:
                self.keyboard.remove_key_event(key, handler)
                self.shortcuts.remove(s)
                break

    def render_inline(self):
        return "  ".join([f"[{s.key}] {s.name}" for s in self.shortcuts])

    def render_list(self):
        return "\n".join([f"{s.key}. {s.name}" for s in self.shortcuts])

    def clear(self):
        self.shortcuts = []

    def listen_thread(self):
        self.keyboard.start_thread()
    
    def listen(self):
        self.keyboard.run()
    
    def listen_once(self):
        self.keyboard.run_once()
    
    def stop_thread(self):
        self.keyboard.clear_events()
        self.keyboard.stop_thread()
