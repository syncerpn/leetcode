# a bit of math should solve it easily
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        n = (numRows - 1) * 2
        
        rows = [''] * numRows
        for i,c in enumerate(s):
            ri = min(i % n, n - i % n)
            rows[ri] += c
        
        return ''.join(rows)