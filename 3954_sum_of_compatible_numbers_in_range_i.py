# easy, with brute-force
# let's see what is offered in the second version
class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        ans = 0
        for x in range(max(1, n - k), n + k + 1):
            if x & n == 0:
                ans += x
        return ans