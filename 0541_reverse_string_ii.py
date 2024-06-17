#1. slice into a list of k-long partitions
#2. reverse those with an even index
#3. merge them all into the result
def solve(s: str, k: int) -> str:
    n = len(s)
    sl = [s[i*k:i*k+k] for i in range(n // k)]
    d = n % k
    if d:
        sl += [s[-d:]]
    for i, si in enumerate(sl):
        if i % 2 == 0:
            sl[i] = si[::-1]
    
    return "".join(sl)