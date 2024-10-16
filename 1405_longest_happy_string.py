# try to go from the character with the highest need
# putting 2 of it into the string, then a separator to avoid "aaa", "bbb", "ccc" cases
# the amount of separator depends on whether the target character is still larger than the separator
# that amount, either one or two is determined by q and k in the code
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = [(a, "a"), (b, "b"), (c, "c")]
        def insert(s, last=None):
            d.sort(reverse=True)
            ans = ""
            q = 0
            for i, nt in enumerate(d):
                n, t = nt
                if t == last:
                    q = 1
                    continue
                if n == 0:
                    continue
                k = min(n, 2-q)
                ans += t * k
                d[i] = ((n-k), t)
                break
            return ans
        
        ans = ""
        l = None
        while (s := insert(ans, l)) != "":
            ans += s
            l = ans[-1]
        return ans
            