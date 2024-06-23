# modify in-place, moving numbers to their corresponding index
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            n = nums[i]
            if n != i+1:
                if nums[i] != nums[n-1]:
                    nums[i] = nums[n-1]
                    nums[n-1] = n
                    continue
            i += 1
        res = []
        for i, n in enumerate(nums):
            if n != i+1:
                res.append(i+1)

        return res

# O(n) time, O(1) space; how beautiful
# an example of how you store extra information with minimal modification
# by marking the existing numbers with their negative
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            nums[abs(n)-1] = -abs(nums[abs(n)-1])
        
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)

        return res