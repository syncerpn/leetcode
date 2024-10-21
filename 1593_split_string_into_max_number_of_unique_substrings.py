# backtracking
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans = [0]
        def helper(l, v):
            if l == len(s):
                ans[0] = max(ans[0], len(v))
            for i in range(l, len(s)):
                w = s[l:i+1]
                if w in v:
                    continue
                v.add(w)
                helper(i+1, v)
                v.discard(w)
        
        helper(0, set())
        return ans[0]

# crazy enough, adding just one condition makes it a lot different in actual run time
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans = [0]
        def helper(l, v):
            if len(v) + (len(s) - l) > ans[0]: # the thing is here; without vs. with it: 159ms vs. 7ms
                if l == len(s):
                    ans[0] = max(ans[0], len(v))
                for i in range(l, len(s)):
                    w = s[l:i+1]
                    if w in v:
                        continue
                    v.add(w)
                    helper(i+1, v)
                    v.discard(w)
        
        helper(0, set())
        return ans[0]