# O(26n)
# we need to find the char with max count within the a sliding window
# other characters can be replace by that one
# so that we obtain a sequence of only a single character
# however, this does not scale well with non-limited charset
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = -1
        d = {c: 0 for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        ans = 0
        for r, c in enumerate(s):
            d[c] += 1
            while r - l - max(d.values()) > k:
                l += 1
                d[s[l]] -= 1
            ans = max(ans, r - l)
        return ans

# this is optimized to reach true O(n)
# the point is, we just need to find res, which is the max length of the valid window
# keep checking it against the max frequency of a character plus k
# as res increases, we dont need to decrease it any time
# instead just uncount the first char within the length of the window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {c: 0 for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        maxf = res = 0
        for r, c in enumerate(s):
            d[c] += 1
            maxf = max(maxf, d[c])
            if res < maxf + k:
                res += 1
            else:
                d[s[r-res]] -= 1
        
        return res

# another variant of the above solution
# it might be harder to understand though
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {c: 0 for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        l = -1
        maxf = 0
        for r, c in enumerate(s):
            d[c] += 1
            maxf = max(maxf, d[c])
            if r - l - maxf > k:
                l += 1
                d[s[l]] -= 1
        
        return r - l