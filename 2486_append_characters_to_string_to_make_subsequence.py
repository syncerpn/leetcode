#1. use two pointers to find the longest subsequence of t existing in s
#2. length of the appending string can be derived easily
def solve(s: str, t: str) -> int:
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    
    return len(t) - j