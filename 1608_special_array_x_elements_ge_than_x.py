# sort and binary search
# not so clean, but covers well the concept
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        l = 0
        r = n
        while l <= r:
            i = (l + r) // 2
            if nums[i] >= i + 1:
                if i == n - 1:
                    return n                
                if nums[i+1] < i + 1:
                    return i + 1
                else:
                    l = i + 1
            else:
                r = i - 1
        
        return -1
