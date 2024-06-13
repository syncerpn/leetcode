#1. simple check
def solve(n: int) -> bool:
    i = 1
    while i < n:
        i *= 3
    
    return i == n