#1. basically the idea is to sort pair/tuple (capital, profits)
#2. then drawing the max profits that we can afford with the current capital
#3. but we need to use priority queue for faster processing
#4. nice problem
def solve(k: int, w: int, profits: list, capital: list) -> int:
    import heapq
    cp = sorted(zip(capital, profits))
    n = len(cp)
    d = []
    i = 0
    i = 0
    while k > 0:
        while i < n:
            if cp[i][0] > w:
                break
            heapq.heappush(d, -cp[i][1])
            i += 1
        if not d:
            break
        k -= 1
        w -= heapq.heappop(d)
    return w