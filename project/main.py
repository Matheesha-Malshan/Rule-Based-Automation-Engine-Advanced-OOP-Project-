"""
FileCreatedTRigger and FileDeleteTrigger is register using metaclass
and use contect manager to proper call and gracegull stop
"""

from engine.rules import Rule
from engine.enginec import Engine
from action.action_ import Action,DeleteF
from triggers.fileDeleteTrigger import FileDeletedTrigger
from triggers.fileCreatedTrigger import FileCreatedTrigger
from triggers.trigger import TRIGGER_REGISTRY


trigger_class1 = TRIGGER_REGISTRY["FileCreatedTrigger"]
path1 = trigger_class1(r"C:\Users\HP\async\project\dbin")
action_create = Action()
rule1 = Rule(path1,action_create)


trigger_class2 = TRIGGER_REGISTRY["FileDeletedTrigger"]
path2 = trigger_class2(r"C:\Users\HP\async\project\dbin")
action_delete = DeleteF()
rule2 = Rule(path2, action_delete)

with Engine() as engine:
    engine.register(rule1)
    engine.register(rule2)
    engine.run()

