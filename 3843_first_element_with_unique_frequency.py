# easy
class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        C = Counter(nums)
        F = Counter(C.values())
        U = set([i for i in F if F[i] == 1])
        if U:
            for a in nums:
                if C[a] in U:
                    return a
        return -1