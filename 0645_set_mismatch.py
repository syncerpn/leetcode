# use xor and bit vector
# single-pass O(n) time O(n) space
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x = 0
        c = [False] * len(nums)
        e = 0
        for i, n in enumerate(nums):
            x ^= (i+1)
            if c[n-1]:
                e = n
            else:
                c[n-1] = True
                x ^= n
        return [e, x]