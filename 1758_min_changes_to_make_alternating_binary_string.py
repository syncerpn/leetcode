# only two cases
# we can form the string "010101..." and "101010..." to compare with s
class Solution:
    def minOperations(self, s: str) -> int:
        z = 0
        o = 0
        for i in range(len(s)):
            if i % 2 == 0:
                z += s[i] != "0"
                o += s[i] != "1"
            else:
                z += s[i] != "1"
                o += s[i] != "0"

        return min(z, o)