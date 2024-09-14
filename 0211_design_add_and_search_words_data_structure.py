# fairly simple trie
class WordDictionary:

    def __init__(self):
        self.r = {}

    def addWord(self, word: str) -> None:
        n = self.r
        for c in word:
            if c not in n:
                n[c] = {}
            n = n[c]
        n["#"] = 0

    def search(self, word: str) -> bool:
        candidates = [self.r]
        for c in word:
            candidates_new = []
            for n in candidates:
                if c == ".":
                    candidates_new += [n[i] for i in n if i != "#"]
                elif c in n:
                    candidates_new.append(n[c])
            candidates = candidates_new
        for n in candidates:
            if "#" in n:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)