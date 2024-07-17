# easy
# just 3 elements, so sorted it to make code compact
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"
        if a == c:
            return "equilateral"
        if a == b or b == c:
            return "isosceles"
        return "scalene"