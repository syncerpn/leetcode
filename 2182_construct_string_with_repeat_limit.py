# counter and greedy
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        d = Counter(s)
        keys = sorted(d.keys(), reverse=True)
        ans = ""
        i, j, n = 0, 1, len(keys)
        while i < n:
            b = keys[i]
            if d[b] == 0:
                i += 1
            else:
                while j <= i:
                    j += 1
                k = min(repeatLimit, d[b])
                ans += b * k
                d[b] -= k
                if d[b] > 0:
                    if j >= n:
                        break
                    a = keys[j]
                    ans += a
                    d[a] -= 1
                    if d[a] == 0:
                        j += 1
        
        return ans