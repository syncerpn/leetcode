# just distribute
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        dA, dB = 0, 0
        ans = []
        for c in seq:
            if c == ")":
                if dA > dB:
                    dA -= 1
                    ans.append(0)
                else:
                    dB -= 1
                    ans.append(1)
            else:
                if dA > dB:
                    dB += 1
                    ans.append(1)
                else:
                    dA += 1
                    ans.append(0)
        return ans