# stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if len(t) > 1 or t.isdigit():
                s.append(int(t))
            else:
                a = s.pop()
                b = s.pop()
                v = 0
                if t == "+":
                    v = b + a
                elif t == "-":
                    v = b - a
                elif t == "/":
                    v = int(b / a)
                elif t == "*":
                    v = b * a
                s.append(v)
        return s[0]