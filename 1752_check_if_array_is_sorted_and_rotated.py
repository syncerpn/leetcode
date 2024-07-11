# count the number of decreasing slopes
# if the array is sorted and rotated
# it should have at most 1 such slope
# (it might have 0, because nums may contain duplicated elements)
class Solution:
    def check(self, nums: List[int]) -> bool:
        d = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                d += 1
                if d > 1:
                    return False
        
        return True
