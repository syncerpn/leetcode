# trie
class MapSum:

    def __init__(self):
        self.r = {}

    def insert(self, key: str, val: int) -> None:
        r = self.r
        for c in key:
            if c not in r:
                r[c] = {}
            r = r[c]
        r["."] = val

    def sum(self, prefix: str) -> int:
        def get_score(r):
            score = 0
            for k in r:
                if k == ".":
                    score += r[k]
                else:
                    score += get_score(r[k])
            return score

        r = self.r
        for c in prefix:
            if c not in r:
                return 0
            r = r[c]
        
        return get_score(r)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)