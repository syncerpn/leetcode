# two lazy optimizing this
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            s = str(n)
            m = max(s)
            if m not in d:
                d[m] = [n]
            else:
                d[m].append(n)
        
        s_max = -1
        for m in d:
            if len(d[m]) > 1:
                s_max = max(s_max, sum(sorted(d[m])[-2:]))
        return s_max