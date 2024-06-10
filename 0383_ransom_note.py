#1. using one dict should be fine

def canConstruct(ransomNote: str, magazine: str) -> bool:
    d = {}
    for c in magazine:
        if c not in d:
            d[c] = 0
        d[c] += 1
    
    for c in ransomNote:
        if c not in d:
            return False
        d[c] -= 1
        if d[c] < 0:
            return False
    
    return True