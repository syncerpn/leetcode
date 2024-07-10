# not very interesting problem though
class OrderedStream:

    def __init__(self, n: int):
        self.storage = [None] * n
        self.p = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.storage[idKey-1] = value
        r = []
        while self.p < len(self.storage):
            if self.storage[self.p]:
                r.append(self.storage[self.p])
                self.p += 1
            else:
                break
        return r


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)