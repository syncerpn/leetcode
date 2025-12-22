# easy
# optimal implementation may not need sorting
# may try optimizing it later
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {0: [], 1: [], 2: []}
        for a in nums:
            d[a % 3].append(a)
        
        for r in d:
            d[r].sort()
        ans = 0
        for r in d:
            if len(d[r]) >= 3:
                ans = max(ans, sum(d[r][-3:]))
        
        if d[0] and d[1] and d[2]:
            ans = max(ans, d[0][-1] + d[1][-1] + d[2][-1])
        return ans