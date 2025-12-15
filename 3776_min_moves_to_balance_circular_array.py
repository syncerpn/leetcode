# at most one negative
# lol
# looks like many people also read it as "at least one negative"
# just like i did
class Solution:
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance) < 0:
            return -1
        l, r, k, n = 0, 0, 0, len(balance)
        for i, a in enumerate(balance):
            if a < 0:
                l, r, k = i, i, a
                break
        
        ans = 0
        m = 1
        while k < 0:
            l, r = (l - 1) % n, (r + 1) % n
            d = balance[l] + balance[r]
            k += d
            if k < 0:
                ans += m * d
            else:
                ans += m * (d - k)
                break
            m += 1
        return ans
