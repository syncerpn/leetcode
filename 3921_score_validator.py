# easy
class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        d = {c: int(c) for c in "0123456"}
        s, c = 0, 0
        for e in events:
            if e in d:
                s += d[e]
            elif e == "W":
                c += 1
            elif e == "WD" or e == "NB":
                s += 1
            if c == 10:
                break
        return s, c