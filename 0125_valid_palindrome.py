#1. using two pointers
def solve(s: str) -> bool:
    charset = set("0123456789abcedefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    i = 0
    j = len(s) - 1
    while i < j:
        while i < len(s):
            if s[i] in charset:
                break
            i += 1
        else:
            break

        while j >= 0:
            if s[j] in charset:
                break
            j -= 1
        else:
            break

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True