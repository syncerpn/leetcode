# single-pass
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        c, d = [tops[0], bottoms[0]]
        tc, bc, td, bd = 0, 0, 0, 0
        for a, b in zip(tops, bottoms):
            if c != a and c != b:
                c = 0
            else:
                tc += c == a
                bc += c == b
            
            if d != a and d != b:
                d = 0
            else:
                td += d == a
                bd += d == b
            
            if c == 0 and d == 0:
                return -1

        if c > 0:
            return min(tc, bc, n-tc, n-bc)
        return min(td, bd, n-td, n-bd)
        
        