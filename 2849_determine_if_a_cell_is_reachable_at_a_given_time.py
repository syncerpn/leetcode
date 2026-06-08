# that edge case tricked me lol
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False
        return abs(fx-sx) <= t and abs(fy-sy) <= t