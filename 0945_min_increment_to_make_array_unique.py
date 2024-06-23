# sorting then check for unique O(nlogn)
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums = sorted(nums)
        m = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                p = nums[i-1] + 1 - nums[i]
                m += p
                nums[i] += p
        return m

# or union-find O(n)??
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        root = {}
        def find(x):
            root[x] = find(root[x] + 1) if x in root else x
            return root[x]
        return sum(find(a) - a for a in A)