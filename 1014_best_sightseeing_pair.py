# one pass O(n) and O(1) space
# save the best score so far
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        m, s = -float("inf"), -float("inf")
        n = len(values)
        for i, v in enumerate(values):
            if i == 0:
                m = v - n
            else:
                s = max(s, m + v + n - i)
                m = max(m, v - (n - i))
        return s

# this answer by lee215 has the same idea as above,
# yet might be easier to understand
# record the best so far, and when it comes to the next
# the best is decreased by 1 because its distance to the current is increased by 1
# in other words, it got decayed while iterating
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cur = res = 0
        for v in values:
            res = max(res, cur + v)
            cur = max(cur, v) - 1
        return res