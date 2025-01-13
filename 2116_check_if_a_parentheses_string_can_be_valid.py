# very very good problem
# costed me 4 hours to solve with an one-pass O(n) time, O(1) space
# we want to greedily balance the string
# so if c == ")" and it is locked, try matching it with any locked "("
# if there is no locked "(" before it, match it with an unlocked one
# the interesting thing is about the second case with a locked c == "("
# we may borrow an unlocked ")" to balance it, but later if there is a locked ")",
# we return the borrowed and match the locked ")" to it.
# in the code, p is the number of free unlocked so far
# q is the number of unmatched locked "("
# and m is the number of borrowed unlocked ")" to match with locked "("
# unlocked "(" and ")" are treated exactly the same
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        p = 0
        q = 0
        m = 0
        for c, l in zip(s, locked):
            if l == "1":
                if c == ")":
                    if q > 0:
                        q -= 1
                    elif p > 0:
                        p -= 1
                    elif m > 0:
                        m -= 1
                        p += 1
                    else:
                        return False
                else:
                    q += 1
            else:
                if q > 0:
                    q -= 1
                    m += 1
                else:
                    p += 1
        return q == 0 and p % 2 == 0