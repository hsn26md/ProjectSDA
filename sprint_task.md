# 🚀 MatchaQ - Sprint Tasks & Guidelines

Repositori ini berisi kerangka dasar (*boilerplate*) untuk aplikasi Kasir MatchaQ. Antarmuka (UI) dan routing Flask sudah disediakan, namun logika **Struktur Data dan Algoritma (SDA)** masih kosong. 

Tugas kita adalah menghidupkan sistem ini sesuai dengan modul pembagian di bawah. Setiap anggota bertanggung jawab atas satu struktur data.

## 📌 Alur Kerja (Workflow)
1. Lakukan `git pull` dari repositori ini.
2. Buat *branch* baru sesuai nama fiturmu (contoh: `git checkout -b fitur-queue`).
3. Cari blok komentar `# TODO:` di dalam file yang ditugaskan kepadamu.
4. Hapus perintah `pass` atau nilai balikan sementara (seperti `return None` atau `return []`), lalu ganti dengan logika kodemu.
5. Uji coba kodemu secara lokal dengan menjalankan `python app.py`.
6. Lakukan *Commit* dan *Push*.

---

## 👨‍💻 Pembagian Tugas (Sprints)

### 🟢 TUGAS 1: Sistem Antrean Dapur (Queue / Linked List)
**File Target:** `data_structures.py` (Kelas `CustomQueue`)
**Deskripsi:** Dapur Barista saat ini tidak menerima pesanan. Kamu harus mengimplementasikan antrean menggunakan prinsip **FIFO (First In, First Out)** berbasis *Linked List*.
**Langkah Pengerjaan:**
1. Di dalam `__init__`, inisialisasi `self.head` dan `self.tail` dengan `None`, serta `self._size` dengan `0`.
2. Di dalam `enqueue(data)`, buat objek `Node` baru. Atur pointer `tail.next` dan `tail` agar node baru berada di posisi paling belakang antrean. Jangan lupa tambah ukuran (size).
3. Di dalam `dequeue()`, ambil data dari `head`, lalu geser `head` ke node berikutnya (`head.next`). Jika antrean menjadi kosong, pastikan `tail` juga diatur menjadi `None`. Kurangi ukuran (size).
4. Di dalam `display()`, buat list kosong. Lakukan *looping* (traversal) dari `head` hingga node terakhir (`None`), masukkan datanya ke dalam list, lalu kembalikan list tersebut agar UI bisa membacanya.

### 🟡 TUGAS 2: Sistem Pesanan Tertunda (Hash Map)
**File Target:** `data_structures.py` (Kelas `PendingMap`)
**Deskripsi:** Fitur "Hold" pesanan belum berfungsi. Kamu harus mengimplementasikan penyimpanan data berkecepatan $O(1)$ menggunakan **Hash Table** (via Dictionary Python).
**Langkah Pengerjaan:**
1. Di dalam `__init__`, buat dictionary kosong pada `self._store`.
2. Di dalam `add(order_id, data)`, masukkan pasangan *key-value* tersebut ke dalam dictionary.
3. Di dalam `remove(order_id)`, gunakan metode `.pop()` bawaan dictionary untuk mencabut pesanan secara aman dan mengembalikannya.
4. Di dalam `get_all()`, cukup kembalikan nilai `self._store` secara keseluruhan agar UI bisa merendernya.

### 🔴 TUGAS 3: Fitur Pembatalan Pesanan Kasir (Stack)
**File Target:** `data_structures.py` (Kelas `UndoStack`)
**Deskripsi:** Kasir tidak bisa mengurungkan pesanan jika salah klik. Implementasikan fitur pembatalan menggunakan prinsip **LIFO (Last In, First Out)** berbasis *Linked List*.
**Langkah Pengerjaan:**
1. Di dalam `__init__`, inisialisasi `self.top` dengan `None`.
2. Di dalam `push(data)`, buat objek `Node` baru. Sambungkan `node.next` ke `self.top` yang lama, lalu jadikan node baru tersebut sebagai `self.top` yang baru.
3. Di dalam `pop()`, ambil data dari `self.top`, lalu turunkan pointer `self.top` ke node di bawahnya (`self.top.next`).
4. Di dalam `display()`, lakukan iterasi traversal ke bawah persis seperti antrean, namun dimulai dari `self.top`.

### 🔵 TUGAS 4: Mesin Pencari Auto-Complete (Trie)
**File Target:** `app.py` (Kelas `TrieNode` dan `MenuTrie`)
**Deskripsi:** *Search bar* di aplikasi saat ini buta. Kamu harus mengimplementasikan pencarian kata berkecepatan tinggi $O(L)$ menggunakan struktur data **Trie (Prefix Tree)**.
**Langkah Pengerjaan:**
1. Di dalam `TrieNode.__init__`, siapkan `children` (dictionary), `is_end` (boolean), dan `menu_key` (None).
2. Di dalam `MenuTrie.insert()`, pecah input `word` menjadi karakter huruf kecil. Buat iterasi: jika huruf belum ada di `children`, buat `TrieNode` baru. Di akhir kata, tandai `is_end = True` dan simpan `menu_key`-nya.
3. Di dalam `MenuTrie.search_prefix()`, telusuri huruf demi huruf dari input kasir. Jika ada huruf yang terputus/tidak ditemukan, langsung kembalikan list kosong `[]`. Jika pencarian awalan berhasil, oper sisa node tersebut ke fungsi `_dfs()`.
4. Di dalam `_dfs()`, gunakan rekursi. Jika node saat ini adalah akhir kata (`is_end`), tambahkan `menu_key` ke dalam set `results`. Lakukan pemanggilan `_dfs` untuk setiap *child* yang ada.