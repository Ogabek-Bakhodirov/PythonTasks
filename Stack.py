class Stack:
    def __init__(self):
        self.list = []
    def push(self, value):
        self.list.insert(0, value)
    def pop(self):
        value = list[0]
        self.list.pop(0)
        return value 
    def top(self):
        return self.list[0]
    def size(self):
        return len(self.list)
    def isEmpty(self):
        if (size(self) == 0):
            return True
        else: 
            return False
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

if stack.size() % 2 == 0:
    for i in range(stack.size() / 2):
        print(i)