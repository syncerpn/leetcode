#1. problem is not clearly defined though
def solve(a: str, b: str) -> int:
    if a == b:
        return -1
    else:
        return max(len(a), len(b))