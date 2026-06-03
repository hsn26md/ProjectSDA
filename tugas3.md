# Ganti keseluruhan blok class UndoStack di data_structures.py dengan ini:

class UndoStack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data: dict) -> None:
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self) -> dict | None:
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data

    def peek(self) -> dict | None:
        return self.top.data if self.top else None

    def is_empty(self) -> bool:
        return self.top is None

    def size(self) -> int:
        return self._size

    def display(self) -> list:
        result = []
        current = self.top
        while current is not None:
            result.append(current.data)
            current = current.next
        return result