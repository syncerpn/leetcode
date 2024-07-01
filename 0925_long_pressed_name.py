# compare two equivalent sequences of the same characters in name and typed
# that in typed should be larger than that in name
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False
        i = 0
        j = 0
        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                return False

            ci = 0
            cj = 0
            r = name[i]
            while i < len(name) and name[i] == r:
                ci += 1
                i += 1
            
            while j < len(typed) and typed[j] == r:
                cj += 1
                j += 1
            
            if cj < ci:
                return False

        return i == len(name) and j == len(typed)