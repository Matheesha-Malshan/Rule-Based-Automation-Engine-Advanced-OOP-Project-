"""
FileDeletedTrigger sacrifices to visiting folder within each 1 second and 
using callback function and bound method of the DeleteF class is used
to procees the csv file
"""


import time
import os
from typing import Callable

from triggers.trigger import Trigger


class FileDeletedTrigger(Trigger):

    def __init__(self, path: str) -> None:
        self.path = path
        self.poll_interval = 1.0
        self._previous = set()

    def watch_event(self, callback: Callable[[str], None]) -> None:
        self._previous = set(os.listdir(self.path))
        while True:
            time.sleep(self.poll_interval)
            current = set(os.listdir(self.path))
            deleted = self._previous - current
            
            if deleted:
                for fname in deleted:
                    callback(os.path.join(self.path, fname))
            self._previous = current

