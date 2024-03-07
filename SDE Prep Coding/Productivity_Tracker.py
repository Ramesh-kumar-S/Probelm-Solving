import json
from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    COMPLETED = "Completed"
    IN_PROGRESS = "In-Progress"
    NOT_STARTED = "Not-Yet-Started"
    
class LifeStyle:
    pass
    
class Task(object):
    def __init__(self, Name, Descr) -> None:
        """
        Task will be Initiated with Name and Descr

        Args:
            Name (Str): Name of the Task
            Descr (Str): Short Note about the Task
        """
        self.name = Name
        self.Descr = Descr
        self.taskStatus(TaskStatus.NOT_STARTED.value)  #Task Status will be Initialised as Not Yet Started
        # self.StartTime=None
        # self.EndTime=None
        # self.ElapsedTime=None
    
    def __getattribute__(self, name: str):
        
        if name == "StartTime":
            return datetime.now()
        else:
            return super().__getattribute__(name)
    
    def taskStatus(self,State):
        """Function to update the Task Status
        
        Args:
            State (Enum): Task State will be updated accordingly
        """
        self.Status = State
    
    def startTask(self):
        """
        Function which updates TaskStatus and StartTime
        """
        self.StartTime = datetime.now()
        self.taskStatus(TaskStatus.IN_PROGRESS.value) 
    
    def endTask(self):
        """
        Function which updates TaskStatus and StartTime
        """
        self.EndTime = datetime.now()
        self.taskStatus(TaskStatus.COMPLETED.value) 
        self.ElapsedTime = self.StartTime - self.EndTime
        
    def showTask(self):
        print("--------------------------------------")
        print("Name       : {}".format(self.name))
        print("Descr      : {}".format(self.Descr))
        print("Status     : {}".format(self.Status))
        if hasattr(self,"StartTime"):                               #use GetAttr
            print("Start Time : {}".format(self.StartTime))
        if  hasattr(self,"EndTime"):
            print("End Time  : {}".format(self.EndTime))
        if hasattr(self,"ElapsedTime"):
            print("Elapsed Time  : {}".format(self.ElapsedTime))
        print("--------------------------------------")
        

t = Task("CapMo","Cap Mo Issue")
t.startTask()
print(t.StartTime)
t.showTask()