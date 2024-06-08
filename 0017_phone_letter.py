#1. simply iterate over all possible cases
#2. some suggest backtracking, but is it that necessary?
def solve(digits: str) -> list:
    if len(digits) == 0:
        return []
    
    m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    r = [""]
    for d in digits:
        r = [ri + c for c in m[d] for ri in r]
    return r