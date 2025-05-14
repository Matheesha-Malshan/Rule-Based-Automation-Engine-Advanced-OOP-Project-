
"""
FileCreatedTrigger sacrifices to visiting folder within each 1 second and 
using callback function and bound method of the action class is used
to procees the csv file
"""

import os
import time
from typing import Callable

from triggers.logger import Log
from triggers.trigger import Trigger


loger=Log()


class FileCreatedTrigger(Trigger):

    def __init__(self,path:str) -> None:
        self.path = path
        self.poll_interval = 1.0

    def watch_event(self,callback:Callable[[str], None]) -> None:  
        seen=set(os.listdir(self.path))
        while True:
            time.sleep(self.poll_interval)
            current = set(os.listdir(self.path))
            new_files = current-seen

            for fname in new_files:
                if fname.lower().endswith('.csv'):
                    callback(os.path.join(self.path,fname))
                else:
                    loger.warning("unexpected file upload")
                seen=current
           

