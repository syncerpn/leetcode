# string modify in-place O(1) space
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = 1
        j = 1
        p = chars[0]
        for i in range(1, len(chars)):
            c = chars[i]
            if c == p:
                n += 1
            else:
                if n > 1:
                    for d in str(n):
                        chars[j] = d
                        j += 1
                chars[j] = c
                j += 1
                n = 1
            p = c
        
        if n > 1:
            for d in str(n):
                chars[j] = d
                j += 1
        return j
