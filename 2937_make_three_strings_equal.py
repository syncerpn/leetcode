# fairly easy, finding common prefix
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        i = 0
        l, m, n = len(s1), len(s2), len(s3)
        while i < l and i < m and i < n:
            if s1[i] == s2[i] == s3[i]:
                i += 1
                continue
            break
        if i == 0:
            return -1
        return l + m + n - 3 * i