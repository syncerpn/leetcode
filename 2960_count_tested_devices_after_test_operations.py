# fair problem
# need to think a bit to optimize it
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        c = 0
        for n in batteryPercentages:
            if n > c:
                c += 1
        
        return c