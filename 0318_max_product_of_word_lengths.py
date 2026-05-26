# easy
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = defaultdict(set)
        for w in words:
            d[w] = set(w)
        
        ans = 0
        for a in words:
            for b in words:
                if d[a] - d[b] == d[a]:
                    ans = max(ans, len(a) * len(b))
        return ans