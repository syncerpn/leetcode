#1. string manip with carry and pattern
def solve(a: str, b: str) -> str:
    c = "0"
    r = ""
    i = -1
    na = len(a)
    nb = len(b)

    if na > nb:
        b = "0" * (na - nb) + b
    else:
        a = "0" * (nb - na) + a

    while i + len(a) >= 0 and i + len(b) >= 0:
        s = sorted(a[i] + b[i] + c)
        c = s[1]
        r = s[0] + r if c == "1" else s[2] + r
        i -= 1
    
    return c + r if c == "1" else r