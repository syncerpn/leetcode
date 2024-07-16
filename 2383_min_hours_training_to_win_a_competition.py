# good problem
# make it feel like a game
# solved with kinda prefix sum
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        r_energy = max(0, sum(energy) + 1 - initialEnergy)
        r_exp = 0
        exp = initialExperience
        for i in experience:
            r_exp = max(r_exp, i + 1 - exp)
            exp += i
        
        return r_exp + r_energy