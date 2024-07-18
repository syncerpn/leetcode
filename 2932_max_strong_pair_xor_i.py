# small constraints can be passed with sliding window
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        x = 0
        i = 0
        for j in range(1, len(nums)):
            while nums[i] + nums[i] < nums[j]:
                i += 1
            for k in range(i, j):
                x = max(x, nums[k] ^ nums[j])
        
        return x