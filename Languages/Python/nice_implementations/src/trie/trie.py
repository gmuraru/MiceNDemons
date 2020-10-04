from collections import defaultdict


class Trie:
    def __init__(self):
        def node():
            return defaultdict(node)

        self.root = node()

    def insert(self, word: str):
        node = self.root

        for c in word:
            node = node[c]

        node[None]

    def find(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c not in node:
                return False

            node = node[c]

        return None in node

    def delete(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c not in node:
                return False
            
            node = node[c]

        if None in node:
            del node[None]
            return True

        return False
