# kinda brute force with set
# works with small constraints
# but you know, there is a follow-up #2916
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(len(nums)):
            s = set()
            s.add(nums[i])
            c = 1
            for j in range(i, len(nums)):
                if nums[j] not in s:
                    c += 1
                    s.add(nums[j])
                result += c * c
        
        return result