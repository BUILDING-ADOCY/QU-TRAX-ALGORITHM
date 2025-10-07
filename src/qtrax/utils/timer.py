import time
from typing import Optional

class Timer:
    """Simple timer context manager."""
    def __init__(self) -> None:
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None

    def __enter__(self) -> 'Timer':
        self.start()
        return self

    def start(self) -> None:
        self.start_time = time.perf_counter()
        self.end_time = None

    def stop(self) -> None:
        self.end_time = time.perf_counter()

    def elapsed(self) -> float:
        if self.start_time is None:
            return 0.0
        end = self.end_time if self.end_time is not None else time.perf_counter()
        return end - self.start_time

    def __exit__(self, exc_type, exc, tb) -> None:
        self.stop()
