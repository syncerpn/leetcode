# greedy, choose higher-unit boxes first
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        u = 0
        for n, v in boxTypes:
            if n < truckSize:
                u += n * v
                truckSize -= n
            else:
                u += truckSize * v
                return u
        return u