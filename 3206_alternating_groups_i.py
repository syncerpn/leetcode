# circular check by appending the first two elements to the last
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        if len(colors) == 3:
            return int(sum(colors) == 2 or sum(colors) == 1)
        
        n = len(colors)
        colors += colors[:2]
        r = 0
        for i in range(n):
            if colors[i+1] != colors[i] == colors[i+2]:
                r += 1
        
        return r