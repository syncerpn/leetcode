#1. simply count the apperance of each char
#2. palindrome can be constructed with even number of characters, except the middle char
def solve(s: str) -> int:
    counter = {}
    for c in s:
        if c not in counter:
            counter[c] = 0
        counter[c] += 1
    
    has_odd = 0
    n = 0
    for c in counter:
        if counter[c] % 2 == 1:
            has_odd = 1
        n += counter[c] - counter[c] % 2
    
    return n + has_odd
