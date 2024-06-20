# just need to check the region with most overlapping, which always starting from (0, 0)
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        im, jm = ops[0]
        for i, j in ops:
            im = min(i, im)
            jm = min(j, jm)
        
        return im * jm