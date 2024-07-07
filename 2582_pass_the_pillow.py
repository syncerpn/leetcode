# calculate how many passes have been done
# one pass is going in one direction until the end
# if number of passes is even, the current direction is ascending
# else descending
# calculate person index according to this
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        return n - time % (n - 1) if (time // (n - 1)) % 2 else 1 + time % (n - 1)