# whether we rearrange them or not?
# cost should be min of those two
class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        p = sum(abs(a-b) for a, b in zip(arr, brr))
        q = k + sum(abs(a-b) for a, b in zip(sorted(arr), sorted(brr)))
        return min(p, q)