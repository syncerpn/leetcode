# 2nd question yet killed me hours
# we need to choose 2 distinct machines
# so lets try choosing one, then searching for the best other
# to do so, we need to sort and record the best capacity with cost < budget - first cost
# we can do this with kind of monostack
# or likely, prefix max as in the hints
# dont worry about duplicates/missing out
# we check for picking duplicates
# and missing out will never happen because assume a + b to be the answer
# we will try both picking a first and then b and picking b first and then a
# so prefix max duplicating a will be ruled out
# while picking b first then a will also leads to the right answer
class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        Q = sorted([(co, ca, i) for i, (co, ca) in enumerate(zip(costs, capacity))])
        n = len(Q)
        dp = []
        for co, ca, i in Q:
            if not dp or dp[-1][1] < ca:
                dp.append((co, ca, i))
        
        ans = 0
        for co, ca, i in Q:
            if co < budget:
                ans = max(ans, ca)
            jj = bisect.bisect_right(dp, (budget - co, -1, -1))
            jj -= 1
            if jj >= 0 and dp[jj][2] != i:
                ans = max(ans, ca + dp[jj][1])

        return ans
