# try to start at different positions
# if at some points the total current gas becomes less than 0
# that starting point is invalid
# so we try the next starting point from the current point
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s, t = 0, 0
        ans = 0
        for i in range(len(gas)):
            d = gas[i] - cost[i]
            s += d
            t += d
            if t < 0:
                t = 0
                ans = i + 1
        return -1 if s < 0 else ans

# further explanation why we dont need to go back
# and check all the points from the last one to the next possible one
# 1. we can only start at a point i if gas[i] - cost[i] >= 0
# 2. if we fail at a point j, and if we start from any point in {i+1, i+2, ..., j-1}
# we will just have fewer gas in our car, because of (1) that gas[i] - cost[i] >= 0
# meaning that we will still fail at point j due to having not enough gas once reaching that point