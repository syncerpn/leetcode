# O(n2) works
# any better?
class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:        
        n = len(nums)
        ans = 0
        for i in range(n):
            d = set()
            s = 0
            for j in range(i, n):
                d.add(nums[j])
                s += nums[j]
                if s in d:
                    ans += 1

        return ans