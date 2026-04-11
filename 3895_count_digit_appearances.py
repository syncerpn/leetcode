# easy
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        ans = 0
        for a in nums:
            while a > 0:
                if a % 10 == digit:
                    ans += 1
                a //= 10
        return ans