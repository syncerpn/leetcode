# we need to check whether the two have exactly two different chars
# or if they are the same while having repeating characters (e.g. two "a"s or three "b"s)
# otherwise, return false
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        has_twin = False
        d = {}
        i = None
        j = None
        for k in range(len(s)):
            c = s[k]
            g = goal[k]
            if c != g:
                if i is None:
                    i = k
                elif j is None:
                    j = k
                    if s[i] != goal[j] or s[j] != goal[i]:
                        return False
                else:
                    return False
            else:
                if c not in d:
                    d[c] = 0
                d[c] += 1
                if d[c] >= 2:
                    has_twin = True
        
        if i is not None and j is not None:
            return True
        if i is None and j is None:
            return has_twin
        return False