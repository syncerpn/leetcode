# mat manip art
class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        n = max(len(si) for si in s)
        s = [list(si + " " * (n - len(si))) for si in s]
        s = list(zip(*s))
        s = ["".join(si).rstrip() for si in s]
        return s