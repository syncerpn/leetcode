# recursive solution
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @functools.cache
        def extends(i, j):
            if i == len(s) and j == len(p):
                return True
            
            if j == len(p):
                return False
            
            if p[j] == "?":
                return extends(i+1, j+1)
            elif p[j] == "*":
                for k in range(i, len(s)+1):
                    if extends(k, j+1):
                        return True
                return False
            else:
                if i < len(s) and s[i] == p[j]:
                    return extends(i+1, j+1)
            return False
        return extends(0, 0)

# much faster with two-pointer
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j, mat, star_idx = 0, 0, 0, -1

        while i < len(s):
            if j < len(p) and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star_idx = j
                mat = i
                j += 1
            elif star_idx != -1:
                j = star_idx + 1
                mat += 1
                i = mat
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)