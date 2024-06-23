# need to iterate over all pairs
# the other two elements can be searched with two pointers
# probably O(N^3) time complexity
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums = sorted(nums)
        n = len(nums)
        results = set()

        for i in range(n-3):
            for j in range(i+1, n-2):
                d = target - nums[i] - nums[j]
                l = j+1
                r = n-1
                while r > l:
                    if nums[l] + nums[r] == d:
                        results.add(tuple([nums[i], nums[j], nums[l], nums[r]]))
                    if nums[l] + nums[r] > d:
                        r -= 1
                    else:
                        l += 1
        return results