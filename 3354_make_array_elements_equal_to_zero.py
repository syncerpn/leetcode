# the logic is fairly easy to breakdown and come up with a good solution
# simply, we want to find a point n == 0 while prefix and suffix sum at n
# is either the same or different by at most 1
# if it is the same, we can start at n and travel in both directions
# otherwise, we have to head for either the prefix or suffix sum whichever is higher
# also because all the elements are greater than zero
# we can early stop when the prefix sum is at least 2 unit larger than the suffix one
# good problem
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        s = sum(nums)
        o = 2 - (s % 2)
        l = 0
        ans = 0
        for n in nums:
            l += n
            d = (l << 1) - s
            if -1 <= d <= 1 and n == 0:
                ans += o
            elif d > 1:
                break
            
        return ans
