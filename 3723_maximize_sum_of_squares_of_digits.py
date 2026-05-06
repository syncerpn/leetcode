# easy
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum / num > 9:
            return ""
        
        ans = []
        while num > 0:
            m = min(sum, 9)
            sum -= m
            ans.append(m)
            num -= 1
        return "".join(list(map(str, ans)))