# fairly easy
class Solution:
    def stringSequence(self, target: str) -> List[str]:
        d = {a: b for a, b in zip("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza")}
        ans = []
        for c in target:
            m = "a"
            p = ans[-1] if ans else ""
            while m != c:
                ans.append(p + m)
                m = d[m]
            ans.append(p + m)
        return ans