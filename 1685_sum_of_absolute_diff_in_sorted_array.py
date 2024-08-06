# prefix sum
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        p = 0
        n = len(nums)
        ans = []
        for i in range(n):
            q = nums[i]
            ans.append(s - 2*p - q*(n - 2*i))
            p += q
        return ans