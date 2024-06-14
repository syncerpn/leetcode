#1. two pointer solution
def solve(s: str) -> str:
    VOWEL = set("aeiouAEIOU")
    sl = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] not in VOWEL:
            i += 1
        elif s[j] not in VOWEL:
            j -= 1
        else:
            sl[i], sl[j] = sl[j], sl[i]
            i += 1
            j -= 1
    
    return "".join(sl)