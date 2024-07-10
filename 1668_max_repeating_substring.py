# lets do binary search
# though it may be not optimal
# some also use KMP
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        l = 1
        r = len(sequence) // len(word) + 1
        while l < r:
            m = (l + r) // 2
            if sequence.find(word * m) != -1:
                l = m + 1
            else:
                r = m
        return l - 1