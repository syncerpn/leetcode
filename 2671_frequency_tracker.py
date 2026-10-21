# lmao spaghetti
class FrequencyTracker:

    def __init__(self):
        self.d = {}
        self.f = {}

    def add(self, number: int) -> None:
        if number not in self.d:
            self.d[number] = 0
        self.d[number] += 1
        if self.d[number] > 1:
            self.f[self.d[number] - 1] -= 1
            if self.f[self.d[number] - 1] == 0:
                del self.f[self.d[number] - 1]
        if self.d[number] not in self.f:
            self.f[self.d[number]] = 0
        self.f[self.d[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.d:
            self.f[self.d[number]] -= 1
            if self.f[self.d[number]] == 0:
                del self.f[self.d[number]]
            self.d[number] -= 1
            if self.d[number] > 0:
                if self.d[number] not in self.f:
                    self.f[self.d[number]] = 0
                self.f[self.d[number]] += 1
            else:
                del self.d[number]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.f
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)