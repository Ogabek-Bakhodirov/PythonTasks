class Node:
    def __init__(self, x):
        self.info = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def add(self, addedValue):
        newValue = Node(addedValue)
        if self.__head == None:
            self.__head = newValue
            self.__tail = newValue
        else:
            self.__tail.next = newValue
            self.__tail = newValue

    def printElements(self):
        value = self.__head
        while(value != None):
            print(value.info)
            value = value.next

    def addToHead(self, x):
        head = Node(x)
        head.next = self.__head
        self.__head = head
        
        

linkedList = LinkedList()
linkedList.add(23)
linkedList.add(11)
linkedList.add(22)
linkedList.printElements()
print("\n")
linkedList.addToHead(20)
linkedList.printElements()



# node = Node("D")
# node.__next = 1
# print(node.__info)
