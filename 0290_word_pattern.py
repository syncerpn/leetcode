#1. two-way dict and lookup
#2. using two-way to make sure no pattern map to two words and vice versa
def solve(pattern: str, s: str) -> bool:
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
