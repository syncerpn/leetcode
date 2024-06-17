#1. two-pointer, 0 and sqrt(c)
def solve(c: int) -> bool:
    a = 0
    b = int(sqrt(c))
    
    while a <= b:
        s = a * a + b * b 
        if s == c:
            return True
        elif s < c:
            a += 1
        else:
            b -= 1
    return False