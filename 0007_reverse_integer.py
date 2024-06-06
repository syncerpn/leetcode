#1. python string reverse should do
def solve(x: int) -> int:
    s = str(x)
    sign = ""
    if s[0] == "-":
        sign = "-"
        s = s[1:]
    
    r = int(sign + s[::-1])

    if r < -2147483648 or r > 2147483647:
        return 0

    return r

#1. true numerical reverse
def solve2(self, x: int) -> int:
    INT_MAX = 2**31-1
    sign = 0
    if x < 0:
        sign = 1
        x = -x
    
    n = 0
    while x > 0:
        d = x % 10
        if (INT_MAX + sign - d) / 10 > n:
            n = n * 10 + d
        else:
            return 0

        x = x // 10

    return -n if sign else n