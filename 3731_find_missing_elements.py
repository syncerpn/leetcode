# easy
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi, ma = min(nums), max(nums)
        s = set(nums)
        ans = []
        for a in range(mi, ma+1):
            if a not in s:
                ans.append(a)
                
        return ans