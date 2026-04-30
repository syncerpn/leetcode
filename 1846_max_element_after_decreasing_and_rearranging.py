# easy
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ma = 0
        for a in arr:
            ma = min(a, ma + 1)
        return ma