class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt

class queueUsingLinkedList:
    def __init__(self):
        self.head = None
        
    def enqueue(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while(current.nxt):
                current = current.nxt
            current.nxt = new_node
            
    def dequeue(self) -> None:
        if self.head is None:
            print("The queue is already empty!")
        else:
            deleted_node = self.head
            self.head = self.head.nxt
            print(f"Deleted node with data: {deleted_node.data}")

    
    def display(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" -> " if current.nxt else "\n")
            current = current.nxt
        
obj = queueUsingLinkedList()

obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
obj.enqueue(50)

obj.display()

obj.dequeue()

obj.display()