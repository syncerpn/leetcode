#1. string concat and modulo
def solve(num: int) -> str:
    if num < 0:
        return "-" + solve(abs(num))
    if num == 0:
        return "0"
    r = ""
    while num:
        r = str(num % 7) + r
        num = num // 7
    
    return str(r)