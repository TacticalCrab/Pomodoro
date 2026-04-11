from dataclasses import dataclass
from datetime import timedelta

@dataclass
class SessionFile:
    file_path: str
    name: str

class TimeType:
    BREAK = "BREAK"
    POMODORO = "POMODORO"

@dataclass
class SessionTime:
    type: TimeType
    time: timedelta