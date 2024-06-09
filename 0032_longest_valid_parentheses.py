#1. stack push pop parentheses
#2. calculate max length on the fly is just beautiful
#3. there are DP and string maip solutions as well
def solve(s: str) -> int:
    stack = [-1]
    max_length = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    
    return max_length