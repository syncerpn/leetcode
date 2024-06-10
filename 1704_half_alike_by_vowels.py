#1. count the first half, then remove for the second
#2. alike if counter is exact zero in the end
def solve(self, s: str) -> bool:
    n = 0
    VOWELS = "aeiouAEIOU"
    for i, c in enumerate(s):
        if c not in VOWELS:
            continue

        if i >= len(s) // 2:
            n -= 1
            if n < 0:
                return False
        else:
            n += 1
    
    return n == 0
