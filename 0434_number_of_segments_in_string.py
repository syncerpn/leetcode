#1. track segment and empty sequence
def solve(s: str) -> int:
    is_segment = False
    count = 0
    for c in s:
        if c != " ":
            is_segment = True
        else:
            if is_segment:
                count += 1
            is_segment = False
    
    return count + is_segment