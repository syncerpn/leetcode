# it is subsequence, so order does not matter
# turns out we can just sort then greedily group
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        p = nums[0]
        c = 1
        for n in nums[1:]:
            if n - p > k:
                c += 1
                p = n
        return c