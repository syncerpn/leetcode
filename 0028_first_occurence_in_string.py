# simply iterate and compare
# here with a bit optimization
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
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

# simple slicing
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        k = len(needle)
        for i in range(n-k+1):
            if haystack[i:i+k] == needle:
                return i
        
        return -1