# number of moves equals distance from an "1" ball to its next position
# so we just track that next position an "1" ball should go to
class Solution:
    def minimumSteps(self, s: str) -> int:
        l, ans = 0, 0
        for i, c in enumerate(s):
            if c == "0":
                ans += i - l
                l += 1
        return ans