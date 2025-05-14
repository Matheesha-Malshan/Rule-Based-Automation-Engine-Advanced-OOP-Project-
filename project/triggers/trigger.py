"""
for the Trigger class i build a meta class to manually build the 
class object because of the i can ability to auto register the 
Trigger classes and add more method/triggers inherits from Trigger class
Trigger

#<class 'triggers.trigger.TriggerMeta'>
#FileCreatedTrigger
#<class 'triggers.trigger.TriggerMeta'>

#<class 'triggers.fileCreatedTrigger.FileCreatedTrigger'>
#{'FileCreatedTrigger': <class 'triggers.fileCreatedTrigger.FileCreatedTrigger'>}
"""

TRIGGER_REGISTRY = {}


class TriggerMeta(type):

    def __new__(cls, name, bases, namespace) -> object:
        if name != "Trigger" and "watch_event" not in namespace:
            raise TypeError(f"{name} must implement watch_event()") 
        return super().__new__(cls, name, bases, namespace)

    def __init__(cls, name, bases, namespace) -> object:
        if name != "Trigger":
            TRIGGER_REGISTRY[name] = cls  
        super().__init__(name, bases, namespace)


class Trigger(metaclass=TriggerMeta):
    pass

