# kinda brute force
# first, we try to limit the possible numbers of zeros in a substring
# because s has len n, we limit number of zeros to sqrt of n
# then try to find all substring with exact k zeros, for k from 0 to the limit
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        z = 0
        while n - z * z >= z:
            ones = 0
            zeros = deque()
            i = -1
            for j in range(n):
                if s[j] == "0":
                    zeros.append(j)
                    while len(zeros) > z:
                        ones -= zeros[0] - i - 1
                        i = zeros.popleft()
                else:
                    ones += 1
                
                if len(zeros) == z and ones >= z ** 2:
                    if zeros:
                        ans += min(zeros[0] - i, ones - z ** 2 + 1)
                    else:
                        ans += ones
            z += 1
        return ans