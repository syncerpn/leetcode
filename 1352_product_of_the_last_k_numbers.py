# this is easy, but the constraints need to include that
# at any point, the product of all continuous non-zeros so far should not exceed the bitwidth
# this is an important point for this O(1) solution to work
class ProductOfNumbers:

    def __init__(self):
        self.q = []
        self.p = 1

    def add(self, num: int) -> None:
        if num:
            self.q.append(self.p)
            self.p *= num
        else:
            self.p = 1
            self.q = []

    def getProduct(self, k: int) -> int:
        if k > len(self.q):
            return 0
        return self.p // self.q[-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)