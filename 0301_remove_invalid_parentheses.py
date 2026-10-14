# tried optimizing it
# but just ended up with the preprocessing part only
# and went back to backtracking in the end
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        s = deque(list(s))
        pref, suff = "", ""
        while s and s[0] != "(":
            c = s.popleft()
            if c != ")":
                pref += c
        while s and s[-1] != ")":
            c = s.pop()
            if c != "(":
                suff += c
        suff = suff[::-1]
        n = len(s)
        m = s.count("(") + s.count(")")
        
        def dfs(i, v, p):
            if p < 0 or v > n - i:
                return
            if i == n:
                if v == 0 and p == 0:
                    ans.add("".join(q))
                return
            c = s[i]
            if c != "(" and c != ")":
                q.append(c)
                dfs(i+1, v, p)
                q.pop()
            elif c == "(":
                if v > 0:
                    dfs(i+1, v-1, p)
                q.append(c)
                dfs(i+1, v, p+1)
                q.pop()
            elif c == ")":
                if v > 0:
                    dfs(i+1, v-1, p)
                if p > 0:
                    q.append(c)
                    dfs(i+1, v, p-1)
                    q.pop()

        for mm in range(m+1):
            ans = set()
            q = []
            dfs(0, mm, 0)
            if ans:
                break

        return [pref + a + suff for a in ans]