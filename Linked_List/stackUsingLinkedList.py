class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data: int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: int) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_position(self, position: int, data: int) -> None:
        new_node = Node(data)

        if position < 1:
            print("Position should be 1 or greater.")
            return

        if position == 1:
            self.insert_at_begining(data)
            return

        current = self.head
        for i in range(1, position - 1):
            if current is None:
                print("Position exceeds the length of the list. Inserting at the end.")
                break
            current = current.next

        new_node.next = current.next if current else None
        if current:
            current.next = new_node
        else:
            self.insert_at_end(data)

    def delete_at_begining(self) -> None:
        if self.head is None:
            print("The list is already empty!")
        else:
            deleted_node = self.head
            self.head = self.head.next
            print(f"Deleted node with data: {deleted_node.data}")

    def delete_at_end(self) -> None:
        if self.head is None:
            print("The list is already empty!")
        elif self.head.next is None:
            deleted_node = self.head
            self.head = None
            print(f"Deleted the only node with data: {deleted_node.data}")
        else:
            current = self.head
            while current.next and current.next.next:
                current = current.next

            deleted_node = current.next
            current.next = None
            print(f"Deleted node with data: {deleted_node.data}")

    def delete_at_position(self, position: int) -> None:
        if self.head is None:
            print("The list is already empty!")
            return

        if position < 1:
            print("Position should be 1 or greater.")
            return

        if position == 1:
            self.delete_at_begining()
            return

        current = self.head
        for i in range(1, position - 1):
            if current.next is None:
                print("Position exceeds the length of the list.")
                return
            current = current.next

        if current.next is None:
            print("Position exceeds the length of the list.")
            return

        deleted_node = current.next
        current.next = deleted_node.next
        print(f"Deleted node with data: {deleted_node.data}")

    def display(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next
        