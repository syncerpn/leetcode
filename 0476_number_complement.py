#1. find its next power-of-two
def solve(num: int) -> int:
    i = 1
    while i <= num:
        i *= 2
    
    return i - 1 - num