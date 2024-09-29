# easy
class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = None
        for n in nums:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            if ans is None or ans > s:
                ans = s
        return ans