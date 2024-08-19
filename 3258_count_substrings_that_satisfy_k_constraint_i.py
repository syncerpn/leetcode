# first part was pretty easy with sliding window/two pointers
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l = 0
        ones = 0
        zeros = 0
        ans = 0
        for i, c in enumerate(s):
            if c == "0":
                zeros += 1
            else:
                ones += 1
            while zeros > k and ones > k:
                if s[l] == "0":
                    zeros -= 1
                else:
                    ones -= 1
                l += 1
            ans += i - l + 1
        return ans