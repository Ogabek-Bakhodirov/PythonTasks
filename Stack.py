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




# def check_parentheses_spelling(string):
#     stack = Stack()
#     returnValue = False
#     for char in string:
#         if char in ['(', '{']:
#             stack.push(char)
#         elif char in [')', '}']:
#             if len(stack.list) == 0:
#                 returnValue = False
#             opening_bracket = stack.pop()
#             if (char == ')' and opening_bracket != '(') or (char == '}' and opening_bracket != '{'):
#                 returnValue = False
#     return len(stack.list) == 0



# print(check_parentheses_spelling("(x{xx(x(x))x}xxx)"))  # True
# print(check_parentheses_spelling("{x(xx})"))  # False
# print(check_parentheses_spelling("((x){xx}{((x)(x))(x)})"))  # True
