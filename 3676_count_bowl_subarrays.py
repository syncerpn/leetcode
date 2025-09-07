# for every element
# put its index into a decreasing monostack
# at some points, when the s has something
# and the element at index stored at top of the stack < the current element
# there is a potential subarray formed by that top of stack and the current element
# if the length >= 3
# so we will pop the stack
# until we get a mono decreasing stack again with the current element pushed into the stack
class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        ans = 0
        s = []
        for r, a in enumerate(nums):
            while s and nums[s[-1]] <= a:
                l = s.pop()
                if r - l + 1 >= 3:
                    ans += 1
            if s and r - s[-1] + 1 >= 3:
                ans += 1
            s.append(r)
        return ans