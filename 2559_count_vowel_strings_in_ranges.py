# prefix sum
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        p = [0]
        V = set(["a", "e", "i", "o", "u"])
        for w in words:
            p.append(p[-1] + (w[0] in V and w[-1] in V))
        ans = []
        for l, r in queries:
            ans.append(p[r+1]-p[l])
        return ans