"""
Within the Engine class build register method is to store the each instances
under the classes of action and triggers , these instances are excuted
on seperate thereds and use context manager to proper handling
"""

import threading
import time
from engine.rules import Rule


class Engine:

    def __init__(self) -> None:
        self.ruleList = []
        self._running = False
        self._threads = []

    def register(self, rule: Rule) -> None:  
        self.ruleList.append(rule)

    def run(self) -> None:
        self._running = True
        for r in self.ruleList:
            t = threading.Thread(target=r.run)
            t.daemon = True  
            t.start()
            self._threads.append(t)

        try:
            while self._running:
                time.sleep(1)
        except KeyboardInterrupt:
            self._running = False
            print("Engine stopped by user.")

    def __enter__(self) -> "Engine":
        print("Engine starting...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._running = False
        print("Engine shutting down...")

        for t in self._threads:
            if t.is_alive():
                t.join(timeout=1)
