class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

class StackUsingLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data: int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> None:
        if self.head is None:
            print("The stack is already empty!")
        else:
            deleted_node = self.head
            self.head = self.head.next
            print(f"Deleted node with data: {deleted_node.data}")


    def display(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next
        
obj = StackUsingLinkedList()

obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)

obj.display()

obj.pop()
obj.pop()

obj.display()
