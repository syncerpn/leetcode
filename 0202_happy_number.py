#1. use dict, O(N) space
def solve(n: int) -> bool:
    def happy_score(n: int) -> int:
        score = 0
        while n:
            score += (n % 10) ** 2
            n = n // 10
        return score

    d = {}
    s = happy_score(n)
    while s != 1:
        if s in d:
            return False
        d[s] = n
        n = s
        s = happy_score(n)
    return True

#1. or cycle detection with floyd's algorithm, just beautiful
def solve2(n: int) -> bool:
    def happy_score(n: int) -> int:
        score = 0
        while n:
            score += (n % 10) ** 2
            n = n // 10
        return score
    
    t = happy_score(n)
    h = happy_score(t)

    while h != 1:
        if t == h:
            return False
        t = happy_score(t)
        h = happy_score(happy_score(h))
    
    return True