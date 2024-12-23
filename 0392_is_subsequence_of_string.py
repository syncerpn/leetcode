# two pointers, one for each sequence
# iterate and check
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s):
            if j >= len(t):
                return False
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return True