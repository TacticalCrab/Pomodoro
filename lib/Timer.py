import datetime as dt

class TimerNotStarted(Exception):
    def __init__(self, *args):
        super().__init__("Timer not started yet")

class Timer:
    time: dt.timedelta = dt.timedelta()
    start_time: dt.datetime = None

    @property
    def end_time(self):
        start_time = self.start_time if self.start_time is not None else dt.datetime.now()
        return start_time + self.time

    def is_started(self):
        return self.start_time is not None

    def get_time_left(self):
        current_time = dt.datetime.now()
        time_left = self.end_time - current_time
        return time_left if time_left.total_seconds() >= 0 else dt.timedelta()

    def get_seconds_left(self):
        return self.get_time_left().total_seconds()

    def set_time(
        self, 
        seconds: float = 0,
        minutes: float = 0,
        hours: float = 0,
        days: float = 0,
        microseconds: float = 0,
        milliseconds: float = 0,
        weeks: float = 0
    ):
        self.time = dt.timedelta(
            seconds=seconds,
            minutes=minutes,
            hours=hours,
            days=days,
            microseconds=microseconds,
            milliseconds=milliseconds,
            weeks=weeks
        )

    def start(self):
        self.start_time = dt.datetime.now()

    def reset(self):
        self.start_time = None

if __name__ == "__main__":
    from time import sleep

    timer = Timer()
    timer.set_time(seconds=10)
    timer.start()
    while timer.get_seconds_left() > 0:
        print(timer.get_seconds_left())
        sleep(2)

