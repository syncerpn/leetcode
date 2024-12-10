# same as the version, but encode with tuple to pass the memory limit
class Solution:
    def maximumLength(self, s: str) -> int:
        d = {}
        p = "."
        v = 1
        for c in s:
            if c != p[-1]:
                p = c
                v = 1
            else:
                v += 1
            if (p, v) not in d:
                d[(p, v)] = 0
            d[(p, v)] += 1
        
        ans = -1
        for c in d:
            p, v = c
            if d[c] >= 3:
                ans = max(ans, v)
            elif v >= 3:
                if d[(p, v-1)] >= 2:
                    ans = max(ans, v-1)
                else:
                    ans = max(ans, v-2)
            elif v == 2:
                if d[(p, v-1)] >= 2:
                    ans = max(ans, v-1)
        return ans
        