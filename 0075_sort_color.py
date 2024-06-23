# this is trivial: counts number of 1 and 2
# then reconstruct the array
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j, k = 0, 0
        for i, n in enumerate(nums):
            if n == 0:
                j += 1
            if n == 1:
                k += 1
        
        k += j
        for i, _ in enumerate(nums):
            if i < j:
                nums[i] = 0
            elif i < k:
                nums[i] = 1
            else:
                nums[i] = 2

# but this is much better; true one-pass (Dutch national flag algorithm)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1