# easy
# somehow has the vibe of adventofcode lol
class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        ans = 0
        i, n = 0, len(instructions)
        e = [False] * n

        while 0 <= i < n:
            s = instructions[i]
            if e[i]:
                break
            
            e[i] = True

            if s == "add":
                ans += values[i]
                i += 1
            elif s == "jump":
                i += values[i]
        
        return ans