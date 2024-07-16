# formulas are given, what else do you expect?
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32.0]