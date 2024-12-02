# math and count
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c = 0
        ans = 0
        for n in nums:
            if n == 0:
                c += 1
            else:
                ans += c * (c+1) // 2
                c = 0
        ans += c * (c+1) // 2
        return ans