# dp
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[inf] * n for _ in range(3)]
        for i, o in enumerate(obstacles):
            if i == 0:
                dp[0][0] = 1
                dp[1][0] = 0
                dp[2][0] = 1
                continue
            for j in range(3):
                if j == o - 1:
                    continue
                for k in range(3):
                    if k == o - 1:
                        continue
                    dp[j][i] = min(dp[j][i], dp[k][i-1] + int(k != j))
        return min(dp[0][n-1], dp[1][n-1], dp[2][n-1])

# may optimize to O(1) space
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [1, 0, 1]
        for a in obstacles:
            if a:
                dp[a - 1] = inf
            for i in range(3):
                if a != i + 1:
                    dp[i] = min(dp[i], dp[(i + 1) % 3] + 1, dp[(i + 2) % 3] + 1)
        return min(dp)

# to further better runtime
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        # track currently available lanes (start at lane 2)
        available = {2}
        jumps = 0
        prev_obstacle = 0 # Obstacle at previous position
        
        for obs in obstacles:
            if obs != 0:
                # if only lane left is blocked, must side jump
                if obs in available and len(available) == 1:
                    available = {1, 2, 3}  # reset to all lanes
                    available.discard(prev_obstacle)  # can't land on previous obstacle
                    jumps += 1
                available.discard(obs)   # remove current blocked lane
            prev_obstacle = obs
        
        return jumps