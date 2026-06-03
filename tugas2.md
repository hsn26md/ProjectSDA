# Ganti keseluruhan blok class PendingMap di data_structures.py dengan ini:

class PendingMap:
    def __init__(self):
        self._store: dict = {}

    def add(self, order_id: str, data: dict) -> None:
        self._store[order_id] = data

    def remove(self, order_id: str) -> dict | None:
        return self._store.pop(order_id, None)

    def get(self, order_id: str) -> dict | None:
        return self._store.get(order_id, None)

    def exists(self, order_id: str) -> bool:
        return order_id in self._store

    def get_all(self) -> dict:
        return self._store

    def size(self) -> int:
        return len(self._store)

    def is_empty(self) -> bool:
        return len(self._store) == 0