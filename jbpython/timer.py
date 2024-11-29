import datetime as dt
from typing import NamedTuple, Dict, Any, Optional, List
import logging
import time

FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class Timing(NamedTuple):
    start: dt.datetime
    end: dt.datetime
    seconds: float

    @classmethod
    def from_json(cls, json: Dict[str, Any]) -> "Timing":
        start = dt.datetime.strptime(json["start"], FORMAT)
        end = dt.datetime.strptime(json["end"], FORMAT)
        seconds = float(json["seconds"])
        return Timing(start, end, seconds)

    def to_json(self) -> Dict[str, Any]:
        return {"start": self.start.strftime(FORMAT), "end": self.end.strftime(FORMAT), "seconds": self.seconds}

    
class Timer:
    def __init__(self, name: Optional[str] = None, logger: Optional[logging.Logger] = None) -> None:
        self._log = logger
        self._name = name

    def __enter__(self):  # type:ignore
        self.start = time.perf_counter()
        self.start_time = dt.datetime.utcnow()
        return self

    def __exit__(self, *arg: List[Any]) -> None:
        self.end = time.perf_counter()
        self.end_time = dt.datetime.utcnow()
        self.interval = self.end - self.start
        self.timing = Timing(self.start_time, self.end_time, self.interval)
        if self._log is not None:
            self._log.info(f"{self._name or 'Timer'}: {self.interval} seconds")
            
