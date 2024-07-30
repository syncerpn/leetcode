# basically just try to compare every substrings formed from s and t
# we fix j = 0 for string t and form substring s[i:] to compare with t
# for example:
# i = 0, j = 0: computer... vs computation...
# i = 1, j = 0:  omputer... vs computation...
# i = 2, j = 0:   mputer... vs computation...
# i = 3, j = 0:    puter... vs computation...
# and so on
# the brilliant point here is then fixing i = 0 and change j from 1 (not 0) until end
# i = 0, j = 1: computer... vs  omputation...
# i = 0, j = 2: computer... vs   mputation...
# i = 0, j = 3: computer... vs    putation...
# i = 0, j = 4: computer... vs     utation...
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        def test(i, j):
            res = pre = cur = 0
            for k in range(min(m-i, n-j)):
                cur += 1
                if s[i+k] != t[j+k]:
                    pre, cur = cur, 0
                res += pre
            return res
        
        return sum(test(i, 0) for i in range(m)) + sum(test(0, j) for j in range(1, n))