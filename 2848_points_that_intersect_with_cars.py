# line sweep
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        p = [0] * 101
        c = 0
        for a, b in nums:
            p[a-1] += 1
            p[b] -= 1
        k = 0
        for i in p:
            k += i
            if k > 0:
                c += 1
        return c