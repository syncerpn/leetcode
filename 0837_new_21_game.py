# dp + sliding window
# we use dynamic programming with a sliding window to efficiently calculate probabilities.
# let dp[i] represent the probability of reaching exactly i points.
# initially, dp[0] = 1 since alice always starts with 0 points.
# for every next score i, its probability comes from all possible scores
# that could have led to it in one draw,
# i.e., dp[i] = (dp[i-1] + dp[i-2] + ... + dp[i-maxPts]) / maxPts.
# directly computing this sum would be too slow, so we maintain a running total called windowsum, which keeps track of the last maxPts probabilities.
# at each step:
# we compute prob = windowsum / maxPts as the probability for i.
# if i < k, alice can still draw more, so we add this probability into windowsum.
# if i >= k, alice stops drawing, so we add this probability to the final result.
# to maintain the window size, if i >= maxPts, we remove the oldest probability from windowsum.
# by repeating this process up to n, we efficiently compute the result without recalculating large sums repeatedly.
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * maxPts
        dp[0] = 1.0

        w = 1.0
        ans = 0.0

        for i in range(1, n + 1):
            p = w / maxPts
            if i < k:
                w += p
            else:
                ans += p
            
            if i >= maxPts:
                w -= dp[i % maxPts]
            
            dp[i % maxPts] = p
        
        return ans