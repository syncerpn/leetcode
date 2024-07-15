# just use intersection
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        s = set(nums[0])
        for n in nums[1:]:
            s = s.intersection(set(n))
        return sorted(list(s))