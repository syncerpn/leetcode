# monostack
class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        ans = 0
        s = []
        d = Counter()
        for a in nums:
            while s and s[-1] > a:
                d[s.pop()] -= 1
            ans += len(s) - d[a]
            s.append(a)
            d[a] += 1
        return ans
