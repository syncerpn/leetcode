# at most one break is allowed
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = []
        j = -1
        for i, (a, b) in enumerate(pairwise(nums)):
            d = b - a
            p.append(d)
            if d < 0:
                if j != -1:
                    return False
                j = i
        
        if j == -1:
            return True
        if j == 0 or j == len(p) - 1:
            return True
        return (p[j-1] + p[j] >= 0) or (p[j] + p[j+1] >= 0)

# a better implementation with better space
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        c = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                c += 1
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return c < 2