# not difficult, but again, very cumbersome
# need to calculate the evenly, left-larger gaps
# then concat words into lines
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        t, s = 0, []
        ans = []
        for w in words:
            if t + len(w) + len(s) > maxWidth:
                r = ""
                n = len(s)
                if n == 1:
                    r = s[0] + (maxWidth - t) * " "
                else:
                    g = (maxWidth - t) // (n - 1)
                    k = (maxWidth - t) - (n - 1) * g
                    r = s[0]
                    for i, c in enumerate(s[1:]):
                        r += g * " "
                        if i < k:
                            r += " " + c
                        else:
                            r += c

                ans.append(r)
                t, s = 0, []
            t += len(w)
            s.append(w)
        
        if s:
            ans.append(" ".join(s) + (maxWidth - t - len(s) + 1) * " ")
        return ans
