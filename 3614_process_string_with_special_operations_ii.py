# math
# may need revisit
# first, check for the final length; if k > final length, return "."
# going backward of the applied operations to get the length at each point
# if c == "*", meaning a char was deleted, then we restore l = l + 1
# if c == "#", meaning the whole string was duplicated; then if k > l // 2, before duplication k = k - l // 2
# or else we keep k and restore l = l // 2
# if c == "%", reverse k as well k = l - k - 1
# if c == a character, meaning it is appended to the result string; if k is that last pos appended, just return it
# otherwise, dont need to care about it by just removing it from the string and decrease l = l - 1
class Solution:
    def processStr(self, s: str, k: int) -> str:
        l = 0
        for c in s:
            if c == "*":
                if l:
                    l -= 1
            elif c == "#":
                l *= 2
            elif c == "%":
                pass
            else:
                l += 1
        if k + 1 > l:
            return "."
        for c in reversed(s):
            if c == "*":
                l += 1
            elif c == "#":
                if k + 1 > (l + 1) // 2:
                    k -= l // 2
                l = (l + 1) // 2
            elif c == "%":
                k = l - k - 1
            else:
                if k + 1 == l:
                    return c
                l -= 1
        return "."