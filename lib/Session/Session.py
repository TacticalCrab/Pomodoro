from .types import SessionTime


class SessionIter:
    times: list[SessionTime]

    def __init__(self, times):
        self.times = times
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.times):
            value = self.times[self.current]
            self.current += 1
            return value
        else:
            raise StopIteration

class Session:
    times: list[SessionTime]
    name: str

    def __init__(self, name, times: list[SessionTime]):
        self.name = name
        self.times = times

    def __iter__(self):
        return SessionIter(self.times)

    def current_time(self):
        return self.times[self.current]
