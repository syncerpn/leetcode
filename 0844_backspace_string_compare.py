# stack push/pop is trivial
# the following solution is O(n) time O(1) space
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        bs = 0
        bt = 0
        while i >= 0 or j >= 0:
            while bs > 0 or (i >= 0 and s[i] == "#"):
                if i < 0:
                    break
                if s[i] == "#":
                    bs += 1
                else:
                    bs -= 1
                i -= 1
                
            while bt > 0 or (j >= 0 and t[j] == "#"):
                if j < 0:
                    break
                if t[j] == "#":
                    bt += 1
                else:
                    bt -= 1
                j -= 1
            
            if i < 0 and j < 0:
                return True
            elif i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
                i -= 1
                j -= 1
            else:
                return False

        return i < 0 and j < 0
