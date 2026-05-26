# greedy
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p: (p[1], p[0]))
        p = -inf
        ans = 0
        for a, b in pairs:
            if a > p:
                p = b
                ans += 1
        return ans