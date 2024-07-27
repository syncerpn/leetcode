# fairly easy with hash table
class UndergroundSystem:

    def __init__(self):
        self.p = {}
        self.s = {}
        self.c = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.p[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s, ts = self.p[id]
        d, td = stationName, t
        if s not in self.s:
            self.s[s] = {}
            self.c[s] = {}
        if d not in self.s[s]:
            self.s[s][d] = 0
            self.c[s][d] = 0
        self.s[s][d] += td - ts
        self.c[s][d] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.s[startStation][endStation] / self.c[startStation][endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)