# easy
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        dp = [False] * (bound + 1)
        xx = 1
        while xx <= bound:
            yy = 1
            while yy <= bound:
                if xx + yy > bound:
                    break
                dp[xx + yy] = True
                if y > 1:
                    yy *= y
                else:
                    break
            if x > 1:
                xx *= x
            else:
                break
        return [i for i in range(bound+1) if dp[i]]