# dont overthinking this one
# just compare left most and right most
# and gradually going in two dirs
# make sure to equalize by replacing the larger one with smaller one lexicoly
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = [c for c in s]
        n = len(s)
        for i in range(n // 2 + 1):
            j = n - 1 - i
            if s[i] < s[j]:
                s[j] = s[i]
            elif s[i] > s[j]:
                s[i] = s[j]
        return "".join(s)
                