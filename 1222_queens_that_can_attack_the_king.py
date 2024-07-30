# just check 8 dirs
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        for x in range(-1,2):
            for y in range(-1,2):
                if x == 0 and y == 0:
                    continue
                i, j = king
                i += x
                j += y
                while 0 <= i < 8 and 0 <= j < 8:
                    if [i, j] in queens:
                        ans.append([i, j])
                        break
                    i += x
                    j += y
        return ans