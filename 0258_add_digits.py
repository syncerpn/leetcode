#1. simply repeat the process and return
def solve(num: int) -> int:
    while num >= 10:
        n = 0
        while num != 0:
            n += num % 10
            num = num // 10
        num = n
    
    return num