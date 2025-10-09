# not that difficult
# use stack, clean, and merge parts
# implementation is a bit complicated
# s += "(" is just a trick to trigger cleaning/merging procedure
class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        def clean(l, r):
            m = min(l, r) // k * k
            return l - m, r - m

        s += "("
        q = []
        l, r = 0, 0
        for c in s:
            if c == "(":
                if r > 0:
                    l, r = clean(l, r)
                    while l > 0 or r > 0:
                        if not q:
                            q.append((l, r))
                            break
                        li, ri = q.pop()
                        if l == 0 or ri == 0:
                            l += li
                            r += ri
                            l, r = clean(l, r)
                        else:
                            q.append((li, ri))
                            q.append((l, r))
                            break
                    
                    l, r = 1, 0
                else:
                    l += 1
            else:
                r += 1
        else:
            q.append((l-1, 0))
        ans = ""
        for l, r in q:
            ans += l * "(" + r * ")"
        return ans