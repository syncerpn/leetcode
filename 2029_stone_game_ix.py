# need revisit
# math like
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt0 = cnt1 = cnt2 = 0
        for a in stones:
            t = a % 3
            if t == 0:
                cnt0 += 1
            elif t == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt0 % 2 == 0:
            return cnt1 >= 1 and cnt2 >= 1
        return cnt1 - cnt2 > 2 or cnt2 - cnt1 > 2
        