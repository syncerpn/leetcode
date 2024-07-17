# track lowest and second lowest prices
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        f = min(prices[0], prices[1])
        s = max(prices[0], prices[1])
        for n in prices[2:]:
            if n < f:
                f, s = n, f
            elif n == f or n < s:
                s = n
        l = money - f - s
        return l if l >= 0 else money