# return sorted index
# quite complicated to achieve O(nlogn)
# but its beautiful in the end
# O(n) can be achieved with bucket sort, yet not generalizable to unbounded range
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        indices = list(range(n))
        indices.sort(key=lambda x: nums[x])
        rank = [0] * n
        for i, n in enumerate(indices):
            if nums[n] == nums[indices[i-1]]:
                rank[n] = rank[indices[i-1]]
            else:
                rank[n] = i
        return rank