# easy
class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        p = 0
        S = [0, 0]
        for i, a in enumerate(nums):
            if a % 2:
                p = 1 - p
            if i % 6 == 5:
                p = 1 - p
            S[p] += a
        return S[0] - S[1]
