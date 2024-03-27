#Node class
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
#Task class
class Task:
    def __init__(self,description:str,priority:int,completed:bool):
        self.__task_id=0
        self.__description=description
        self.__priority=priority
        self.__completed=completed



        