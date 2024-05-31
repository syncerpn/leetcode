#1. convert to int
#2. simply loop and count
def solve(s: str) -> int:
    i = 0
    n = int(s, 2)
    while n != 1:
        i = i + 1 + n % 2
        n = n - n//2
    return i