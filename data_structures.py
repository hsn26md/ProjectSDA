class Node:
    def __init__(self, data: dict):
        self.data = data
        self.next = None

# ============================================================
# TUGAS 1: Implementasi Linked List (FIFO)
# ============================================================
class CustomQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, data: dict) -> None:
        # TODO: Tambahkan node baru ke belakang (tail) antrean
        pass

    def dequeue(self) -> dict | None:
        # TODO: Ambil dan hapus node dari depan (head) antrean
        return None

    def peek(self) -> dict | None:
        # TODO: Lihat data terdepan tanpa menghapus
        return None

    def is_empty(self) -> bool:
        # TODO: Cek apakah antrean kosong
        return True

    def size(self) -> int:
        # TODO: Kembalikan ukuran antrean
        return 0

    def display(self) -> list:
        # TODO: Lakukan traversal Linked List, masukkan datanya ke dalam list Python untuk UI
        return []


# ============================================================
# TUGAS 2: Implementasi Hash Map (Dictionary)
# ============================================================
class PendingMap:
    def __init__(self):
        self._store: dict = {}

    def add(self, order_id: str, data: dict) -> None:
        # TODO: Tambahkan data pesanan ke dalam hash map berdasarkan order_id
        pass

    def remove(self, order_id: str) -> dict | None:
        # TODO: Hapus dan kembalikan data pesanan dari hash map
        return None

    def get(self, order_id: str) -> dict | None:
        # TODO: Ambil data tanpa menghapus
        return None

    def exists(self, order_id: str) -> bool:
        # TODO: Cek apakah order_id ada di dalam hash map
        return False

    def get_all(self) -> dict:
        # TODO: Kembalikan seluruh isi hash map
        return {}

    def size(self) -> int:
        # TODO: Kembalikan jumlah pesanan pending
        return 0

    def is_empty(self) -> bool:
        # TODO: Cek apakah hash map kosong
        return True


# ============================================================
# TUGAS 3: Implementasi Stack (LIFO)
# ============================================================
class UndoStack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data: dict) -> None:
        # TODO: Masukkan data pesanan ke atas (top) tumpukan stack
        pass

    def pop(self) -> dict | None:
        # TODO: Ambil dan hapus pesanan dari atas (top) tumpukan stack
        return None

    def peek(self) -> dict | None:
        # TODO: Lihat pesanan teratas tanpa menghapus
        return None

    def is_empty(self) -> bool:
        # TODO: Cek apakah stack kosong
        return True

    def size(self) -> int:
        # TODO: Kembalikan ukuran stack
        return 0

    def display(self) -> list:
        # TODO: Lakukan traversal Stack, masukkan datanya ke dalam list
        return []