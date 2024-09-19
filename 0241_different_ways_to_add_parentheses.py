# recursive + memoi
# it actually still passed without the memoi
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        cache = {}
        def helper(l, r):
            if (l, r) in cache:
                return cache[(l, r)]
            if r - l <= 1:
                cache[(l, r)] = [int(expression[l:r+1])]
            else:
                v = []
                for i in range(l, r+1):
                    c = expression[i]
                    if not c.isdigit():
                        lps = helper(l, i-1)
                        rps = helper(i+1, r)
                        for lp in lps:
                            for rp in rps:
                                if c == "-":
                                    v.append(lp-rp)
                                elif c == "+":
                                    v.append(lp+rp)
                                elif c == "*":
                                    v.append(lp*rp)
                cache[(l, r)] = v
            return cache[(l, r)]
        return helper(0, len(expression)-1)

# dp is also available
# but i dont like it at all
# maybe one day i will get back to you dp