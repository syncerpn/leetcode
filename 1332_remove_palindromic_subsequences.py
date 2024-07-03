# this one is very nice
# it does not test your coding skill
# but rather your logic
# if the whole string is palindromic, it takes only one turn
# otherwise, just remove all "a" then all "b"
# string composed from only one character is palindromic
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        return 2