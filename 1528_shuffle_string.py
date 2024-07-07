# i read the desc twice to understand it correctly lol
# the problem is easy btw
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sl = [""] * len(s)
        for i, c in zip(indices, s):
            sl[i] = c
        return "".join(sl)
