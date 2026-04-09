import msvcrt
from threading import Thread


class TerminalKeyboard:
    _events: dict[str, set]
    _is_running: bool
    _thread: Thread

    def __init__(self):
        self._events = {}
        self._is_running = True
        self._thread = None

    def register_key_event(self, key, handler):
        if key not in self._events:
            self._events[key] = set()

        self._events[key].add(handler)

    def remove_key_event(self, key, handler):
        if key not in self._events:
            return

        if handler not in self._events[key]:
            return

        self._events[handler].remove(handler)
    
    def clear_events(self):
        self._events = {}
    
    def run_once(self):
        key = msvcrt.getch()
        if not self._is_running:
            return

        if key == b'\x03':
            raise KeyboardInterrupt()

        key = key.decode()
        if key in self._events:
            for handler in self._events[key]:
                handler()

    def run(self):
        while self._is_running:
            self.run_once()
    
    def start_thread(self):
        self._is_running = True
        self._thread = Thread(
            target=lambda: self.run(),
            daemon=True
        )
        self._thread.start()

    def stop_thread(self):
        if self._thread is not None:
            self._is_running = False


if __name__ == "__main__":
    from time import sleep

    tk = TerminalKeyboard()
    tk.register_key_event("a", lambda: print("Yoooo!"))
    tk.register_key_event("a", lambda: print("BAM!!"))
    tk.register_key_event("c", lambda: tk.clear_events())
    tk.register_key_event("b", lambda: tk.stop_thread())

    tk.start_thread()

    while True:
        print("Hello world!")
        sleep(1)