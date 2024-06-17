#1. append char at the end or at the beginning?
def solve(s: str) -> str:
    forward = True
    r = ""
    for c in s:
        if c == "i":
            forward = not forward
        elif forward:
            r += c
        else:
            r = c + r
    
    return r if forward else r[::-1]