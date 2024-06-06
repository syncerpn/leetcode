#1. pure counter dict
def solve(words: list) -> list:
    counter = {}
    for i, s in enumerate(words):
        for c in s:
            if c not in counter:
                counter[c] = [0 for _ in range(len(words))]
            counter[c][i] += 1
    
    commons = []
    for c in counter:
        commons += min(counter[c]) * [c]
    
    return commons
