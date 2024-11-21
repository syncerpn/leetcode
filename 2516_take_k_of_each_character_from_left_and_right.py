# using 0 as a left bound, try expanding to the right until we find a valid one
# then move the (sliding) window cyclic left (taking -1, -2, ... indices)
# while shrinking the window at the same time without invalidate the condition
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        r = 0
        d, p = {"a": 0, "b": 0, "c": 0}, set()
        for i, c in enumerate(s):
            d[c] += 1
            if d[c] >= k:
                p.add(c)
            if len(p) == 3:
                r = i
                break
        else:
            return -1
        
        ans = r + 1
        j = len(s) - 1
        while j >= 0:
            d[s[j]] += 1
            while r >= 0:
                if d[s[r]] < k + 1:
                    break
                d[s[r]] -= 1
                r -= 1
            ans = min(ans, r + 1 + len(s) - j)
            j -= 1
        return ans