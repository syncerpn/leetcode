# sliding window
# expand the right side first to find a valid substring
# then trim the left side, removing all unnecessary chars without invalidate the ans
# check whether the substring is shorter than the previous solution
# trim one more char on the left to invalidate the current substring
# repeat until the end of the string
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(t)
        if len(s) < n:
            return ""
        d = Counter(t)
        q = set(d.keys())
        ans_l, ans = len(s), ""
        j = 0
        for i, c in enumerate(s):
            if c in d:
                d[c] -= 1
                if d[c] <= 0:
                    q.discard(c)
                if not q:
                    while j < i:
                        e = s[j]
                        if e in d:
                            if d[e] == 0:
                                break
                            d[e] += 1
                        j += 1
                    
                    if ans_l >= i - j + 1:
                        ans_l, ans = i - j + 1, s[j:i+1]
                    
                    e = s[j]
                    d[e] += 1
                    q.add(e)
                    j += 1
        
        return ans