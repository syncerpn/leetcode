# deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.v = value
        self.k = k
        self.s = collections.deque()
        self.f = 0

    def consec(self, num: int) -> bool:
        f = num == self.v
        self.s.append(f)
        if not f:
            self.f += 1
        if len(self.s) > self.k:
            f = self.s.popleft()
            if not f:
                self.f -= 1
        return len(self.s) == self.k and self.f == 0


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)