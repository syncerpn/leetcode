# easy
class RLEIterator:

    def __init__(self, encoding: List[int]):
        n = len(encoding) // 2
        self.V = []
        self.C = []
        for i in range(n):
            self.C.append(encoding[2*i])
            self.V.append(encoding[2*i+1])
        self.C = self.C[::-1]
        self.V = self.V[::-1]

    def next(self, n: int) -> int:
        while self.C and n > 0:
            if self.C[-1] < n:
                n -= self.C.pop()
                self.V.pop()
            else:
                self.C[-1] -= n
                n = 0
                break
        if n > 0:
            return -1
        return self.V[-1]
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)