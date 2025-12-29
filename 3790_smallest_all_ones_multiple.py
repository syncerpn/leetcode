# math
# same as #1015
# is existed, the number of 1s should be at most k
class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0: return -1
        r = 0
        for n in range(1, k + 1):
            r = (r * 10 + 1) % k
            if not r: return n
        