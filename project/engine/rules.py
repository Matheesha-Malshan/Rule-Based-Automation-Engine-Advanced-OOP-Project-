
"""
Withing the Rule class instances are seperatly run within the threads
"""

from action.action_ import Action
from triggers.fileCreatedTrigger import FileCreatedTrigger


class Rule:

    def __init__(self, file: FileCreatedTrigger,
                 action: Action) -> None:        
        self.file = file
        self.action = action
        
    def run(self) -> None:
        self.file.watch_event(self.action.execute)
        self.file.watch_event(self.action.execute)

       

    