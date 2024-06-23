# using dict should be fine, O(N) space
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                if i - d[n] <= k:
                    return True
            d[n] = i
        return False