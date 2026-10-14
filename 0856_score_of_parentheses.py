# works
# but does not seem like a good solution though
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def helper(l, r):
            if r < l:
                return 1
            ll = l
            i = l
            t = 0
            ans = 0
            while i <= r:
                if s[i] == ")":
                    t -= 1
                else:
                    t += 1
                if t == 0:
                    ans += 2 * helper(ll + 1, i - 1)
                    ll = i + 1
                i += 1

            return ans
        
        return helper(0, len(s) - 1) // 2

# super fast O(n) time O(1) space
# by nicely expand the expression
# (()(())) = 2*() + 2*(()) = 2*() + 4*()
# therefore, just count the depth of unit bracket pair "()"
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        d = 0
        ans = 0
        p = ""
        for c in s:
            if c == "(":
                d += 1
            else:
                d -= 1
                if p == "(":
                    ans += 1 << d
            p = c
        return ans