class Node:
    def __init__(self, x):
        self.info = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.__tail = None

    def add(self, addedValue):
        newValue = Node(addedValue)
        if self.head == None:
            self.head = newValue
            self.__tail = newValue
        else:
            self.__tail.next = newValue
            self.__tail = newValue

    def printElements(self):
        value = self.head
        while(value != None):
            print(value.info)
            value = value.next

    def deleteTop(self):
        deletedElement = self.head
        self.head = self.head.next
        del(deletedElement)


    # def addToHead(self, x):
    #     head = Node(x)
    #     head.next = self.__head
    #     self.__head = head


    # def addToAfterX(self, after, value):
    #     newValue = Node(value)
    #     startValue = self.__head
    #     while(startValue.info != after and startValue == self.__tail):
    #         startValue = startValue.next
    #     oldNext = startValue.next
    #     startValue.next = newValue
    #     newValue.next = oldNext

        
        

linkedList = LinkedList()
linkedList.add(2)
linkedList.add(11)
linkedList.add(10)
linkedList.add(12)
linkedList.add(9)
linkedList.add(110)
linkedList.add(900)
linkedList.printElements()
print("\n")

current = linkedList.head
print(current.info)

while current.next != None:
    next = current.next
    if current.info < next.info:
        print(next.info)
    current = next   

