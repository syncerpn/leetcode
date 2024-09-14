# with hash table
# basics of a trie
class Trie:

    def __init__(self):
        self.r = {}

    def insert(self, word: str) -> None:
        n = self.r
        for c in word:
            if c not in n:
                n[c] = {}
            n = n[c]
        n["#"] = 0

    def search(self, word: str) -> bool:
        n = self.r
        for c in word:
            if c not in n:
                return False
            n = n[c]
        return True if "#" in n else False

    def startsWith(self, prefix: str) -> bool:
        n = self.r
        for c in prefix:
            if c not in n:
                return False
            n = n[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)