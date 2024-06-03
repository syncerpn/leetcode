#1. parse leading zeros
#2. parse sign
#3. parse nums
def solve(s: str) -> int:
    charnums = "0123456789"
    num_found = False
    sign = 1
    pos_end =  2147483647
    neg_end = -2147483648

    n = 0

    for c in s:
        if not num_found:
            if c == " ":
                continue
            elif c == "-":
                sign = -1
                num_found = True
                continue
            elif c == "+":
                num_found = True
                sign = 1
                continue
        
        num_found = True
        if c not in charnums:
            break
            
        n = n * 10 + sign * (ord(c) - 48)
        if n > pos_end:
            n = pos_end
            break
        elif n < neg_end:
            n = neg_end
            break

    return n