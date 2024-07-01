# two-pointer swap
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        i = 0
        j = len(s) - 1
        s = [c for c in s]
        while i < j:
            if s[i] not in ALPHABET:
                i += 1
            elif s[j] not in ALPHABET:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)