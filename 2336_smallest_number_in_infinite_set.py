# one pointer to in-range set
# one deque for addback chaotic discete numbers
# pop: O(1)
# addback: average O(log(len(self.d))) with binary search
class SmallestInfiniteSet:

    def __init__(self):
        self.d = deque()
        self.r = 1

    def popSmallest(self) -> int:
        if self.d:
            return self.d.popleft()
        ans = self.r
        self.r += 1
        return ans

    def addBack(self, num: int) -> None:
        if num == self.r - 1:
            self.r -= 1
            while self.d:
                if self.d[-1] != self.r - 1:
                    break
                self.r -= 1
                self.d.pop()
        elif num < self.r - 1:
            i = bisect_left(self.d, num)
            if i == len(self.d):
                self.d.append(num)
            elif self.d[i] != num:
                self.d.insert(i, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)