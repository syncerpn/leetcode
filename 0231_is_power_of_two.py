#1. bit manip solution is beautiful
def isPowerOfTwo(n: int) -> bool:
    return n and not (n & n - 1)