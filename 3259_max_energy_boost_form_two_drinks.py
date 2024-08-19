# beautiful dp solution
# thanks to the best time to buy/sell stock problem
# i managed to write this solution with good intuition
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        dpA = 0 # best boost with the last time drank A
        dpB = 0 # best boost with the last time drank B
        for a, b in zip(energyDrinkA, energyDrinkB):
            dpA, dpB = max(dpA + a, dpB), max(dpB + b, dpA)
        return max(dpA, dpB)