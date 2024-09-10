# binary search for timestamp retrieval
# pretty fast
class TimeMap:

    def __init__(self):
        self.c = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.c:
            self.c[key] = {"t": [], "v": []}
        self.c[key]["t"].append(timestamp)
        self.c[key]["v"].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.c:
            return ""
        i = bisect.bisect(self.c[key]["t"], timestamp)
        if i == 0:
            return ""
        return self.c[key]["v"][i-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)