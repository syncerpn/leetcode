#1. simply iterate and compare
#2. here with a bit optimization
def solve(haystack: str, needle: str) -> int:
    fn = needle[0]
    i = 0
    while i < len(haystack) - len(needle) + 1:
        i_next = -1
        if fn == haystack[i]:
            for j in range(1, len(needle)):
                if i_next == -1 and fn == needle[j]:
                    i_next = i+j
                if haystack[i+j] != needle[j]:
                    break
            else:
                return i

        i = i_next if i_next != -1 else i+1

    return -1