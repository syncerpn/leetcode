# nothing special than bitcount
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        B = [0] * 32
        for n in nums:
            i = 0
            while n:
                B[i] += n & 1
                n >>= 1
                i += 1
        
        r = 0
        for i in range(32):
            r |= (B[i] >= k) << i
        return r