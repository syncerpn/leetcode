# can be solved with brute-force
# but let's do it wisely
# try to find the consecutive "1" from right to left (stop when the first "0" is found)
# remove the lsb "1" of that group
# if there are remaining, shift left back to the length of the original
# (if there none, this becomes 0)
# then append the consecutive "1" group
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
            else:
                t = 0
                c = 0
                while n > 0:
                    if n & 1 == 0:
                        break
                    n >>= 1
                    t = (t << 1) | 1
                    c += 1
                ans.append((n << c) | (t >> 1))
        return ans