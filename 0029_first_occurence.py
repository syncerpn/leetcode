#1. slicing
def strStr(haystack: str, needle: str) -> int:
    n = len(haystack)
    k = len(needle)
    for i in range(n-k+1):
        if haystack[i:i+k] == needle:
            return i
    
    return -1