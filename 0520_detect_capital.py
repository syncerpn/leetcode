def solve(word: str) -> bool:
    UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(word) == 1:
        return True
    
    if word[0] in UPPER and word[1] not in UPPER:
        return word[2:] == word[2:].lower()
    return word == word.upper() or word == word.lower()
