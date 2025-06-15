# actually fairly easy
# stack solution for the concept
# we simply keep track of the min and max possible last element
# as we iterate over those can be the first elements
class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        ans = -inf
        neg, pos = [], []
        for i in range(len(nums) - m + 1):
            if not neg or neg[-1] > nums[~i]:
                neg.append(nums[~i])
            else:
                neg.append(neg[-1])
            
            if not pos or pos[-1] < nums[~i]:
                pos.append(nums[~i])
            else:
                pos.append(pos[-1])
            
        for i in range(len(nums) - m + 1):
            ans = max(ans, nums[i] * neg[~i])
            ans = max(ans, nums[i] * pos[~i])
        return ans

# simply O(1) space for that tracking part
# this time, we iterate over those possible last elements
class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        mi, ma = nums[0], nums[0]
        ans = -inf

        for i in range(m - 1, len(nums)):
            ma = max(ma, nums[i - m + 1])
            mi = min(mi, nums[i - m + 1])
            ans = max(ans, mi * nums[i], ma * nums[i])
        return ans