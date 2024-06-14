#1. recursive solution
def solve(n: int) -> bool:
    i = 1
    while i < n:
        i *= 4
    return i == n

#1. bitwise solution is just beautiful
def solve2(n: int) -> bool:
    return (n > 0) and (n & (n - 1) == 0) and (n & 0x55555555 != 0)