#Task class
class Task:
    def __init__(self,task_id,description:str,priority:int):
        self.__next=None
        self.__task_id= task_id
        self.__description=description
        self.__priority=priority
        self.__completed=False
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
        self.__completed=completed
    def getNext(self):
        return self.__next
    def setNext(self,new_next):
        self.__next=new_next

#Linked List class
class LinkedList:

    def __init__(self):
        self.__header = None


    def isEmpty(self):
        return self.__header == None

    

    def addNodeWithPriority(self,new_node :Task) -> None:

        if (self.isEmpty):
            self.__header = new_node
            return

        if (new_node.getPriority() < self.__header.getPriority()):
            new_node.setNext(self.__header)
            self.__header = new_node
            
            

        current = self.__header 
        previous =  None

        while (current is not None and current.getPriority() >= new_node.getPriority() ):
            previous = current
            current = current.getNext()
            


        previous.setNext(new_node)
        new_node.setNext(current)

    def deleteNodeWithPriority(self):
        current=self.__header
        self.__header=self.__header.getNext()
        current.setNext(None)
        deleted=f"The deleted task is: {current}"
        return deleted
    def displayCompleted(self):
        if self.isEmpty():
            print("empty")
        current=self.__header
        while current:
            if current.getCompleted()==True:
                print(f"ID: {current.getTaskId()} completed: {current.getCompleted()}")
            else:
                print("not completed")
                current=current.getNext()
    def markAsCompleted(self):
        current=self.__header
        while current:
            if current.getCompleted()==False:
                self.__header.setCompleted(True)
                break
            self.__header=current.getNext()

    


#Task Manager class
class TaskManager:
    def __init__(self,task):
        self.__task=task
    def queueTask(self):
        LinkedList.addNodeWithPriority()
        


        


        



        