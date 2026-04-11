# simple logic
class Robot:
    def __init__(self, width: int, height: int):
        self.D = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.p = 0
        self.initial_state = True
        self.w = width
        self.h = height
        self.mod = (width + height - 2) * 2
        self.milestone = {"East": (1, width-1), "North": (width, width+height-2), "West": (width+height-1, width*2+height-3)}
        self.i = 0

    def step(self, num: int) -> None:
        if num > 0:
            self.initial_state = False
        self.p = (self.p + num) % self.mod

    def getPos(self) -> List[int]:
        p = self.p
        if p < self.w:
            return (p, 0)
        p -= self.w - 1
        if p < self.h:
            return (self.w - 1, p)
        p -= self.h - 1
        if p < self.w:
            return (self.w - 1 - p, self.h - 1)
        p -= self.w - 1
        return (0, self.h - 1 - p)

    def getDir(self) -> str:
        if self.initial_state:
            return "East"
        for k in self.milestone:
            a, b = self.milestone[k]
            if a <= self.p <= b:
                return k
        return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()