#1. math works
def solve(low: int, high: int) -> int:
    return (high - low) // 2 + max(high % 2, low % 2)