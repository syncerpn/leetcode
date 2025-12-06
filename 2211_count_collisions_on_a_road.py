# simulate it
# but maybe overcomplicated
class Solution:
    def countCollisions(self, directions: str) -> int:
        s, r = False, 0
        ans = 0
        for d in directions:
            if d == "L":
                if s:
                    ans += r
                    r = 0
                    ans += 1
            elif d == "S":
                s = True
                ans += r
                r = 0
            elif d == "R":
                s = True
                r += 1
        return ans

# simply count those are bounded
class Solution:
    def countCollisions(self, directions: str) -> int:
        return len(directions.lstrip("L").rstrip("R")) - directions.count("S")