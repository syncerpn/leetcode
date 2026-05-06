# optimal O(1) space
# pretty good
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = 0
        m = 0
        for i, a in enumerate(flips):
            m = max(m, a)
            if m == i + 1:
                ans += 1
        return ans