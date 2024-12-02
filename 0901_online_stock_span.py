# monostack
class StockSpanner:

    def __init__(self):
        self.h = []
        self.n = 0

    def next(self, price: int) -> int:
        ans = 1
        while self.h:
            s, i = self.h[-1]
            if price >= s:
                self.h.pop()
            else:
                ans = self.n - i
                self.h.append((price, self.n))
                self.n += 1
                break
        else:
            self.h.append((price, self.n))
            self.n += 1
            ans = self.n
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# cleaner solution with amortized O(1) by lee
# actually quite similar to my solution
class StockSpanner:
    
    def __init__(self):
        self.stack = []

    def next(self, price):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)