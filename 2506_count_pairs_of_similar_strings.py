# count sorted set
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words = [sorted(list(set(word))) for word in words]
        d = {}
        for word in words:
            w = "".join(word)
            if w not in d:
                d[w] = 0
            d[w] += 1
        
        c = 0
        for w in d:
            c += d[w] * (d[w] - 1) // 2
        return c