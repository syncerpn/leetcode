#1. simply go through all possible factors
def solve(num: int) -> bool:
    if num < 3:
        return False
    s = 1
    i = 2
    while i <= int(num ** 0.5):
        if num % i == 0:
            s += i
            if i != num // i:
                s += num // i
        i += 1
    if s == num:
        return True
    return False