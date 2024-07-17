# simulation
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        d = 0
        while mainTank >= 5:
            r = mainTank % 5
            q = mainTank // 5
            b = min(q, additionalTank)
            additionalTank -= b
            d += q * 50
            mainTank = r + b
        
        return d + mainTank * 10

# or math
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        return (mainTank + min((mainTank - 1) // 4, additionalTank)) * 10