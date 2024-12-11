class Queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.current_size = 0
        self.max_size = 15
        self.queue = [0] * self.max_size
        
    def enqueue(self, item: int) -> None:
        if self.current_size == self.max_size:
            exit(1)
        elif self.rear == -1:
            self.rear = 0
            self.front = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
            
        self.queue[self.rear] = item
        self.current_size += 1
    
    
    def dequeue(self) -> int:
        if self.current_size == 0:
            exit(1)
        popped = self.queue[self.front]
        
        if self.current_size == 1:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        
        self.current_size -= 1
        
        return popped
    
    def display(self) -> None:
        if self.current_size == 0:
            print("Empty!")
        else:
            index = self.front
            items = []
            for _ in range(self.current_size):
                items.append(self.queue[index])
                index = (index + 1) % self.max_size
            print(items)


class StackUsingQueue:
    def __init__(self):
        self.q = Queue()
    
    def push(self, item) -> None:
        size = self.q.current_size
        
        self.q.enqueue(item)
        
        for i in range(size):
            self.q.enqueue(self.q.dequeue())
        
        self.q.display()
        
    def pop(self) -> int:
        if self.q.current_size == 0:
            print("The stack is empty!")
        else:
            return self.q.dequeue()
        
    def display(self) -> None:
        if self.q.current_size == 0:
            print("The stack is empty!")
        else:
            self.q.display()
            
obj = StackUsingQueue()

obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
obj.push(60)

obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()