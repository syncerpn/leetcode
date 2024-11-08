# fairly easy
class Solution:
    def compressedString(self, word: str) -> str:
        p = word[0]
        n = 1
        ans = ""
        for i in range(1, len(word)):
            c = word[i]
            if c == p and n < 9:
                n += 1
            else:
                ans += str(n) + p
                p = c
                n = 1
        ans += str(n) + p
        return ans