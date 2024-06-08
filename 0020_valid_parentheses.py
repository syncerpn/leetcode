#1. stack push and pop
def solve(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    
    openb = ["(", "[", "{"]
    stack = ""
    for c in s:
        if c in openb:
            stack += c
        else:
            if not stack:
                return False
            l = stack[-1]
            if (l == "(" and c == ")") or (l == "[" and c == "]") or (l == "{" and c == "}"):
                stack = stack[:-1]
            else:
                return False
    
    return False if stack else True