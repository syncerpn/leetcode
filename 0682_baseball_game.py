# stack push/pop should work
# single-pass, tracking sum on the way
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = 0
        r = [0]
        for c in operations:
            v = 0
            if   c == "C":
                v = -(r.pop())
            else:
                if c == "D":
                    v = r[-1] * 2
                elif c == "+":
                    v = r[-1] + r[-2]
                else:
                    v = int(c)
                r.append(v)
            s += v
        return s