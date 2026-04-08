import datetime as dt

class Timer:
    _stop_time: dt.datetime = None
    _count_from_time: dt.datetime = None
    _time: dt.datetime = None

    time: dt.timedelta = dt.timedelta()
    start_time: dt.datetime = None
    is_stopped: bool = True

    def get_end_time(self):
        start_time = dt.datetime.now()
        if self._count_from_time is not None and not self.is_stopped:
            start_time = self._count_from_time

        return start_time + self._time

    def get_time_left(self):
        current_time = dt.datetime.now()
        time_left: dt.timedelta = self.get_end_time() - current_time
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

        self._time = self.time

    def start(self):
        self.is_stopped = False

        self.start_time = dt.datetime.now()
        self._count_from_time = self.start_time
    
    def stop(self):
        self.is_stopped = True

        self._stop_time = dt.datetime.now()
        self._time = self._time - (self._stop_time - self._count_from_time)

    def resume(self):
        self.is_stopped = False
        self._count_from_time = dt.datetime.now()

    def reset(self):
        self.is_stopped = True
        self.start_time = None
        self._count_from_time = None
        self._stop_time = None
        self._time = self.time

    def __str__(self):
        total_seconds_left = self.get_time_left().total_seconds()
        minutes_left, seconds_left = divmod(total_seconds_left, 60)
        return f"{round(minutes_left):02}:{round(seconds_left):02}"


if __name__ == "__main__":
    from time import sleep

    timer = Timer()
    timer.set_time(seconds=20)
    timer.start()
    print("Start time:", timer.get_seconds_left())

    sleep(2)
    print("Timer before stop: ", timer.get_seconds_left())
    timer.stop()
    print("Timer stopped at: ", timer.get_seconds_left())

    sleep(2)
    print("Timer afer 2 seconds of stopped: ", timer.get_seconds_left())

    timer.resume()
    print("Timer after resumed", timer.get_seconds_left())

    sleep(2)
    print("Timer 2 seconds after resume", timer.get_seconds_left())

    sleep(2)
    print("Timer 2 seconds after resume", timer.get_seconds_left())

    print("Timer before stop: ", timer.get_seconds_left())
    timer.stop()
    print("Timer stopped at: ", timer.get_seconds_left())

    sleep(2)
    print("Timer afer 2 seconds of stopped: ", timer.get_seconds_left())

    timer.resume()
    print("Timer after resumed", timer.get_seconds_left())

    sleep(2)
    print("Timer 2 seconds after resume", timer.get_seconds_left())
