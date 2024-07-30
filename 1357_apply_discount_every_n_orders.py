# fairly easy
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.i = 0
        self.n = n
        self.d = discount
        self.p = {p: c for p, c in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        for i, k in zip(product, amount):
            total += self.p[i] * k
        self.i = (self.i + 1) % self.n
        if self.i == 0:
            total = total * (100 - self.d) / 100
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)