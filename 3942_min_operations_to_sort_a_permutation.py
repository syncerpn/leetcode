# codeforce type of prob lol
# guess they want to make leetcode more competitive
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        z = 0
        for i in range(n):
            if nums[i] != (nums[i-1] + 1) % n:
                break
            if nums[i] == 0:
                z = i
        else:
            return min(z, 2 + n - z)
        
        for i in range(n):
            if nums[i] != (nums[i-1] - 1) % n:
                break
            if nums[i] == 0:
                z = i
        else:
            return 1 + min(n - 1 - z, 1 + z)
        
        return -1