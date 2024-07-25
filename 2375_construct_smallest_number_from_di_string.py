# 2 stacks ping pong
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        nums = list("987654321")
        si, sd = [], []
        pattern = pattern[0] + pattern
        p = pattern[0]
        for c in pattern:
            if c == "I":
                while sd:
                    si.append(sd.pop())
                si.append(nums.pop())
            else:
                if c != p:
                    sd.append(si.pop())
                sd.append(nums.pop())
            p = c
        while sd:
            si.append(sd.pop())
        return "".join(si)