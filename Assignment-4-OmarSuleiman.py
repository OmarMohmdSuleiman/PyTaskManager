#Node class
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    def getData(self):
        return self.__data
    def getNext(self):
        return self.__next
    def setNext(self,new_next):
        self.__next=new_next
#Linked List class
class LinkedList:
    def __init__(self):
        self.__header=None
    def isEmpty(self):
        return self.__header==None
    #add priority queue
    def addNodeWithPriority(self,new_node : Node) -> None:

        if (self.isEmpty()):
            self.__header = new_node
            return

        if (new_node.getData() > self.__header.getData()):
            new_node.setNext(self.__header)
            self.__header = new_node

        current = self.__header 
        previous =  self.__header 

        while (current is not None and current.getData() >= new_node.getData() ):
            previous = current
            current = current.getNext()


        previous.setNext(new_node)
        new_node.setNext(current)
    
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
        


        



        