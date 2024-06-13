#1. beautiful O(n) solution
#2. simply add 1 to previous counting upon reaching a new power of two number
def solve(n: int) -> list:
    result = [0]
    k = 0
    for i in range(1, n+1):
        if i & (i-1) == 0:
            k = 0
        result.append(1 + result[k])
        k += 1
    return result
