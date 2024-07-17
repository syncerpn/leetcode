# this solution is applied to #3097 as well
# bitwise or is similar to addition
# with positive num, removing the element from subarray results in decrease of or of the whole array
# so we can use sliding window for such problem
# the main challenge is that we cannot easily undo bitwise or, unlike what we can do with addition
# therefore, we need a bit counter to keep track of the result after removing an element from the subarray
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bit_counter = [0] * 32
        i, j = 0, 0
        r = len(nums) + 1
        x = 0
        # sliding windows inclusive range [i,j]
        # we increase j until reaching at least k
        for j in range(len(nums)):
            for b in range(32):
                bit_counter[b] += (nums[j] & (1 << b)) >> b
            x |= nums[j]
            # then try to decrease i to minimize the window until we fail k
            while x >= k and i <= j:
                r = min(r, j - i + 1)
                x = 0
                for b in range(32):
                    bit_counter[b] -= (nums[i] & (1 << b)) >> b
                    x |= (bit_counter[b] > 0) << b
                i += 1
        return r if r <= len(nums) else -1