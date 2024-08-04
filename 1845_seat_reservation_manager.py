# same as #2336 infinite set
# we actually dont need to care about n
class SeatManager:

    def __init__(self, n: int):
        self.d = deque()
        self.r = 1
        

    def reserve(self) -> int:
        if self.d:
            return self.d.popleft()
        ans = self.r
        self.r += 1
        return ans
        

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.r - 1:
            self.r -= 1
            while self.d:
                if self.d[-1] != self.r - 1:
                    break
                self.r -= 1
                self.d.pop()
        elif seatNumber < self.r - 1:
            i = bisect_left(self.d, seatNumber)
            if i == len(self.d):
                self.d.append(seatNumber)
            elif self.d[i] != seatNumber:
                self.d.insert(i, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)