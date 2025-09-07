# dont need anything complicated
# just find the farthest character away from "a"
class Solution:
    def minOperations(self, s: str) -> int:
        A = {a: i for i, a in enumerate("bcdefghijklmnopqrstuvwxyza")}
        return max(A["a"] - A[c] for c in s)