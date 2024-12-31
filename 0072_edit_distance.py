# dfs
# but with memoi, it is a dp solution
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        @functools.cache
        def test(i, j):
            if j == n:
                return m - i
            elif i == m:
                return n - j
            elif word1[i] == word2[j]:
                return test(i+1, j+1)
            return 1 + min(test(i+1, j+1), test(i, j+1), test(i+1, j))
            
        return test(0, 0)