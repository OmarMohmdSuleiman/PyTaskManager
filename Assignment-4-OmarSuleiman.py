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
    def displayLinkedList(self):
        if self.isEmpty():
            print("empty")
        current=self.__header
        while current is not None:
            print(f"ID: {current.getTaskId()} Deecription: {current.getDescription()}, Priority: {current.getPriority()}")
            print("||")
            current=current.getNext()
        print("None")
    def getSize(self):
        size=0
        current=self.__header
        while current:
            size+=1
            current=current.getNext()
        return size
class PriorityQueue():

    def __init__(self):

        self.__linkedlist = LinkedList()



    def enqueue(self,desc,prio):
        t_id = 0
        for i in range(self.__linkedlist.getSize()):
            t_id += 1


        new_node = Task(t_id,desc,prio)
        
        return self.__linkedlist.addNodeWithPriority(new_node)
    


    def dequeue(self) -> int:

        self.__linkedlist.deleteNodeWithPriority()

    def displayPriorityQueue(self):

        self.__linkedlist.displayLinkedList()
    def displayCompletedPriorityQueue(self):

        self.__linkedlist.displayCompleted()

class Stack:


    def __init__(self):
        self.__lst = []

    def isEmpty(self):
        return len(self.__lst) == 0


    def push(self, desc,prio):

        self.__lst.insert(0,desc,prio)   


#Task Manager class
class TaskManager:
    def __init__(self):
        self.__task_queue=PriorityQueue()
        self.__task_history=Stack()


def displayMenu():
    print('''1. Adding a new task to the task manager.
          \n2. Getting a task from the queue given a task id.
          \n3. Marking the highest priority task as completed and putting it in the task history.
          \n4. Displaying all tasks in order of priority.
          \n5. Displaying only the tasks that are not completed.
          \n6. Displaying the last completed task.
          \n7. Exit''')
