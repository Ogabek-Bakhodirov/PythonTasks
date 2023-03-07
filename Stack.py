class Stack:
    # Init
    def __init__(self):
        self.list = []

    # Add new Element in Top of List.
    def push(self, value):
        self.list.insert(0, value)

    # Removes Top Itme in List and returns it.
    def pop(self):
        value = list[0]
        self.list.pop(0)
        return value 
    
    # Returns top element of List
    def top(self):
        return self.list[0]
    
    # Returns number of elements in List
    def size(self):
        return len(self.list)
    
    # Check is list Empty or not.
    def isEmpty(self):
        if (self.size(self) == 0):
            return True
        else: 
            return False
        # Print Values.
    def printValues(self):
        print(self.list)

list = [1, 2, 3, 4, 5, 4, 7]
stack = Stack()
for i in list:
    stack.push(i)
stack.printValues()
stack.pop()
stack.printValues()
topValue = stack.top()
numberOfValues = stack.size()
print(numberOfValues, topValue)