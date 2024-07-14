# pairwise check for "ba" pair
# or the following
class Solution:
    def checkString(self, s: str) -> bool:
        must_be_b = False
        for c in s:
            if c == "b":
                must_be_b = True
            elif c == "a" and must_be_b:
                return False
        return True