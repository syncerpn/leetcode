# simple sliding window
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = "aeiou"
        t = 0
        for i in range(k):
            if s[i] in VOWELS:
                t += 1
        ans = t
        for i in range(k, len(s)):
            t += (s[i] in VOWELS) - (s[i-k] in VOWELS)
            ans = max(ans, t)
        return ans