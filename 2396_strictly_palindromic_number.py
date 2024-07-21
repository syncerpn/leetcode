# solution is easy, because this is math-based
# with any n >= 4
# convert to base n-2 will always result in non-palindromic str
# for example n == 4: it is base-2 100 which is non-palindromic
# for example n  > 4: it is base-(n-2) 12 which is non-palindromic
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False