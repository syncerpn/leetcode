# interval problem, or linesweep
# we are free to choose which index to decrease
# so just make sure we have enough (at most what) to reduce them to zeros
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        changes = [0] * n
        for l, r in queries:
            changes[l] += 1
            if r + 1 < n:
                changes[r+1] -= 1
        
        p = 0
        for a, b in zip(nums, changes):
            p += b
            if p < a:
                return False
        return True