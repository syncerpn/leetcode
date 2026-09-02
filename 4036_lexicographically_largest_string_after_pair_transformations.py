# fairly easy
class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        A = "abcdefghijklmnopqrstuvwxyz"
        ans = []
        for a in nums:
            b = bin(a)[2:]
            m = len(b)
            t = []
            for j, c in enumerate(b):
                i = m - 1 - j
                if c == "1":
                    if i >= 25:
                        t += ["z"] * (1 << (i - 25))
                    else:
                        t += [A[i]]
            ans.append("".join(t))
        return ans
