# use deque
class Solution:
    def processStr(self, s: str) -> str:
        r = False
        d = deque()
        for c in s:
            if c == "*":
                if d:
                    if r:
                        d.popleft()
                    else:
                        d.pop()
            elif c == "#":
                d += d
            elif c == "%":
                r = ~r
            else:
                if r:
                    d.appendleft(c)
                else:
                    d.append(c)

        return "".join(list(d)) if not r else "".join(list(d)[::-1])