# just take the smallest positive one every step
# so the number of turns equal to length set of positive elements in nums
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        s.discard(0)
        return len(s)