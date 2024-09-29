# using list is ok
class MyCircularDeque:

    def __init__(self, k: int):
        self.i, self.k = 0, k
        self.f, self.b = 0, 0
        self.d = [-1] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.isEmpty():
            self.f = (self.f - 1) % self.k
        self.d[self.f] = value
        self.i += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.isEmpty():
            self.b = (self.b + 1) % self.k
        self.d[self.b] = value
        self.i += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.d[self.f] = -1
        self.i -= 1
        if self.isEmpty():
            self.f, self.b = 0, 0
        else:
            self.f = (self.f + 1) % self.k
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.d[self.b] = -1
        self.i -= 1
        if self.isEmpty():
            self.f, self.b = 0, 0
        else:
            self.b = (self.b - 1) % self.k
        return True

    def getFront(self) -> int:
        return self.d[self.f]

    def getRear(self) -> int:
        return self.d[self.b]

    def isEmpty(self) -> bool:
        return self.i == 0

    def isFull(self) -> bool:
        return self.i == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()