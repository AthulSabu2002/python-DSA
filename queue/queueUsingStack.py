class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item) -> None:
        self.items.append(item)
        
    def pop(self) -> int:
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Empty"
    
    def peek(self) -> int:
        if self.items:
            return self.items[-1]
        return "Empty"
    
    def is_empty(self):
        return len(self.items) == 0
    

class QueueUsingStack:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def enqueue(self, item) -> None:
        self.s1.push(item)
    
    def dequeue(self) -> int:
        if self.s1.is_empty():
            if self.s2.is_empty():
                print("Queue is empty")
            else:
                self.s2.push(self.s1.pop())
            
        return self.s2.pop()
    
            
            
obj = QueueUsingStack()

obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)