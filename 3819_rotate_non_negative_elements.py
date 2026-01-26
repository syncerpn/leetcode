# easy
class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        s = []
        for i, a in enumerate(nums):
            if a >= 0:
                s.append((i, a))
        m = len(s)
        if m > 0:
            k %= m
            for j, (i, a) in enumerate(s):
                nums[s[(j - k) % m][0]] = a
        return nums