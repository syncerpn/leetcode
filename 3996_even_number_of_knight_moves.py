# knight moves black to white or white to black in the next move
# just check the cell color
class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        x = start[0] + start[1]
        y = target[0] + target[1]
        return (x % 2) == (y % 2)