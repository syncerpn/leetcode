# sorted set
class Router:

    def __init__(self, memoryLimit: int):
        self.n = memoryLimit
        self.d = {}
        self.q = deque()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if destination in self.d and (timestamp, source) in self.d[destination]:
            return False
        
        if len(self.q) == self.n:
            ss, dd, tt = self.q.popleft()
            self.d[dd].discard((tt, ss))

        if destination not in self.d:
            self.d[destination] = SortedSet()
        self.d[destination].add((timestamp, source))
        self.q.append((source, destination, timestamp))
        return True

    def forwardPacket(self) -> List[int]:
        if self.q:
            s, d, t = self.q.popleft()
            self.d[d].discard((t, s))
            return [s, d, t]
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.d:
            return 0
        l = self.d[destination].bisect_left((startTime, 0))
        r = self.d[destination].bisect_right((endTime, float("inf")))
        return r - l


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)