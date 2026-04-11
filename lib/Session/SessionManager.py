from os import listdir
from os.path import isfile, join
from datetime import timedelta
from .Session import Session
from .types import SessionFile, TimeType, SessionTime


class SessionManager:
    sessions_dir: str

    def __init__(self, sessions_dir):
        self.sessions_dir = sessions_dir

    def parse_session_time(self, time):
        if ":" in time:
            time = list(map(int, time.split(":")))
            return timedelta(
                minutes=time[0],
                seconds=time[1]
            )
        else:
            return timedelta(
                seconds=int(time)
            )

    def session_from_file(self, file_path):
        with open(join(self.sessions_dir, file_path)) as file:
            session_name = file.readline().split("=")[1]
            session_times_raw = map(
                self.parse_session_time,
                file.readline().split("=")[1].split(",")
            )

            session_times = []
            for i, session_time in enumerate(session_times_raw, 1):
                time_type = TimeType.POMODORO if i % 2 == 1 else TimeType.BREAK
                session_times.append(SessionTime(
                    type=time_type,
                    time=session_time
                ))

        return Session(
            name=session_name,
            times=session_times
        )

    def resolve_session_file(self, session_file: SessionFile):
        return self.session_from_file(session_file.file_path)

    def get_session_files(self):
        files = [f for f in listdir(self.sessions_dir) if isfile(join(self.sessions_dir, f))]
        session_files = []
        for file in files:
            with open(join(self.sessions_dir, file)) as f:
                name = f.readline().split("=")[1].replace("\n", "")
                session_files.append(SessionFile(
                    name=name,
                    file_path=file
                ))

        return session_files
