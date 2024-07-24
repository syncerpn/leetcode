# my design with fixed-length array at init time
# and delayed increment
class CustomStack:

    def __init__(self, maxSize: int):
        self.m = maxSize
        self.i = -1
        self.s = [0] * maxSize
        self.d = [0] * maxSize

    def push(self, x: int) -> None:
        self.update()
        if self.i < self.m - 1:
            self.i += 1
            self.s[self.i] = x

    def pop(self) -> int:
        self.update()
        if self.i >= 0:
            r = self.s[self.i]
            self.i -= 1
            return r
        return -1

    def increment(self, k: int, val: int) -> None:
        self.d[0] += val
        if k < self.m:
            self.d[min(k, self.i+1)] -= val

    def update(self):
        v = 0
        for i in range(self.m):
            if i <= self.i:
                v += self.d[i]
                self.s[i] += v
            self.d[i] = 0

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


# improved design which true lazy update O(1)
# the point is to propage the update on pop to previous element in the stack
class CustomStack:

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.inc: return -1
        if len(self.inc) > 1:
            # update propagation
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)