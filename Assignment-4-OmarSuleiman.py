#Node class
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
#Task class
class Task:
    def __init__(self,description:str,priority:int,completed=False):
        self.__task_id=0
        self.__description=description
        self.__priority=priority
        self.__completed=completed
    #Getters and Setters
    def getTaskId(self):
        return self.__task_id
    def getDescription(self):
        return self.__description
    def getPriority(self):
        return self.__priority
    def setPriority(self,priority):
        self.__priority=priority
    def getCompleted(self):
        return self.__completed
    def setCompleted(self,completed):
        self.__completed=True
        


        



        