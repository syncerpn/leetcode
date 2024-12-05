# two-pointer
# this looks not very nice, but works just fine
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        j = 0
        for i, c in enumerate(target):
            if c == "_":
                continue
            if c == "L":
                while j < n:
                    d = start[j]
                    if d == "L":
                        if j < i:
                            return False
                        j += 1
                        break
                    elif d == "R":
                        return False
                    j += 1
                else:
                    return False
            elif c == "R":
                while j < n:
                    d = start[j]
                    if d == "R":
                        if j > i:
                            return False
                        j += 1
                        break
                    elif d == "L":
                        return False
                    j += 1
                else:
                    return False
        while j < n:
            if start[j] != "_":
                return False
            j += 1
        return True