# use set
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        d = set()
        for a, b in pairwise(s):
            if a+b not in d:
                d.add(a+b)
            if b+a in d:
                return True
        return False