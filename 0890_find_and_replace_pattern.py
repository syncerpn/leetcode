# trivial solution with map
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(s, r):
            d = {}
            u = set()
            for a, b in zip(s, r):
                if a not in d:
                    if b in u:
                        return False
                    d[a] = b
                    u.add(b)
                elif d[a] != b:
                    return False
            return True
        return [w for w in words if match(w, pattern)]

# or more optimized one with normalized words
# may use numbers instead of alphabets
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def normalize(s):
            d = {}
            ALPHABETS = list("abcdefghijklmnopqrstuvwxyz")
            r = ""
            for c in s:
                if c not in d:
                    d[c] = ALPHABETS.pop()
                r += d[c]
            return r
        
        p = normalize(pattern)
        return [w for w in words if normalize(w) == p]