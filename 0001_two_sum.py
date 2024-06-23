# iterate through the list, add the number to a hash table
# the check whether its counterpart is already in the hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, n in enumerate(nums):
            if target - n in nums_dict:
                return [i, nums_dict[target-n]]
            nums_dict[n] = i
        
        return []