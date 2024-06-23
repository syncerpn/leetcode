# iterate the string
# find palindrome by extending from the center, where the current char is the center
# pay attention to removing all char same as the center ("zcccccz" case for example)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_p_length = 1
        max_p_i = [0,0]


        i = 0
        while i < len(s):
            n = 1
            l = i - 1
            r = i + 1
            c = s[i]
            while l >= 0:
                if s[l] != c:
                    break
                
                l = l - 1
            
            while r < len(s):
                if s[r] != c:
                    break
                
                r = r + 1
            
            i = r

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l = l - 1
                r = r + 1
            
            if (r - l - 1) > max_p_length:
                max_p_i = [l+1,r-1]
                max_p_length = r - l - 1
            
        l, r = max_p_i
        return s[l:r+1]

# manacher's algorithm O(N) time and space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        max_len = 1
        max_str = s[0]
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0

        for i in range(len(s)):
            if i < right:
                dp[i] = min(right-i, dp[2*center-i])
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1
            if i+dp[i] > right:
                center = i
                right = i+dp[i]
            if dp[i] > max_len:
                max_len = dp[i]
                max_str = s[i-dp[i]:i+dp[i]+1].replace('#','')
        return max_str