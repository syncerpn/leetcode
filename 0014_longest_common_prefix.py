#1. just take one as ref and iterate
def solve(strs: list) -> str:
    lcp = ""
    for i, c in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s):
                return lcp
            if s[i] != c:
                return lcp
        
        lcp += c
    
    return lcp