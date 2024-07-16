# pure condition checking
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        D = 10 ** 4
        is_bulky = length >= D or width >= D or height >= D or length * width * height >= 10 ** 9
        is_heavy = mass >= 100
        if is_bulky and is_heavy:
            return "Both"
        if not is_bulky and not is_heavy:
            return "Neither"
        return "Bulky" if is_bulky else "Heavy"