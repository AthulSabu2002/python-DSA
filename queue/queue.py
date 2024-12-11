class Queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.current_size = 0
        self.max_size = 15
        self.queue = [0] * self.max_size
        
    def enqueue(self, item: int) -> None:
        if self.current_size == self.max_size:
            print("queue is full!")
            exit(1)
        elif self.rear == -1:
            self.rear = 0
            self.front = 0
        else:
            self.rear += 1
            
        self.queue[self.rear] = item
        self.current_size += 1
        
        print("The queue is: ")
        self.display()
    
    def dequeue(self) -> None:
        if self.current_size == 0:
            print("The queue is already empty!")
            exit(1)
        popped = self.queue[self.front]
        
        if self.current_size == 1:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        
        self.current_size -= 1
        
        self.display()
    
    def display(self) -> None:
        if self.current_size == 0:
            print("The queue is empty")
        else:
            print(self.queue[self.front: self.rear + 1])


obj = Queue()

obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
obj.enqueue(50)
obj.enqueue(60)

obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()