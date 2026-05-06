# a bit mess implementing this
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        f = 0
        m = 1
        ans = 0
        for a, b in pairwise(arr):
            if b > a:
                if f == 1:
                    m += 1
                else:
                    if f == -1:
                        if m > 2:
                            ans = max(ans, m)
                        m = 2
                    else:
                        m += 1
                    f = 1
            elif b < a:
                if f == -1:
                    if m > 1:
                        m += 1
                        ans = max(ans, m)
                else:
                    if f == 1:
                        m += 1
                        ans = max(ans, m)
                    f = -1
            else:
                if f == -1 and m > 1:
                    ans = max(ans, m)
                m = 1
                f = 0
        return ans

# more clean
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ans = 0
        u, d = 0, 0
        for a, b in pairwise(arr):
            if d and a < b or a == b:
                u = 0
                d = 0
            u += int(a < b)
            d += int(a > b)
            if u and d:
                ans = max(ans, u + d + 1)
        return ans