# no need to sort
# just count O(n) with conditions
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        d = {}
        for k in nums:
            if k > n or k <= 0:
                return False
            if k not in d:
                d[k] = 0
            d[k] += 1
            if k != n and d[k] > 1:
                return False
            elif k == n and d[k] > 2:
                return False
        return True