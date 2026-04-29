# easy
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        b = -1
        if n % 2:
            b = n // 2
        for i, c in enumerate(palindrome):
            if i == b:
                continue
            if c > "a":
                return palindrome[:i] + "a" + palindrome[i+1:]
        return palindrome[:-1] + "b"