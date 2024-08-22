# using prefix and suffix product
# no division
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = []
        t = 1
        for n in nums:
            p.append(t)
            t *= n
        q = []
        t = 1
        for n in nums[::-1]:
            q.append(t)
            t *= n
        
        return [p[i] * q[-1-i] for i in range(len(nums))]

# reduced to two pass and O(1) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        t = 1
        for n in nums:
            ans.append(t)
            t *= n

        t = 1
        for i in range(len(nums)-1,-1,-1):
            n = nums[i]
            ans[i] *= t
            t *= n
        
        return ans