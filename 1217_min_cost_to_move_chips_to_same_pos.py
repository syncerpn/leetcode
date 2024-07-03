# counting
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        co = 0
        ce = 0
        for i in position:
            co += i % 2
            ce += (i % 2 == 0)
        return min(co, ce)