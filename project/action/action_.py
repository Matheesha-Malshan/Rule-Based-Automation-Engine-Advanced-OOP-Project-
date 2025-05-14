"""
Here two actions are defined as Action and DeleteF , Action sacrifices
to excute the csv file within the folder ,the pipeline action is not
emplemented yet but this is exist on Action class

DeleleF class Delete csv files within the folder and logging details are
kept in a file
"""

import os

from triggers.logger import Log


logger=Log()


class Action:

    def execute(self,event_data:str) -> None:
        print(f"executed with pipeline: {event_data}")
        logger.info(f"File uploaded: {event_data}")


class DeleteF:

    def execute(self,event_data:str) -> None:
        if os.path.exists(event_data):
            try:
                os.remove(event_data)
                print(f"{event_data} deleted successfully.")
                logger.info(f"File deleted: {event_data}")
            except Exception as e:
                print( f"Failed to delete {event_data}: {e}")
                logger.error(f"Failed to delete {event_data}: {e}")
        else:
            logger.warning( f"File not exist {event_data}")

        
                