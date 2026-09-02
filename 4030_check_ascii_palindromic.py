# edge cases are interesting
class Solution:
    def isPalindromic(self, s: str) -> bool:
        n = len(s)
        for i in range(n//2):
            a, b = bin(ord(s[i]))[2:], bin(ord(s[~i]))[2:]
            aa = "0" * (8 - len(a)) + a
            bb = b[::-1] + "0" * (8 - len(b))
            if aa != bb:
                return False
        if n % 2:
            a = bin(ord(s[n//2]))[2:]
            aa = "0" * (8 - len(a)) + a
            if aa[:4] != aa[4:][::-1]:
                return False
        return True