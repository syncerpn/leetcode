# introduce bisect right to concat numbers, lol
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        t = [10 ** i for i in range(1, 6)]
        n = len(nums)
        r = 0
        for i in range((n + 1) // 2):
            j = n - 1 -i
            if i == j:
                r += nums[i]
            else:
                m = t[bisect_right(t, nums[j])]
                r += m * nums[i] + nums[j]
        return r