# lee's solution
# it was supposed to be one-lining
# anyway, it is at some fucking different levels
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        t, f = True, False
        return eval(expression.replace('!', 'not |').replace('&(', 'all([').replace('|(', 'any([').replace(')', '])'))