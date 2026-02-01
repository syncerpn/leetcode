# an easy q3
class RideSharingSystem:

    def __init__(self):
        self.R = deque()
        self.D = deque()
        self.Rs = set()

    def addRider(self, riderId: int) -> None:
        self.R.append(riderId)
        self.Rs.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.D.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if self.D:
            while self.R:
                r = self.R.popleft()
                if r in self.Rs:
                    self.Rs.discard(r)
                    d = self.D.popleft()
                    return d, r
        return -1, -1

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.Rs:
            self.Rs.discard(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)