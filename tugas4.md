# Ganti keseluruhan blok kelas TrieNode dan MenuTrie di app.py dengan ini:

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.menu_key = None

class MenuTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, menu_key):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.menu_key = menu_key

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return [] 
            node = node.children[char]
        
        results = set()
        self._dfs(node, results)
        return list(results)

    def _dfs(self, node, results):
        if node.is_end:
            results.add(node.menu_key)
        for child in node.children.values():
            self._dfs(child, results)