# fairly easy sliding window
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ans = 0
        l, r, n = 0, 1, len(colors)
        p = colors[l]

        ans = 0
        while l < n:
            q = colors[r%n]
            if q != p:
                if r - l + 1 == k:
                    ans += 1
                    l += 1
            else:
                l = r
            p = q
            r += 1
        return ans