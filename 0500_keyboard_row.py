#1. just check if all chars are in the same row
def solve(words: list) -> list:
    D = {0: set("qwertyuiop"), 1: set("asdfghjkl"), 2: set("zxcvbnm")}
    res = []
    for word in words:
        i = 0
        for k in D:
            if word[0].lower() in D[k]:
                i = k
                break
        
        for c in word:
            if c.lower() not in D[k]:
                break
        else:
            res.append(word)
    
    return res