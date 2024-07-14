# good problem
# where we deal with stack, prefix product, and string parser
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        DIGITS = "01234567890"
        stack_multiplier = [1]
        n = ""
        atom = ""
        counter = {}
        for c in formula[::-1]:
            if c in DIGITS:
                n = c + n
            elif c == "(":
                stack_multiplier.pop()            
            elif c == ")":
                m = int(n) if n != "" else 1
                stack_multiplier.append(m * stack_multiplier[-1])
                n = ""
            else:
                atom = c + atom
                if c.upper() == c:
                    if atom not in counter:
                        counter[atom] = 0
                    m = stack_multiplier[-1]
                    if n != "":
                        m *= int(n)
                    counter[atom] += m
                    atom = ""
                    n = ""

        r = ""
        for k in sorted(counter.keys()):
            r += k
            if counter[k] > 1:
                r += str(counter[k])
        return r