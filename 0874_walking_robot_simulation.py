# just simulate every small step in a big step
# and check obstable with hash table
# because the number of step is fairly small 1 <= c <= 9
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = 0
        dx, dy = 0, 1
        rx = ry = 0
        obstacles = {(x, y) for x, y in obstacles}
        for c in commands:
            if c == -2:
                dx, dy = -dy, dx
            elif c == -1:
                dx, dy = dy, -dx
            else:
                for _ in range(c):
                    if (rx + dx, ry + dy) in obstacles:
                        break
                    rx, ry = rx + dx, ry + dy
                ans = max(ans, rx*rx+ry*ry)
        return ans

# this solution is for very large walking steps
# and of course, not starting inside an obstacle
# which is pretty much stupid
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = 0
        n = len(obstacles)
        
        dx, dy = 0, 1
        def turn(c, dx, dy):
            if c == -2:
                return -dy, dx
            elif c == -1:
                return dy, -dx
            return dx, dy
        
        obstacles_x = sorted(obstacles)
        obstacles_y = sorted([[y, x] for x, y in obstacles])

        rx = ry = 0

        for c in commands:
            if c < 0:
                dx, dy = turn(c, dx, dy)
            else:
                if dy == 0:
                    if dx > 0:
                        i = bisect.bisect_left(obstacles_y, [ry, rx])
                        rx += dx * c
                        if i < n and obstacles_y[i][0] == ry:
                            rx = min(rx, obstacles_y[i][1]-1)
                        
                    elif dx < 0:
                        i = bisect.bisect_right(obstacles_y, [ry, rx])
                        rx += dx * c
                        if i > 0 and obstacles_y[i-1][0] == ry:
                            rx = max(rx, obstacles_y[i-1][1]+1)

                elif dx == 0:
                    if dy > 0:
                        i = bisect.bisect_left(obstacles_x, [rx, ry])
                        ry += dy * c
                        if i < n and obstacles_x[i][0] == rx:
                            ry = min(ry, obstacles_x[i][1]-1)

                    elif dy < 0:
                        i = bisect.bisect_right(obstacles_x, [rx, ry])
                        ry += dy * c
                        if i > 0 and obstacles_x[i-1][0] == rx:
                            ry = max(ry, obstacles_x[i-1][1]+1)
                
                ans = max(ans, ry*ry+rx*rx)
        
        return ans