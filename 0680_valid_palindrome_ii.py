# two-pass two-pointer, checking forward-going and backward-going palindrome
# with early stop
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        i, j, c = 0, n - 1, 0
        while i < j:
            if s[i] == s[j]:
                j -= 1
            else:
                c += 1
                if c > 1:
                    break
            i += 1
        else:
            return True
        
        i, j, c = 0, n - 1, 0
        while i < j:
            if s[i] == s[j]:
                i += 1
            else:
                c += 1
                if c > 1:
                    return False
            j -= 1
        return True