#1. backtracking or recursion like below should be ok
def solve(n: int) -> list:
    if n == 0:
        return [""]
    if n == 1:
        return ["()"]
    
    res = set()
    for i in range(1,n):
        l = generateParenthesis(i)
        r = generateParenthesis(n-1-i)
        for li in l:
            for ri in r:
                res.add("(" + li + ")" + ri)
                res.add(li + "(" + ri + ")")
    return res