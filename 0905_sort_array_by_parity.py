# two-pointer, one-pass, same direction
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] % 2:
                break
            i += 1

        j = i + 1
        while j < len(nums):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        
        return nums

# or two-pointer, one-pass, opposite direction
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] % 2 == 0:
                i += 1
            elif nums[j] % 2 == 1:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums