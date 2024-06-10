#1. simple dict should do
def solve(s: str, t: str) -> bool:
    ms = {}
    mt = {}
    for cs,ct in zip(s,t):
        if cs in ms:
            if ct != ms[cs]:
                return False
        else:
            if ct in mt:
                return False
            ms[cs] = ct
            mt[ct] = cs
    
    return True