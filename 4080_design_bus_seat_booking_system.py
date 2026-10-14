# easy, super easy for a q3
class BusBooking:
    def __init__(self, n: int):
        self.S = {k: [0] * n for k in "ABCD"}
        self.c = 0
        self.t = 0
        self.D = {"A"}

    def toggle(self, seat: str) -> None:
        k = seat[0]
        i = int(seat[1:]) - 1
        if self.S[k][i] > 0:
            self.c -= 1
            self.t -= self.S[k][i]
            self.S[k][i] = 0
        else:
            self.c += 1
            if k == "B" or k == "C":
                self.t += 1
                self.S[k][i] = 1
            elif k == "A":
                if self.S["B"][i] > 0:
                    self.t += 3
                    self.S[k][i] += 3
                else:
                    self.t += 1
                    self.S[k][i] += 1
            elif k == "D":
                if self.S["C"][i] > 0:
                    self.t += 3
                    self.S[k][i] += 3
                else:
                    self.t += 1
                    self.S[k][i] += 1

    def getTotalTime(self) -> int:
        return self.t

    def getMinTime(self) -> int:
        return self.c


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()