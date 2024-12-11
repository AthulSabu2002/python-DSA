class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"
    
    def peek(self):
        if self.items:
            return self.items[-1]
        return "Stack is empty"
    
    def is_empty(self):
        return len(self.items) == 0
    


obj = Stack()
print(obj.is_empty())
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop()) 
print(obj.peek()) 
print(obj.is_empty()) 