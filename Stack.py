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

value = '{x(xx})'
stack = Stack()
for i in value:
    if i == '(':
        stack.push(1)
    elif i == ')':
        stack.push(-1)
    elif i == '{':
        stack.push(2)
    elif i == '}':
        stack.push(-2)
    else:
        stack.push(0)

stack.printValues()

print("\n")

def checker(stack, index):
    count = 0
    for value in stack:
        if value != 0:
            print(value)
        count += 1

checker(stack.list, 0)