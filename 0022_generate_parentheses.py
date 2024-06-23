# backtracking or recursion like below should be ok
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]
        
        res = set()
        for i in range(1,n):
            l = self.generateParenthesis(i)
            r = self.generateParenthesis(n-1-i)
            for li in l:
                for ri in r:
                    res.add("(" + li + ")" + ri)
                    res.add(li + "(" + ri + ")")
        return res