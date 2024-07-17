# find index of 1 and n
# move them towards their desired pos
# if index of 1 is after n
# we can reduce the number of ops by 1 because they will encounter each other on the way
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        f = nums.index(1)
        l = nums.index(n)
        return f + (n - 1 - l) - (l < f)