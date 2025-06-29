# very satisfied with this solution
# O(n) time O(1) space + no overflow
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = 0
        for i in range(len(s)):
            if k == 0:
                ans += s[~i] == "0"
            else:
                k -= (s[~i] == "1")
                ans += 1

            k >>= 1
        return ans
