# bruteforce should work at about O(nlogn) (even less)
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for a in range(num1, num2+1):
            s = str(a)
            for i in range(1, len(s)-1):
                if (s[i] > s[i-1] and s[i] > s[i+1]) or (s[i] < s[i-1] and s[i] < s[i+1]):
                    ans += 1
        return ans