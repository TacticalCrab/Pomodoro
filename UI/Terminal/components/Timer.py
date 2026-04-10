from lib.Timer import Timer as BaseTimer
from art import text2art

class Timer(BaseTimer):
    def __init__(self):
        super().__init__()

    def render(self):
        total_seconds_left = self.get_time_left().total_seconds()
        minutes_left, seconds_left = divmod(total_seconds_left, 60)
        return text2art(f"{int(minutes_left):02}:{int(seconds_left):02}")
