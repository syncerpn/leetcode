# turns out, a and b should be that a <= b <= 2*a
# more like a codeforce problem
# where math is required lol
class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        s = sorted([abs(a) for a in nums])
        l, n = 0, len(s)
        ans = 0
        for r in range(n):
            while s[r] > s[l] * 2:
                l += 1
            ans += r - l
        return ans