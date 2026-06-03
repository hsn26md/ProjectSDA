# Ganti keseluruhan blok class CustomQueue di data_structures.py dengan ini:

class CustomQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, data: dict) -> None:
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self) -> dict | None:
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return data

    def peek(self) -> dict | None:
        return self.head.data if self.head else None

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        return self._size

    def display(self) -> list:
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result