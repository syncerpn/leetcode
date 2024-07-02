# string stacking is just beautiful
# if their stacks are the same, return first c-char substring
# where c is gcd of length of str1 and str2
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            c = gcd(len(str1), len(str2))
            return str1[0:c]

        return ""