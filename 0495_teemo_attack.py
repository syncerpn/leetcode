#1. calculate overlapping between two consecutive time in the series
#2. no overlapping gives max duration; otherwise, partly
def solve(timeSeries: list, duration: int) -> int:
    r = 0
    for i, j in pairwise(timeSeries):
        r += min(j-i, duration)
    
    return r + duration