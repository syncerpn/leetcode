# use segment add, similar to #1992, but much simpler
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def segment(row):
            s, c = set(), 0
            x, l = 0, 0
            for i, k in enumerate(row + ["."]):
                if k == "X":
                    l += 1
                else:
                    if l == 1:
                        s.add(x)
                    elif l > 1:
                        c += 1
                    x, l = i + 1, 0
            return s, c
        
        def add(s, a):
            r, c = set(), 0
            for j in s:
                if j not in a:
                    c += 1
            for i in a:
                if i in s or i not in r:
                    r.add(i)
            return r, c

        acc = {}
        c = 0
        for r, row in enumerate(board + [["."]]):
            s, ci = segment(row)
            c += ci
            acc, ci = add(acc, s)
            c += ci
        return c