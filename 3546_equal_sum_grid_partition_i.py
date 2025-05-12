# fairly easy with prefix-sum
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row_sum = list(accumulate(sum(r) for r in grid))
        if row_sum[-1] % 2:
            return False
        if (row_sum[-1] // 2) in row_sum:
            return True
        col_sum = list(accumulate(sum(r) for r in zip(*grid)))
        return (row_sum[-1] // 2) in col_sum