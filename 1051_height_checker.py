#1. sort and check for general constraints
#2. counting sort might be used in specific cases
def solve(heights: list) -> int:
    sheights = sorted(heights)
    c = 0
    for s, h in zip(sheights, heights):
        c += (s != h)
    return c