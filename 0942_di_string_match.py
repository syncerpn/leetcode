# likely greedy solution
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        r = []
        i = 0
        j = len(s)
        for c in s:
            if c == "I":
                r.append(i)
                i += 1
            elif c == "D":
                r.append(j)
                j -= 1
        return r + [i]