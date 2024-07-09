# we just need 3 chars a b c for replacement
class Solution:
    def modifyString(self, s: str) -> str:
        ALPHABET = "abc"
        sl = [c for c in s]
        sl = ["#"] + sl + ["#"]
        for i in range(1, len(sl)-1):
            if sl[i] != "?":
                continue
            p = sl[i-1]
            n = sl[i+1]
            for c in ALPHABET:
                if c != p and c != n:
                    sl[i] = c
        return "".join(sl[1:-1])