# prefix sum is the thing
# make sure to save the remainder into dict for quick reference
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        acc = 0
        d = {0: -1}
        for i, n in enumerate(nums):
            acc = (acc + n) % k
            if acc not in d:
                d[acc] = i
            elif i - d[acc] >= 2:
                return True

        return False