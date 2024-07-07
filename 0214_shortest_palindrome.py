# brute force solution somehow is still allowed
# maybe built in function is fast enough for performance
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        i = n
        while i > 0:
            if s[:i] == s[i-1::-1]:
                break
            i -= 1
        return s[n-1:i-1:-1] + s

# KMP algorithm is optimal for an O(n) solution
# the trick is to append reverse of s into s with "#" as separator
# we then build the lps table (named "m" in the code) for the new string
# we can find out the common part between the target palindrome and the provided s
# then append the uncommon part to s result in the answer
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)    
        ss = s + "#" + s[::-1]
        
        m = [0] * (2 * n + 1)

        # as an effort to understand KMP
        # we have to build from the beginning of the string
        # instead of trying to check just s and its reverse
        # (i.e. i tried pi = 0 and si = n + 1)
        # that will NOT work
        pi, si = 0, 1
        while si < 2 * n + 1:
            if ss[pi] == ss[si]:
                m[si] = pi + 1
                pi += 1
                si += 1
            else:
                if pi == 0:
                    si += 1
                else:
                    pi = m[pi-1]
        
        k = m[-1]
        return s[n-1:k-1-n:-1] + s