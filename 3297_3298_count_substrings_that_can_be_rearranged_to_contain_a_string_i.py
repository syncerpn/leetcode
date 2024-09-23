# sliding window
# should have done it well, but no
# fucked!!!!!
# the counting formula
# THE COUNTING FORMULA
# THE COUNTING FORMULAAAAAAAAAAAAAAAAAAA
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            return 0

        def ind(c):
            return ord(c) - ord("a")

        def is_valid(d):
            for i in range(26):
                if d[i] > 0:
                    return False
            return True

        d = [0 for _ in range(26)]
        for c in word2:
            d[ind(c)] += 1
        
        m = len(word1)
        n = len(word2)
        l = 0
        ans = 0
        for i, c in enumerate(word1):
            d[ind(c)] -= 1
            if i >= n - 1:
                if is_valid(d):
                    j = l
                    while is_valid(d) and j <= i:
                        d[ind(word1[j])] += 1
                        j += 1
                    ans += (j - l) * (m - i)
                    l = j
        return ans