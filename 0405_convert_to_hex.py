#1. char lookup
def solve(self, num: int) -> str:
    if num == 0:
        return "0"
    if num < 0:
        return solve((1 << 31) + num + (1 << 31))
    HEXSTR = "0123456789abcdef"
    r = ""
    while num != 0:
        c = HEXSTR[num % 16]
        num = num // 16
        r = c + r
    return r
