# two-way hash table and lookup
# using two-way to make sure no pattern map to two words and vice versa
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = {c: None for c in set(pattern)}
        s_map = {}
        sl = s.split(" ")
        if len(pattern) != len(sl):
            return False

        for c, si in zip(pattern, sl):
            if pattern_map[c] == None:
                if si in s_map:
                    return False
                pattern_map[c] = si
                s_map[si] = c
            elif pattern_map[c] != si:
                return False
        
        return True