# quite a good problem
# it looks easy at first, then turns out to be quite complicated
# the best way to do it is to travel left to right then right to left to validate the maximum value we can obtain at each position
# we only need one peak at one index, decreasing to the two sides
# e.g. 0 1 2 3 4 7 5 4 3 1 0 0 0
# solved it myself, yet should revisit sometimes to make it concrete
class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        dp = [float(inf)] * n
        dp[0] = 0
        
        for i, a in restrictions:
            dp[i] = a

        for i in range(1, n):
            dp[i] = min(dp[i], dp[i-1] + diff[i-1])

        for i in range(n-2, -1, -1):
            dp[i] = min(dp[i], dp[i+1] + diff[i])
        
        return max(dp)

# optimize for runtime
# dont use min, use if
class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        dp = [float(inf)] * n
        dp[0] = 0
        
        for i, a in restrictions:
            dp[i] = a

        for i in range(1, n):
            t = dp[i-1] + diff[i-1]
            if t < dp[i]:
                dp[i] = t

        for i in range(n-2, -1, -1):
            t = dp[i+1] + diff[i]
            if t < dp[i]:
                dp[i] = t
        
        return max(dp)